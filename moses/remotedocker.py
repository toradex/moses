""" Class used to manage remote docker instance
"""
import io
import logging
import json
import paramiko
import docker
import exceptions
import sshtunnel
import sharedssh


class RemoteDocker:
    """ Manages a remote instance and support with statement
    """

    def __init__(self, device):
        self.dev = device
        self.remotedocker = None

        try:

            self.sshtunnel = sharedssh.SharedSSHDockerTunnel.get_tunnel(device)

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)
        except Exception as e:
            raise e

    def get_image_by_tag(self, tag) -> dict:
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

    def delete_image(self, img, force):

        try:
            self.remotedocker.images.remove(image=img,
                                            force=force,
                                            noprune=False)
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def load_image(self, limg, localpath):
        """Loads an image on the target device

        Arguments:
            img {docker.Image} -- local docker image
            path {str} -- local image path
        """
        try:
            with open(localpath, "rb", buffering=1024*1024) as inp:
                rimg = self.remotedocker.images.load(inp)

            rimg[0].tag(limg.tags[0])

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    @staticmethod
    def make_volume(x: tuple) -> dict:
        return {"bind": x[0], "mode": x[1]}

    def run_image(self,
                  img: docker.models.images.Image,
                  name: str,
                  ports: dict,
                  volumes: dict,
                  devices: list,
                  privileged: bool,
                  extraparms: dict,
                  networks: list) -> docker.models.containers.Container:
        """Runs a new instance of the specified image

        Arguments:
            img {docker.Image} -- image used for the instance
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
            docker.Container -- [description]
        """

        image = self.remotedocker.images.get(img.id)

        if image is None:
            raise exceptions.RemoteImageNotFoundError(img.id)

        try:

            # collect networks to ensure that they are available
            nets = map(self.remotedocker.networks.get, networks)

            # convert ports from string into docker format
            dockerports = dict(
                map(lambda x: (x[0], int(x[1])) if (x[1] is not None and x[1] != "") else (x[0], None), ports.items()))

            # convert volumes from string into docker format
            dockervolumes = dict(
                map(lambda x: (x[0], (x[1]+",rw").split(",")[0:2]), volumes.items()))

            dockervolumes = dict(
                map(lambda x: (x[0], {"bind": x[1][0], "mode": x[1][1]}), dockervolumes.items()))

            container = self.remotedocker.containers.run(image.id,
                                                         name=name,
                                                         privileged=privileged,
                                                         ports=dockerports,
                                                         volumes=dockervolumes,
                                                         devices=devices,
                                                         detach=True,
                                                         **extraparms
                                                         )

            for network in nets:
                network.connect(container)

            return container

        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_containers(self, filters):
        """Returns one or more containers matching the filters

        Arguments:
            filters {list} -- list of strings

        Raises:
            RemoteDockerError -- command error

        Returns:
            list -- array of docker.models.containers.Container objects
        """
        try:
            containers = self.remotedocker.containers.list(all=True,
                                                           filters=filters)
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
        except docker.errors.NotFound:
            return False
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_container(self, container_id: str) -> docker.models.containers.Container:
        """returns a container given its Id

        Arguments:
            container_id {str} -- container id

        Raises:
            exceptions.RemoteDockerError: error on docker on the device

        Returns:
            docker.Container -- container or None
        """
        try:
            return self.remotedocker.containers.get(container_id)
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def get_images(self, filters):
        """Returns one or more images matching the filters

        Arguments:
            filters {list} -- list of strings

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

    def get_image_by_id(self, id):
        """Return information about a specific image

        Arguments:
            tag {str} - - Image tag

        Returns:
            docker.Image -- Image information
        """
        try:
            image = self.remotedocker.images.get(id)
        except docker.errors.ImageNotFound:
            return None
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

        return image

    def remove_image_by_id(self, id):
        try:
            self.remotedocker.images.remove(
                image=id, force=True, noprune=False)
        except docker.errors.ImageNotFound:
            return
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    def remove_container(self, id):
        try:
            container = self.remotedocker.containers.get(id)
            container.remove(v=True, force=True)
        except docker.errors.ImageNotFound:
            return
        except docker.errors.NotFound:
            return
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(self.dev, str(e))

    # enable object to be used in "with" statements

    def __enter__(self):
        localdocker = "tcp://127.0.0.1:"+str(self.sshtunnel.local_bind_port)
        self.remotedocker = docker.DockerClient(
            base_url=localdocker, timeout=1800)
        self.sshtunnel.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        self.remotedocker.close()
        self.sshtunnel.__exit__(type, value, traceback)
