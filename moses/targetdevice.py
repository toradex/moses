"""Classes used to manage connected devices."""
import io
import logging
import os
import re
from typing import Optional, List, Dict, Any
from pathlib import Path
import docker
import paramiko
import sshtunnel
import config
import remotedocker
import console
import serialconsole
import sshconsole
import singleton
import sharedssh
import nameresolution
import rsync
import logs
import progresscookie
import processoutput
import targetdevice_setup
from moses_exceptions import (
    SSHError,
    SSHTunnelError,
    InternalServerError,
    InvalidDeviceError)


# this source file is quite long, but still
# makes sense to keep all target device related
# code together, we may split in the future
# if mi goes above A
# pylint: disable = too-many-lines

PS_CMD_LINE = "ps -A -o pid,ppid,user,time,nice,stat,args"
DF_CMDLINE = "df -k"
FREE_CMD_LINE = "free -k"


# pylint: disable = too-many-instance-attributes
# pylint: disable = too-many-public-methods
class TargetDevice(config.ConfigurableKeysObject):
    """Class used to store information about a specific device.

    Property changes will be saved permanently.
    Methods are used to retrieve information from device, and to
    configure it.
    """

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.copy()
    publicfields: set = set()

    def __init__(self, folder: Optional[Path] = None):
        """Load data from a configuration file.

        :param folder: path to the folder used to store configuration data
        :type folder: Path
        """
        super().__init__(folder)

        self.name = ""
        self.model = ""
        self.hwrev = ""
        self.kernelrelease = ""
        self.kernelversion = ""
        self.distroversion = ""
        self.hostname = ""
        self.dockertunnel: Optional[sshtunnel.SSHTunnelForwarder] = None
        self.sshforwarder: Optional[sharedssh.SSHListenThread] = None
        self.homefolder = ""
        self.runningtorizon = True

        if self.folder is not None:
            self.load()

        self.logs: Dict[str, Any] = {}

    def _build_folder_path(self) -> Path:
        """Generate folder path usign base folder and ID."""
        assert self.id is not None
        return config.ServerConfig().devicespath / self.id

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary,
            if None is passed then self.__dict__ is used
        :type fields: dict
        :returns: true if all fields contain valid values
        :rtype: bool

        """
        if fields is None:
            fields = self.__dict__

            # replace not in filter chars
            if fields["id"] is not None and len(fields["id"]) > 0:
                fields["id"] = re.sub(r"[^-0-9a-zA-Z.]", "", fields["id"])

        if (
            fields["name"] is None
            or fields["hostname"] is None
            or fields["homefolder"] is None
        ):
            return False

        return True

    def __repr__(self) -> str:
        """Generate string rapresentation of the object."""
        return (
            "name :"
            + self.name
            + os.linesep
            + "id : "
            + str(self.id)
            + os.linesep
            + "model : "
            + self.model
            + os.linesep
            + "revision : "
            + self.hwrev
            + os.linesep
            + "kernelname : "
            + self.kernelrelease
            + os.linesep
            + "kernelversion : "
            + self.kernelversion
            + os.linesep
            + "distroversion : "
            + self.distroversion
            + os.linesep
            + "hostname : "
            + self.hostname
            + os.linesep
            + "homefolder : "
            + self.homefolder
            + os.linesep
        )

    def get_containers(self) -> List[dict]:
        """Return a list of containers running on the target device.

        :return: List of containers (as property dictionaries)
        :rtype: List[dict]

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            containers = remotedocker_.get_containers(None)

            jsoncontainers = []

            for container in containers:
                jsoncontainers.append(container.attrs)

            return jsoncontainers

    def get_container(
            self, container_id: str) -> docker.models.containers.Container:
        """Return a container, given its ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            return remotedocker_.get_container(container_id)

    def start_container(
            self, container_id: str) -> docker.models.containers.Container:
        """Start a container, given it ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            container = remotedocker_.get_container(container_id)
            container.start()

            if container_id in self.logs:
                del self.logs[container_id]

            return remotedocker_.get_container(container_id)

    def stop_container(
            self, container_id: str) -> docker.models.containers.Container:
        """Stop a given container.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            container = remotedocker_.get_container(container_id)
            container.stop()
            return remotedocker_.get_container(container_id)

    def get_images(self) -> List[dict]:
        """Return a list of container images available on the target device.

        :returns: list of images as property dictionary
        :rtype: List[dict]

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            return remotedocker_.get_images(None)

    def get_image(self, image_id: str) -> docker.models.images.Image:
        """Return a docker image stored on the target, given it ID.

        :param image_id: image ID (SHA)
        :type image_id: str

        :returns:  image object
        :rtype: docker.models.images.Image

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            return remotedocker_.get_image_by_id(image_id)

    def remove_image(self, image_id: str) -> None:
        """Remove specified image, given its ID.

        :param image_id: image ID (SHA)
        :type image_id: str

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            remotedocker_.remove_image_by_id(image_id)

    def remove_container(self, container_id: str) -> None:
        """Remove specified container, given its ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:
            remotedocker_.remove_container(container_id)

        if container_id in self.logs:
            del self.logs[container_id]

    def expose_docker(self, port: Optional[int]) -> Optional[int]:
        """Expose remote docker REST interface as local port.

        This is done over a safe SSH tunnel

        :param port: local port where shell should be exposed, if None system will use random port
        :type port: int

        :returns: local port where the docker socket is exposed
        :rtype: int

        """
        if self.dockertunnel is not None:
            return None

        try:
            k = paramiko.RSAKey.from_private_key(io.StringIO(self.privatekey))

            if port is not None:
                self.dockertunnel = sshtunnel.SSHTunnelForwarder(
                    ssh_address_or_host=self.hostname,
                    ssh_username=self.username,
                    ssh_pkey=k,
                    local_bind_address=("127.0.0.1", port),
                    remote_bind_address=("127.0.0.1", 2375),
                    allow_agent=False,
                )
            else:
                self.dockertunnel = sshtunnel.SSHTunnelForwarder(
                    ssh_address_or_host=self.hostname,
                    ssh_username=self.username,
                    ssh_pkey=k,
                    remote_bind_address=("127.0.0.1", 2375),
                    allow_agent=False,
                )

            self.dockertunnel.start()

            return self.dockertunnel.local_bind_port
        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except sshtunnel.BaseSSHTunnelForwarderError as exception:
            raise SSHTunnelError(exception) from exception

    def stop_exposing_docker(self) -> None:
        """Disable the docker interface remotized via SSH tunnel."""
        if self.dockertunnel is None:
            return

        try:
            # there is no other way to ensure that the tunnel stops
            # without generating a deadlock
            # pylint: disable = protected-access
            self.dockertunnel._get_transport().sock.shutdown()
            self.dockertunnel.stop()
        # pylint: disable = broad-except
        except Exception:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.dockertunnel = None

    def get_docker_port(self) -> Optional[int]:
        """Return the port where the remote docker socket is exposed on localhost.

        :returns: local port where the docker socket is exposed on
            or None if docker is not exposed locally
        :rtype: int | None

        """
        if self.dockertunnel is None:
            return None

        try:
            return self.dockertunnel.local_bind_port
        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except sshtunnel.BaseSSHTunnelForwarderError as exception:
            raise SSHTunnelError(exception) from exception
        except Exception as exception:
            raise InternalServerError(exception) from exception

    def expose_ssh(self, port: Optional[int]) -> int:
        """Expose an already connected SSH shell on a local port.

        :param port: local port where shell should be exposed,  if None system will use random port
        :type port: int

        :returns: port where shell is exposed
        :rtype: int

        """
        try:
            if self.sshforwarder is not None:
                return self.sshforwarder.get_port()

            self.sshforwarder = sharedssh.SSHListenThread(port, self)
            self.sshforwarder.start()

            return self.sshforwarder.get_port()
        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except sshtunnel.BaseSSHTunnelForwarderError as exception:
            raise SSHTunnelError(exception) from exception
        except Exception as exception:
            raise InternalServerError(exception) from exception

    def stop_exposing_ssh(self) -> None:
        """Stop exposing local port for SSH shell."""
        try:
            if self.sshforwarder is None:
                return

            self.sshforwarder.stop()
        # pylint: disable = broad-except
        except Exception:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.sshforwarder = None

    def get_ssh_port(self) -> Optional[int]:
        """Return the port where the remote SSH shell is exposed on localhost.

        :returns: local port where the remote shell is exposed on
            or None if shell is not exposed locally
        :rtype: int

        """
        if self.sshforwarder is None:
            return None

        try:
            return self.sshforwarder.get_port()
        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except sshtunnel.BaseSSHTunnelForwarderError as exception:
            raise SSHTunnelError(exception) from exception
        except Exception as exception:
            raise InternalServerError(exception) from exception

    def get_process_list(self) -> List[Dict[str, Any]]:
        """Return jsonizable list of local processes.

        :returns: list of processed as a property dictionary
        :rtype: List[Dict[str,Any]]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:
                return processoutput.process_ps_output(
                    ssh.exec_command(PS_CMD_LINE)[1])

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception

    def get_container_process_list(
            self, container_id: str) -> List[Dict[str, Any]]:
        """Return jsonizable list of processes running inside a specific container.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: list of processed as a property dictionary
        :rtype: List[Dict[str,Any]]

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:

            container = remotedocker_.get_container(container_id)
            plist = container.exec_run(PS_CMD_LINE)[1]

            return processoutput.process_ps_output(
                io.StringIO(plist.decode("utf-8")))

    def get_memoryinfo(self) -> Dict[str, int]:
        """Retrieve memory information for the device as jsonizable dictionary.

        :returns: MemInfo struct (total/free/available kb) as property dictionary
        :rtype: Dict[str, int]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return processoutput.process_free_output(
                    ssh.exec_command(FREE_CMD_LINE)[1])

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception

    def get_container_memoryinfo(self, container_id: str) -> Dict[str, int]:
        """Retrieve memory information for as specific container as jsonizable dictionary.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: MemInfo struct (total/free/available kb) as property dictionary
        :rtype: Dict[str, int]

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:

            container = remotedocker_.get_container(container_id)
            plist = container.exec_run(FREE_CMD_LINE)[1]

            return processoutput.process_free_output(
                io.StringIO(plist.decode("utf-8")))

    def get_storageinfo(self) -> List[Dict[str, Any]]:
        """Retrieve storage information for the device as jsonizable dictionary.

        :returns: StorageInfo struct  as property dictionary
        :rtype: List[Dict[str,Any]]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return processoutput.process_df_output(
                    ssh.exec_command(DF_CMDLINE)[1])

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception

    def get_container_storageinfo(self, container_id: str) -> list:
        """Retrieve storage information for a specific container as jsonizable dictionary.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: StorageInfo struct  as property dictionary
        :rtype: List[Dict[str,Any]]

        """
        with remotedocker.RemoteDocker(self) as remotedocker_:

            container = remotedocker_.get_container(container_id)
            plist = container.exec_run(DF_CMDLINE)[1]

            return processoutput.process_df_output(
                io.StringIO(plist.decode("utf-8")))

    def sync_folders(
        self,
        sourcefolder: str,
        destfolder: str,
        progress: Optional[progresscookie.ProgressCookie],
    ) -> None:
        """Syncronize a local folder and a folder on the target device.

        :param sourcefolder: local folder
        :type sourcefolder: str
        :param destfolder: remote folder (on target)
        :type destfolder: str
        :param progress: object used to notify about operation progress
        :type progress: progresscookie.ProgressCookie, optional

        """
        assert self.id is not None

        rsync.run_rsync(
            sourcefolder,
            self.id,
            destfolder,
            None,
            None,
            progress)

    def get_current_ip(self) -> str:
        """Return the device current ip.

        :returns: device ip or hostname if it was not possible to solve it
        :rtype: str

        """
        ipaddress, _ = nameresolution.resolve_hostname(self.hostname)

        return ipaddress

    def get_container_logs(self, container_id: str,
                           restart: bool) -> Optional[str]:
        """Return one line of a specific container logs.

        :param container_id: container ID (SHA)
        :type container_id: str
        :param restart: if true then the log will be returned from first line
        :type restart: bool

        :returns: one line from the logs
        :rtype: str

        """
        log = None

        if container_id in self.logs and not restart:
            log = self.logs[container_id]
        else:
            container = self.get_container(container_id)
            log = container.logs(stream=True)
            self.logs[container_id] = log

        return logs.get_log_chunk(log)

    # support for serialization

    def __getstate__(self) -> Dict[str, Any]:
        """Return a dictionary with exported properties.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        fields = super().__getstate__()
        del fields["dockertunnel"]
        del fields["sshforwarder"]
        del fields["logs"]
        return fields


class TargetDevices(Dict[str, TargetDevice], metaclass=singleton.Singleton):
    """Class that manages the list of devices.

    Works only as a container, Specific properties are accessed
    using the :class:`TargetDevice` class

    """

    def __init__(self) -> None:
        """Initialize global structs and load configured devices."""
        # Iterates on all devices
        subfolders = [
            dir for dir in config.ServerConfig().devicespath.iterdir() if dir.is_dir()
        ]

        for subfolder in subfolders:
            try:
                dev = TargetDevice(subfolder)

                assert dev.id is not None

                # pylint false positive
                # pylint: disable = unsupported-assignment-operation
                self[dev.id] = dev
            # pylint: disable = broad-except
            except Exception:
                logging.exception(
                    "Can't create device from folder %s.", str(subfolder))

    def __delitem__(self, device_id: str) -> None:
        """Remove a device and its data.

        :param device_id: device ID
        :type device_id: str

        """
        # pylint false positive
        # pylint: disable = unsupported-membership-test
        if device_id not in self:
            return

        self[device_id].destroy()
        dict.__delitem__(self, device_id)

    def _setup_device(
        self,
        console_: console.GenericConsole,
        username: str,
        password: str,
        timeout: int,
    ) -> TargetDevice:
        """Configure device to be used with ide-extensions.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :param timeout: timeout in seconds
        :type timeout: int

        """
        console_.login(username, password, timeout * 2)

        logging.warning("DETECT - Login successful.")

        device = TargetDevice()

        targetdevice_setup.setup_device_from_console(device, console_, timeout)

        device.username = username

        assert device.id is not None

        # keeps keys
        # pylint false positive
        # pylint: disable = unsupported-membership-test
        if device.id in self:
            device.publickey = self[device.id].publickey
            device.privatekey = self[device.id].privatekey

        targetdevice_setup.check_sudo(console_, username, password)

        device.save()

        targetdevice_setup.unlock_ssh(console_, device, timeout)
        targetdevice_setup.enable_docker_interface(console_, timeout, password)
        targetdevice_setup.add_debug_warning(console_, timeout)
        targetdevice_setup.reboot_device(console_, password)
        # pylint false positive
        # pylint: disable = unsupported-assignment-operation
        self[device.id] = device
        return device

    def add_serial_device(
        self, port: str, username: str, password: str
    ) -> TargetDevice:
        """Initialize a device using serial port.

        :param port: OS-specific port name (COM*: on Windows, /dev/tty* on Linux)
        :type port: str
        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :returns: device object
        :rtype: TargetDevice

        """
        timeout = config.ServerConfig().commandtimeout

        logging.info("DETECT - Trying to detect device on port %s.", port)

        with serialconsole.SerialConsole(port) as console_:
            return self._setup_device(console_, username, password, timeout)

    def add_network_device(
        self, hostname: str, username: str, password: str
    ) -> TargetDevice:
        """Initialize a device using network.

        :param hostname: device hostname or ip as string
        :type hostname: str
        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :returns: device object
        :rtype: TargetDevice

        """
        timeout = config.ServerConfig().commandtimeout

        logging.info("DETECT - Trying to detect device %s.", hostname)

        with sshconsole.SSHConsole(hostname) as console_:
            dev = self._setup_device(console_, username, password, timeout)

            ipaddress, mdns = nameresolution.resolve_hostname(dev.hostname)

            if ipaddress == dev.hostname:
                dev.hostname = hostname
                logging.warning(
                    f"Can't solve hostname {hostname} saving address used for detection instead.")
                dev.save()
            elif mdns:
                dev.hostname = dev.hostname + ".local"
                logging.warning(
                    "Added .local suffix to support mdns resolution.")
                dev.save()

            return dev

    def refresh_device_info(self, device_id: str) -> TargetDevice:
        """Read information from a device.

        :param device_id: device ID
        :type device_id: str

        :returns: device object
        :rtype: TargetDevice

        """
        timeout = config.ServerConfig().commandtimeout

        # pylint false positive
        # pylint: disable = unsupported-membership-test
        if not device_id in self:
            raise InvalidDeviceError(device_id)

        dev = self[device_id]

        with sshconsole.SSHConsole(dev.hostname) as console_:
            assert dev.username is not None
            assert dev.privatekey is not None
            console_.connect(dev.username, dev.privatekey)
            targetdevice_setup.get_version_info_from_console(
                console_, dev, timeout)

        dev.save()
        return dev
