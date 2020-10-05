""" Class used to manage remote docker instance
"""
import io
import time
import logging
import json
import yaml
import paramiko
import docker
import exceptions
import sshtunnel
import sharedssh
import targetdevice
import progresscookie
import dockerapi
from typing import Optional, List, Dict, Any


class RemoteDocker:
    """ Manages a remote instance and support with statement
    """

    def __init__(self, device: "targetdevice.TargetDevice"):
        self.dev = device
        self.remotedocker: docker.DockerClient = None

        try:

            self.sshtunnel = sharedssh.SharedSSHDockerTunnel.get_tunnel(device)

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)

    def get_image_by_tag(self, tag: str) -> Optional[dict]:
        """Return information about a specific image

        Arguments:
            tag {str} - - Image tag

        Returns:
            dict -- Image information
        """
        try:
            image = self.remotedocker.images.get(tag)
        except docker.errors.ImageNotFound:
            return None
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

        return image.attrs

    def delete_image(self, img: str, force: bool) -> None:
        """Removes a remote image

        Args:
            img (str): image name
            force (bool): terminates existing instances

        Raises:
            exceptions.RemoteDockerError: [description]
        """

        try:

            self.remotedocker.images.remove(image=img, force=force, noprune=False)

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def load_image(
        self,
        limg: docker.models.images.Image,
        localpath: str,
        progress: Optional[progresscookie.ProgressCookie],
    ) -> None:
        """Loads an image on the target device

        Arguments:
            img {docker.models.images.Image} -- local docker image
            path {str} -- local image path
        """
        try:

            rimg = dockerapi.load_image(
                self.remotedocker, localpath, self.dev, progress
            )

            if rimg is None:
                raise exceptions.ImageNotFoundError(localpath)

            rimg.tag(limg.tags[0])

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def run_image(
        self,
        img: docker.models.images.Image,
        name: str,
        ports: Dict[str, Optional[str]],
        volumes: Dict[str, str],
        devices: List[str],
        privileged: bool,
        extraparms: Dict[str, str],
        networks: List[str],
    ) -> docker.models.containers.Container:
        """Runs a new instance of the specified image

        Arguments:
            img {docker.models.images.Image} -- image used for the instance
            name {str} -- instance name
            ports {dict} -- dictionary of local ports
            volumes {dict} -- dictionary of volumes to be mounted
            devices {list} -- list of device
            privileged {bool} -- if true runs as privileged
            extraparms {dict} -- additional parameters in a dictionary
            networks {list} -- networks that should be connected to the container

        Raises:
            exceptions.RemoteImageNotFoundError: [description]
            exceptions.RemoteDockerError: [description]

        Returns:
            docker.models.containers.Container -- [description]
        """

        image = self.remotedocker.images.get(img.id)

        if image is None:
            raise exceptions.RemoteImageNotFoundError(img.id)

        try:

            # collect networks to ensure that they are available
            nets = map(self.remotedocker.networks.get, networks)

            # convert ports from string into docker format
            dockerports = dict(
                map(
                    lambda x: (x[0], int(x[1]))
                    if (x[1] is not None and x[1] != "")
                    else (x[0], None),
                    ports.items(),
                )
            )

            # convert volumes from string into docker format
            dockervolumesstr = dict(
                map(
                    lambda x: (x[0].strip(), (x[1].strip() + ",rw").split(",")[0:2]),
                    volumes.items(),
                )
            )

            dockervolumes = dict(
                map(
                    lambda x: (x[0], {"bind": x[1][0], "mode": x[1][1]}),
                    dockervolumesstr.items(),
                )
            )

            dockerextraparms = dict(
                map(lambda x: (x[0].strip(), yaml.full_load(x[1])), extraparms.items())
            )

            if "ports" in dockerextraparms:
                dockerports.update(dockerextraparms["ports"])
                del dockerextraparms["ports"]

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

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_containers(
        self, filters: Dict[str, Any]
    ) -> List[docker.models.containers.Container]:
        """Returns one or more containers matching the filters

        Arguments:
            filters {list} -- list of strings

        Raises:
            RemoteDockerError -- command error

        Returns:
            list -- array of docker.models.containers.Container objects
        """
        try:
            containers = self.remotedocker.containers.list(all=True, filters=filters)
            return containers

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def is_container_running(self, container_id: str) -> bool:
        """checks if a container is running

        Arguments:
            container_id {str} -- container id

        Returns:
            bool -- true if container exists
        """
        try:
            if self.remotedocker.containers.get(container_id):
                return True
            return False

        except docker.errors.NotFound:
            return False
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))
        except Exception as e:
            raise e

    def get_container(self, container_id: str) -> docker.models.containers.Container:
        """returns a container given its Id

        Arguments:
            container_id {str} -- container id

        Raises:
            exceptions.RemoteDockerError: error on docker on the device

        Returns:
            docker.models.containers.Container -- container
        """
        try:
            return self.remotedocker.containers.get(container_id)
        except docker.errors.NotFound:
            return None
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_images(self, filters: Dict[str, Any]) -> List[dict]:
        """Returns one or more images matching the filters

        Arguments:
            filters {dict} -- list of strings

        Raises:
            RemoteDockerError -- command error

        Returns:
            list -- array of dict objects
        """
        try:
            images = self.remotedocker.images.list(filters)

            jsonimages = []

            for img in images:
                jsonimages.append(img.attrs)

            return jsonimages

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_image_by_id(self, id: str) -> docker.models.images.Image:
        """Return information about a specific image

        Arguments:
            id {str} - - Image tag

        Returns:
            docker.models.images.Image -- Image information
        """
        try:
            image = self.remotedocker.images.get(id)
        except docker.errors.ImageNotFound:
            return None
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

        return image

    def remove_image_by_id(self, id: str) -> None:
        """removes a remote image

        Args:
            id (str): image id

        Raises:
            exceptions.RemoteDockerError: docker error
        """
        try:
            self.remotedocker.images.remove(image=id, force=True, noprune=False)
            return

        except docker.errors.ImageNotFound:
            return
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def remove_container(self, id: str) -> None:
        """removes a remote container

        Args:
            id (str): container id

        Raises:
            exceptions.RemoteDockerError: docker exception
        """
        try:
            container = self.remotedocker.containers.get(id)
            container.remove(v=True, force=True)
            return

        except docker.errors.ImageNotFound:
            return
        except docker.errors.NotFound:
            return
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_network(self, network: str) -> docker.models.networks.Network:
        """Returns a network given its name

        Args:
            network (str): network name

        Returns:
            docker.Network: network object
        """
        list = self.remotedocker.networks.list(names=[network])

        if len(list) == 0:
            return None

        return list[0]

        # enable object to be used in "with" statements

    def __enter__(self):

        if self.sshtunnel is None:
            e = exceptions.SSHTunnelError(Exception("Tunnel is not connected."))
            self.sshtunnel.__exit__(type(e), e, None)
            raise e

        if not (self.sshtunnel.is_active and self.sshtunnel.is_alive):
            e = exceptions.SSHTunnelError(Exception("Tunnel is not connected."))
            self.sshtunnel.__exit__(type(e), e, None)
            raise e

        localdocker = "tcp://127.0.0.1:" + str(self.sshtunnel.local_bind_port)
        self.remotedocker = docker.DockerClient(base_url=localdocker, timeout=1800)
        self.sshtunnel.__enter__()
        return self

    def __exit__(self, etype, value, traceback):
        self.remotedocker.close()
        self.sshtunnel.__exit__(etype, value, traceback)
