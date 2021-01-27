"""Classes used to manage connected devices."""
import exceptions
import io
import logging
import os
import pathlib
import docker
import paramiko
import sshtunnel
import config
import docker
import remotedocker
import console
import serialconsole
import sshconsole
import singleton
import sharedssh
import rsync
import utils
import re
import progresscookie
from typing import Optional, List, Dict, Any, Iterable


PS_CMD_LINE = "ps -A -o pid,ppid,user,time,nice,stat,args"
DF_CMDLINE = "df -k"
FREE_CMD_LINE = "free -k"


class TargetDevice(config.ConfigurableKeysObject):
    """Class used to store information about a specific device.

    Property changes will be saved permanently.
    Methods are used to retrieve information from device, and to
    configure it.
    """

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.copy()

    def __init__(self, folder: Optional[pathlib.Path] = None):
        """Load data from a configuration file.

        :param folder: path to the folder used to store configuration data
        :type folder: pathlib.Path
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

    def _build_folder_path(self) -> pathlib.Path:
        """Generate folder path usign base folder and ID."""
        assert self.id is not None
        return config.ServerConfig().devicespath / self.id

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary, if None is passed then self.__dict__ is used
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
        with remotedocker.RemoteDocker(self) as rd:
            containers = rd.get_containers(None)

            jsoncontainers = []

            for container in containers:
                jsoncontainers.append(container.attrs)

            return jsoncontainers

    def get_container(self, container_id: str) -> docker.models.containers.Container:
        """Return a container, given its ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_container(container_id)

    def start_container(self, container_id: str) -> docker.models.containers.Container:
        """Start a container, given it ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as rd:
            container = rd.get_container(container_id)
            container.start()

            if container_id in self.logs:
                del self.logs[container_id]

            return rd.get_container(container_id)

    def stop_container(self, container_id: str) -> docker.models.containers.Container:
        """Stop a given container.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: container object
        :rtype: docker.models.containers.Container

        """
        with remotedocker.RemoteDocker(self) as rd:
            container = rd.get_container(container_id)
            container.stop()
            return rd.get_container(container_id)

    def get_images(self) -> List[dict]:
        """Return a list of container images available on the target device.

        :returns: list of images as property dictionary
        :rtype: List[dict]

        """
        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_images(None)

    def get_image(self, image_id: str) -> docker.models.images.Image:
        """Return a docker image stored on the target, given it ID.

        :param image_id: image ID (SHA)
        :type image_id: str

        :returns:  image object
        :rtype: docker.models.images.Image

        """
        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_image_by_id(image_id)

    def remove_image(self, image_id: str) -> None:
        """Remove specified image, given its ID.

        :param image_id: image ID (SHA)
        :type image_id: str

        """
        with remotedocker.RemoteDocker(self) as rd:
            rd.remove_image_by_id(image_id)

    def remove_container(self, container_id: str) -> None:
        """Remove specified container, given its ID.

        :param container_id: container ID (SHA)
        :type container_id: str

        """
        with remotedocker.RemoteDocker(self) as rd:
            rd.remove_container(container_id)

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
        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)

    def stop_exposing_docker(self) -> None:
        """Disable the docker interface remotized via SSH tunnel."""
        if self.dockertunnel is None:
            return

        try:
            self.dockertunnel._get_transport().sock.shutdown()
            self.dockertunnel.stop()
        except:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.dockertunnel = None

    def get_docker_port(self) -> Optional[int]:
        """Return the port where the remote docker socket is exposed on localhost.

        :returns: local port where the docker socket is exposed on None if docker is not exposed locally
        :rtype: int | None

        """
        if self.dockertunnel is None:
            return None

        try:
            return self.dockertunnel.local_bind_port
        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)
        except Exception as e:
            raise exceptions.InternalServerError(e)
        raise exceptions.InternalServerError(None)

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
        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)
        except Exception as e:
            raise exceptions.InternalServerError(e)
        raise exceptions.InternalServerError(None)

    def stop_exposing_ssh(self) -> None:
        """Stop exposing local port for SSH shell."""
        try:
            if self.sshforwarder is None:
                return

            self.sshforwarder.stop()
        except:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.sshforwarder = None

    def get_ssh_port(self) -> Optional[int]:
        """Return the port where the remote SSH shell is exposed on localhost.

        :returns: local port where the remote shell is exposed on None if shell is not exposed locally
        :rtype: int

        """
        if self.sshforwarder is None:
            return None

        try:
            return self.sshforwarder.get_port()
        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise exceptions.SSHTunnelError(e)
        except Exception as e:
            raise exceptions.InternalServerError(e)
        raise exceptions.InternalServerError(None)

    def _process_ps_output(self, stream: Iterable[str]) -> List[Dict[str, Any]]:
        """Convert output of ps command into a jsonizable dictionary.

        :param stream: output of ps command
        :type stream: Iterable[str]

        :returns: list of running processes with their properties as dictionary
        :rtype: List[Dict[str,Any]]

        """
        # 1st row contains headers
        first = True
        processes = []

        for line in stream:
            if first:
                first = False
                continue
            fields = line.split()

            if len(fields) < 7:
                continue

            process: Dict[str, Any] = {}
            process["pid"] = int(fields[0])
            process["ppid"] = int(fields[1])
            process["user"] = str(fields[2])
            process["time"] = str(fields[3])
            process["nice"] = 0 if str(fields[4]) == "-" else int(fields[4])
            process["state"] = str(fields[5])
            cmd = str(fields[6])

            for i in range(7, len(fields)):
                cmd = cmd + " " + str(fields[i])

            process["args"] = cmd
            processes.append(process)

        return processes

    def get_process_list(self) -> List[Dict[str, Any]]:
        """Return jsonizable list of local processes.

        :returns: list of processed as a property dictionary
        :rtype: List[Dict[str,Any]]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:
                return self._process_ps_output(ssh.exec_command(PS_CMD_LINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_process_list(self, container_id: str) -> List[Dict[str, Any]]:
        """Return jsonizable list of processes running inside a specific container.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: list of processed as a property dictionary
        :rtype: List[Dict[str,Any]]

        """
        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(PS_CMD_LINE)[1]

            return self._process_ps_output(io.StringIO(plist.decode("utf-8")))

    def _process_free_output(self, stream: Iterable[str]) -> Dict[str, int]:
        """Collect output of free command as jsonizable dictionary.

        :param stream: output of free command
        :type stream: Iterable[str]

        :returns: MemInfo struct (total/free/available kb) as property dictionary
        :rtype: Dict[str, int]

        """
        # 1st row contains headers
        first = True

        meminfo = {"total": -1, "free": -1, "available": -1}

        for line in stream:
            if first:
                first = False
                continue

            fields = line.split()

            meminfo["total"] = int(fields[1])
            meminfo["free"] = int(fields[3])
            meminfo["available"] = int(fields[6])

            # only 1st line needs to be parsed
            break

        return meminfo

    def get_memoryinfo(self) -> Dict[str, int]:
        """Retrieve memory information for the device as jsonizable dictionary.

        :returns: MemInfo struct (total/free/available kb) as property dictionary
        :rtype: Dict[str, int]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return self._process_free_output(ssh.exec_command(FREE_CMD_LINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_memoryinfo(self, container_id: str) -> Dict[str, int]:
        """Retrieve memory information for as specific container as jsonizable dictionary.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: MemInfo struct (total/free/available kb) as property dictionary
        :rtype: Dict[str, int]

        """
        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(FREE_CMD_LINE)[1]

            return self._process_free_output(io.StringIO(plist.decode("utf-8")))

    def _process_df_output(self, stream: Iterable[str]) -> List[Dict[str, Any]]:
        """Collect output of df command as a list of jsonable dictionary.

        :param stream: output of df command
        :type stream: Iterable[str]

        :returns: StorageInfo struct as property dictionary
        :rtype: List[Dict[str,Any]]

        """
        # 1st row contains headers
        first = True
        storages = []

        for line in stream:
            if first:
                first = False
                continue

            fields = line.split()

            if len(fields) < 6:
                continue

            storage: Dict[str, Any] = {}
            storage["filesystem"] = fields[0]
            storage["size"] = int(fields[1])
            storage["available"] = int(fields[3])
            storage["mountpoint"] = fields[5]

            storages.append(storage)

        return storages

    def get_storageinfo(self) -> List[Dict[str, Any]]:
        """Retrieve storage information for the device as jsonizable dictionary.

        :returns: StorageInfo struct  as property dictionary
        :rtype: List[Dict[str,Any]]

        """
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return self._process_df_output(ssh.exec_command(DF_CMDLINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_storageinfo(self, container_id: str) -> list:
        """Retrieve storage information for a specific container as jsonizable dictionary.

        :param container_id: container ID (SHA)
        :type container_id: str

        :returns: StorageInfo struct  as property dictionary
        :rtype: List[Dict[str,Any]]

        """
        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(DF_CMDLINE)[1]

            return self._process_df_output(io.StringIO(plist.decode("utf-8")))

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

        rsync.run_rsync(sourcefolder, self.id, destfolder, None, None, progress)

    def get_current_ip(self) -> str:
        """Return the device current ip.

        :returns: device ip or hostname if it was not possible to solve it
        :rtype: str

        """
        ip, _ = sharedssh.resolve_hostname(self.hostname)

        return ip

    def get_container_logs(self, container_id: str, restart: bool) -> Optional[str]:
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

        return utils.get_log_chunk(log)

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

    def save(self) -> None:
        """Save object data.

        On object first save the key pair is generated and stored inside the object's configuration.

        """
        super().save()


class TargetDevices(Dict[str, TargetDevice], metaclass=singleton.Singleton):
    """Class that manages the list of devices.

    Works only as a container, Specific properties are accessed
    using the :class:`TargetDevice` class

    """

    def __init__(self) -> None:
        """Initialize global structs and load configured devices."""
        # dictionary with supported modules
        self.modeldict = dict.fromkeys(["0014", "0015", "0016", "0017"], "colibri-imx6")
        self.modeldict.update(dict.fromkeys(["0032", "0033", "0039"], "colibri-imx7"))
        self.modeldict.update(
            dict.fromkeys(["0027", "0028", "0029", "0035"], "apalis-imx6")
        )
        self.modeldict.update(
            dict.fromkeys(["0036", "0040", "0044", "0045"], "colibri-imx6ull")
        )
        self.modeldict.update(
            dict.fromkeys(
                ["0037", "0047", "0048", "0049", "0046", "0053", "0054", "0038"],
                "apalis-imx8",
            )
        )
        self.modeldict.update(
            dict.fromkeys(["0038", "0050", "0051", "0052"], "colibri-imx8")
        )
        self.modeldict.update(
            dict.fromkeys(["0055", "0056", "0057", "0059", "0060"], "verdin-imx8")
        )

        # Iterates on all devices
        subfolders = [
            dir for dir in config.ServerConfig().devicespath.iterdir() if dir.is_dir()
        ]

        for dir in subfolders:
            try:
                dev = TargetDevice(dir)

                assert dev.id is not None

                self[dev.id] = dev
            except:
                logging.exception("Can't create device from folder %s.", str(dir))

    def __delitem__(self, device_id: str) -> None:
        """Remove a device and its data.

        :param device_id: device ID
        :type device_id: str

        """
        if device_id not in self:
            return

        self[device_id].destroy()
        dict.__delitem__(self, device_id)

    def _unlock_ssh(
        self, console: console.GenericConsole, dev: TargetDevice, timeout: int
    ) -> None:
        """Enable ssh connection to the device without having to use a password.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param dev: target device
        :type dev: TargetDevice
        :param timeout: timeout in seconds
        :type timeout: int

        """
        keysfile = console.send_cmd("ls .ssh/authorized_keys", timeout)

        keys = None

        # file does not exists
        if keysfile != ".ssh/authorized_keys":
            keys = dev.publickey
        else:
            keys = console.send_cmd("cat .ssh/authorized_keys", timeout)

            assert dev.publickey is not None

            if dev.publickey not in keys:
                keys += "\n" + dev.publickey

        assert keys is not None

        # regenerates the keys file
        console.send_cmd("mkdir .ssh")
        console.send_cmd('echo "' + keys + '" > .ssh/authorized_keys')
        console.send_cmd("chmod 644 .ssh/authorized_keys")
        console.send_cmd("chmod 700 .ssh")

    def _check_sudo(
        self, console: console.GenericConsole, username: str, password: str
    ) -> None:
        """Check that user can run commands as root.

        If sudo is not enabled for the user, then an exception is rised

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param username: username
        :type username: str
        :param password: password
        :type password: str

        """
        if "sudo enabled" not in console.send_cmd(
            'echo "' + password + '" | sudo -S echo "sudo enabled"'
        ):
            raise exceptions.SudoError(username)

    def _add_debug_warning(self, console: console.GenericConsole, timeout: int) -> None:
        """Add a warning message at boot for devices where ide-connectivity has been enabled.

        :param console: SSH or serial console
        :type console: console.GenericConsole
        :param timeout: timeout in seconds
        :type timeout: int
        """
        # TODO add a warning to boot scripts
        pass

    def _get_version_info_from_console(
        self, console: console.GenericConsole, dev: TargetDevice, timeout: int
    ) -> None:
        """Collect device version info from a console.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param dev: target device
        :type dev: TargetDevice
        :param timeout: timeout in seconds
        :type timeout: int

        """
        dev.hwrev = console.send_cmd(
            "cat /proc/device-tree/toradex,board-rev", timeout
        ).rstrip("\x00")

        # Community device
        if "No such file or directory" in dev.hwrev:
            dev.hwrev = "v?.?"

        dev.kernelrelease = console.send_cmd("uname -r", timeout).rstrip("\x00\n")

        dev.kernelversion = console.send_cmd("uname -v", timeout).rstrip("\x00\n")

        dev.distroversion = (
            console.send_cmd("cat /usr/lib/os-release | grep PRETTY_NAME=", timeout)
            .rstrip("\x00")
            .strip()
        )

        dev.distroversion = dev.distroversion.lstrip("PRETTY_NAME=")
        dev.distroversion = dev.distroversion.strip('"')

    def _create_device_from_console(
        self, console: console.GenericConsole, timeout: int
    ) -> TargetDevice:
        """Create a new device collecting its information from the console.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param timeout: timeout in seconds
        :type timeout: int
        :returns: device object
        :rtype: TargetDevice

        """
        dev = TargetDevice()

        dev.id = console.send_cmd(
            "cat /proc/device-tree/serial-number", timeout
        ).rstrip("\x00")

        # Toradex Devices has product Id
        productId = console.send_cmd(
            "cat /proc/device-tree/toradex,product-id", timeout
        ).rstrip("\x00")

        if "No such file or directory" not in productId:
            logging.info("DETECT - Toradex device id %s", dev.id)
            dev.model = productId
            dev.hostname = self.get_hostname_from_model(dev.model)
        elif len(str(dev.id)) > 0:
            logging.info("DETECT - Community device id %s", dev.id)
            dev.runningtorizon = False

            # Check if the distro have docker
            dockerCheck = console.send_cmd("ls /var/run/docker.sock", timeout).rstrip(
                "\x00"
            )

            if "No such file or directory" in dockerCheck:
                logging.info(
                    "Docker socket not present, make sure you have "
                    + "Docker installed and running on your board."
                )
                raise exceptions.InvalidDeviceError(dev)

            # Check if the board in running arm or arm64
            archCheck = console.send_cmd("arch", timeout).rstrip("\x00")

            if "arm" not in archCheck:
                logging.info("Unsupported architecture %s", archCheck)
                raise exceptions.InvalidDeviceError(dev)

            # Community Devices has Model name
            dev.model = console.send_cmd("cat /proc/device-tree/model", timeout).rstrip(
                "\x00"
            )

            dev.hostname = console.send_cmd("cat /etc/hostname", timeout).rstrip("\x00")
        else:
            raise exceptions.InvalidDeviceIdError()

        logging.info("DETECT - %s detected :: Model %s", dev.hostname, dev.model)

        dev.name = (
            console.send_cmd("cat /proc/device-tree/model", timeout).rstrip("\x00")
            + "("
            + dev.id
            + ")"
        )

        dev.hostname = console.send_cmd("hostname", timeout).rstrip("\x00").strip()

        dev.homefolder = console.send_cmd("echo $HOME", timeout).rstrip("\x00").strip()

        self._get_version_info_from_console(console, dev, timeout)

        if not dev.is_valid():
            logging.warning("DETECT - Device information is not valid.")
            logging.warning(repr(dev))
            raise exceptions.InvalidDeviceError(dev)
        return dev

    def _reboot_device(self, console: console.GenericConsole, password: str) -> None:
        """Reboot target device at the end of setup process.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param password: password
        :type password: str

        """
        try:
            console.send_cmd("echo " + password + " | sudo -S reboot", 0)
        except exceptions.TimeoutError:
            pass

    def _enable_docker_interface(
        self, console: console.GenericConsole, timeout: int, password: str
    ) -> None:
        """Enable docker TCP/IP interface on localhost.

        :param console: serial or SSH console
        :type console: console.GenericConsole
        :param timeout: timeout in seconds
        :type timeout: int
        :param password: password
        :type password: str

        """
        # checks if override folder exists
        folder = (
            console.send_cmd(
                "echo "
                + password
                + " | sudo -S ls /etc/systemd/system/docker.service.d 2> /dev/null",
                timeout,
            )
            .strip()
            .rstrip("\x00")
        )

        # creates it
        if len(folder) == 0:
            console.send_cmd(
                "echo "
                + password
                + " | sudo -S  mkdir -p /etc/systemd/system/docker.service.d",
                timeout,
            )

        # creates override file
        console.send_cmd(
            "echo " + password + " | sudo -S sh -c \"echo '[Service]\n"
            "ExecStart=\n"
            "ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375\n"
            "' > /etc/systemd/system/docker.service.d/override.conf\"",
            timeout,
        )

    def _setup_device(
        self,
        console: console.GenericConsole,
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
        console.login(username, password, timeout * 2)

        logging.warning("DETECT - Login successful.")

        device = self._create_device_from_console(console, timeout)

        device.username = username

        assert device.id is not None

        # keeps keys
        if device.id in self:
            device.publickey = self[device.id].publickey
            device.privatekey = self[device.id].privatekey

        self._check_sudo(console, username, password)

        device.save()

        self._unlock_ssh(console, device, timeout)
        self._enable_docker_interface(console, timeout, password)
        self._add_debug_warning(console, timeout)
        self._reboot_device(console, password)
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

        with serialconsole.SerialConsole(port) as console:
            return self._setup_device(console, username, password, timeout)

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

        with sshconsole.SSHConsole(hostname) as console:
            dev = self._setup_device(console, username, password, timeout)

            ip, mdns = sharedssh.resolve_hostname(dev.hostname)

            if ip == dev.hostname:
                dev.hostname = hostname
                logging.warning(
                    "Can't solve hostname "
                    + hostname
                    + " saving address used for detection instead."
                )
                dev.save()
            elif mdns:
                dev.hostname = dev.hostname + ".local"
                logging.warning("Added .local suffix to support mdns resolution.")
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

        if not device_id in self:
            raise exceptions.InvalidDeviceError(device_id)

        dev = self[device_id]

        with sshconsole.SSHConsole(dev.hostname) as console:
            assert dev.username is not None
            assert dev.privatekey is not None
            console.connect(dev.username, dev.privatekey)
            self._get_version_info_from_console(console, dev, timeout)

        dev.save()
        return dev

    def get_hostname_from_model(self, model: str) -> str:
        """Return default hostname for specific model.

        :param model: model string
        :type model: str

        :returns: device name prefix
        :rtype: str

        """
        if model in self.modeldict:
            return self.modeldict[model]
        raise exceptions.InvalidModelError(model)
