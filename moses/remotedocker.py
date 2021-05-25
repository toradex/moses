"""Class used to manage remote docker instance.

The backend opens a tunnel to the remote docker instance and then
uses docker APIs over the local socket.

"""
import logging
from types import TracebackType
from typing import Optional, List, Dict, Any, TYPE_CHECKING, Type
import yaml
import paramiko
import docker
import sshtunnel
import sharedssh
import progresscookie
import dockerapi
from moses_exceptions import (
    SSHError,
    SSHTunnelError,
    RemoteDockerError,
    ImageNotFoundError,
    RemoteImageNotFoundError)

if TYPE_CHECKING:
    import targetdevice

def get_mount_info(infostr:str) -> dict:
    """Parse string into docker mount info."""
    modeinfo={ "bind":infostr, "mode":"rw" }
    elements=infostr.split(",")

    if elements[-1] in {"ro","rw"}:
        modeinfo["mode"]=elements[-1]
        modeinfo["bind"]=",".join(elements[:-1])

    return modeinfo

class RemoteDocker:
    """Manages docker instance running on a device."""

    def __init__(self, device: "targetdevice.TargetDevice"):
        """Create the tunnel.

        :param device: target device
        :type device: targetdevice.TargetDevice

        """
        self.dev = device
        self.remotedocker: docker.DockerClient = None

        try:

            self.sshtunnel = sharedssh.SharedSSHDockerTunnel.get_tunnel(device)

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except sshtunnel.BaseSSHTunnelForwarderError as exception:
            raise SSHTunnelError(exception) from exception

    def get_image_by_tag(self, tag: str) -> Optional[dict]:
        """Return information about a specific image.

        :param tag: tag used to find the image
        :tpye tag: str

        :returns: image information as dictionary
        :rtype: dict

        """
        try:
            image = self.remotedocker.images.get(tag)
        except docker.errors.ImageNotFound:
            return None
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

        return image.attrs

    def delete_image(self, img: str, force: bool) -> None:
        """Remove a remote image.

        :param img: image id (SHA)
        :type img: str
        :param force: if true running instances are terminated

        """
        try:

            self.remotedocker.images.remove(
                image=img, force=force, noprune=False)

        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def load_image(
        self,
        limg: docker.models.images.Image,
        localpath: str,
        progress: Optional[progresscookie.ProgressCookie],
    ) -> None:
        """Load an image on the target device.

        :param limg: local docker image
        :type limg: docker.models.images.Image
        :param localpath: local path of the image file to be imported
        :type localpath: str
        :param progress: object used to return progress information
        :type progress: progresscookie.ProgressCookie, optional

        """
        try:

            rimg = dockerapi.load_image(
                self.remotedocker, localpath, self.dev, progress
            )

            if rimg is None:
                raise ImageNotFoundError(localpath)

            rimg.tag(limg.tags[0])

        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    # pylint: disable = too-many-arguments
    # pylint: disable = too-many-locals
    def run_image(
            self,
            img: docker.models.images.Image,
            name: str,
            ports: Dict[str, Optional[str]],
            volumes: Dict[str, str],
            devices: List[str],
            privileged: bool,
            extraparms: Dict[str, str],
            networks: List[str]) -> docker.models.containers.Container:
        """Run a new instance of the specified image.

        :param img: docker image to be used for this instance
        :type img: docker.models.image.Image
        :param name: name to be assigned to the instance
        :type name: str
        :param ports: dictionary with host/container ports
        :type ports: dict
        :param volumes: dictionary with local/container mount point
        :type volumes: dict
        :param devices: list of devices to be shared with container
        :type device: list
        :param privileged: true if the container must run in privileged mode
        :type privileged: bool
        :param extraparms: dictionary with additional parameters and their value
        :type extraparams: dict
        :param networks: list of networks that the container will be connected to
        :type network: list

        :returns: container
        :rtype: docker.models.containers.Container

        """
        image = self.remotedocker.images.get(img.id)

        if image is None:
            raise RemoteImageNotFoundError(img.id)

        try:

            # collect networks to ensure that they are available
            nets = map(self.remotedocker.networks.get, networks)

            dockerextraparms = dict(
                map(lambda x: (x[0].strip(), yaml.full_load(
                    x[1])), extraparms.items())
            )

            if "network_mode" in extraparms and extraparms["network_mode"] == "host":
                dockerports={}

                if "ports" in dockerextraparms:
                    del dockerextraparms["ports"]

                logging.warning("Network mode is set to host, ignoring port settings.")
            else:
                # convert ports from string into docker format
                dockerports = dict(
                    map(
                        lambda x: (x[0], int(x[1]))
                        if (x[1] is not None and x[1] != "")
                        else (x[0], None),
                        ports.items(),
                    )
                )

                if "ports" in dockerextraparms:
                    dockerports.update(dockerextraparms["ports"])
                    del dockerextraparms["ports"]


            # convert volumes from string into docker format
            dockervolumes = dict(
                map(
                    lambda x: (x[0], get_mount_info(x[1])),
                    volumes.items())
            )

            if "volumes" in dockerextraparms:
                dockervolumes.update(dockerextraparms["volumes"])
                del dockerextraparms["volumes"]

            dockerdevices = devices

            if "devices" in dockerextraparms:
                dockerdevices.extend(dockerextraparms["devices"])
                del dockerextraparms["devices"]

            if "privileged" in dockerextraparms:
                privileged = dockerextraparms["privileged"]
                del dockerextraparms["privileged"]

            if "name" in dockerextraparms:
                del dockerextraparms["name"]
                logging.warning("Can't use a different name for container.")

            if "detach" in dockerextraparms:
                del dockerextraparms["detach"]
                logging.warning("container is detached by default.")

            container = self.remotedocker.containers.run(
                image.id,
                name=name,
                privileged=privileged,
                ports=dockerports,
                volumes=dockervolumes,
                devices=dockerdevices,
                detach=True,
                **dockerextraparms
            )

            for network in nets:
                network.connect(container)

            return container

        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def get_containers(
        self, filters: Optional[Dict[str, Any]]
    ) -> List[docker.models.containers.Container]:
        """Return one or more containers matching the filters.

        :param filters: dictionary with filters
        :type filters: dict, optional

        :returns: list of container objects
        :rtype: docker.models.containers.Container

        """
        try:
            containers = self.remotedocker.containers.list(
                all=True, filters=filters)
            return containers

        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def is_container_running(self, container_id: str) -> bool:
        """Check if a container is running.

        :param container_id: str
        :param container_id: str:
        :returns: bool -- true if container exists

        """
        try:
            if self.remotedocker.containers.get(container_id):
                return True
            return False

        except docker.errors.NotFound:
            return False
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def get_container(
            self, container_id: str) -> docker.models.containers.Container:
        """Return a container given its Id.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container
        :rtype: docker.models.containers.Container

        """
        try:
            return self.remotedocker.containers.get(container_id)
        except docker.errors.NotFound:
            return None
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def get_images(self, filters: Optional[Dict[str, Any]]) -> List[dict]:
        """Return one or more images matching the filters.

        :param filters: dictionary with filters
        :type filters: dict, optional

        :returns: list of image objects
        :rtype: list[dict]

        """
        try:
            images = self.remotedocker.images.list(filters)

            jsonimages = []

            for img in images:
                jsonimages.append(img.attrs)

            return jsonimages

        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def get_image_by_id(self, image_id: str) -> docker.models.images.Image:
        """Return information about a specific image.

        :param image_id: image ID (SHA)
        :type image_id: str

        :returns: Image information
        :rtype: docker.models.images.Image

        """
        try:
            image = self.remotedocker.images.get(image_id)
        except docker.errors.ImageNotFound:
            return None
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

        return image

    def remove_image_by_id(self, image_id: str) -> None:
        """Remove a remote image.

        :param image_id: image ID (SHA)
        :type image_id: str

        """
        try:
            self.remotedocker.images.remove(
                image=image_id, force=True, noprune=False)
            return

        except docker.errors.ImageNotFound:
            return
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def remove_container(self, container_id: str) -> None:
        """Remove a remote container.

        :param container_id: container ID (SHA)
        :type container_id: str

        """
        try:
            container = self.remotedocker.containers.get(container_id)
            container.remove(v=True, force=True)
            return

        except docker.errors.ImageNotFound:
            return
        except docker.errors.NotFound:
            return
        except docker.errors.DockerException as exception:
            raise RemoteDockerError(self.dev, str(exception)) from exception

    def get_network(self, network: str) -> docker.models.networks.Network:
        """Return a network given its name.

        :param network: network name
        :type network: str

        :returns: network object
        :rtype: docker.models.networks.Network

        """
        networks_list = self.remotedocker.networks.list(names=[network])

        if len(networks_list) == 0:
            return None

        return networks_list[0]

        # enable object to be used in "with" statements

    def __enter__(self) -> "RemoteDocker":
        """Check that connections are OK before starting remote operations."""
        if self.sshtunnel is None:
            exception = SSHTunnelError(
                Exception("Tunnel is not connected."))
            raise exception

        if not (self.sshtunnel.is_active and self.sshtunnel.is_alive):
            exception = SSHTunnelError(
                Exception("Tunnel is not connected."))
            self.sshtunnel.__exit__(type(exception), exception, None)
            raise exception

        try:
            localdocker = "tcp://127.0.0.1:" + \
                str(self.sshtunnel.local_bind_port)
            self.remotedocker = docker.DockerClient(
                base_url=localdocker, timeout=1800)
        except Exception as exception:
            self.sshtunnel.__exit__(type(exception), exception, None)
            raise exception

        self.sshtunnel.__enter__()
        return self

    def __exit__(
        self,
        etype: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Close shared connections when an exceptions is generated."""
        self.remotedocker.close()

        if self.sshtunnel is not None:
            return self.sshtunnel.__exit__(etype, value, traceback)
        return None
