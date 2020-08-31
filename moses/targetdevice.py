import exceptions
import io
import logging
import os
import platform
import select
import socket
import threading
import time
import pathlib
import docker
import flask
import paramiko
import serial
import sshtunnel
import config
import docker
import remotedocker
import serialconsole
import singleton
import sshconsole
import sharedssh
import yaml
import rsync
import utils
import re
from typing import Optional, List, Dict, Any, Iterable


""" This module contain classes used to manage devices and their connections
"""

PS_CMD_LINE = "ps -A -o pid,ppid,user,time,nice,stat,args"
DF_CMDLINE = "df -k"
FREE_CMD_LINE = "free -k"


class TargetDevice(config.ConfigurableKeysObject):
    """ Class used to store information about a specific device

    Property changes will be saved permanently.
    Methods are used to retrieve information from device, and to
    configure it.
    """

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.copy()

    def __init__(self, folder: Optional[pathlib.Path] = None):
        """Loads data from a configuration file

        Arguments:
            folder {Path} -- Path of the folder used to store
                             target information
        """
        super().__init__(folder)

        self.name = ""
        self.model = ""
        self.hwrev = ""
        self.kernelrelease = ""
        self.kernelversion = ""
        self.torizonversion = ""
        self.hostname = ""
        self.dockertunnel: Optional[sshtunnel.SSHTunnelForwarder] = None
        self.sshforwarder: Optional[sharedssh.SSHListenThread] = None
        self.homefolder = ""
        self.community = False

        if self.folder is not None:
            self.load()

        self.logs: Dict[str, Any] = {}

    def _build_folder_path(self) -> pathlib.Path:
        return config.ServerConfig().devicespath / self.id

    def is_valid(self, fields: dict = None) -> bool:
        """Validate fields of current object

        Arguments:
            fields {dictionary} -- dictionary with values, if None then
                                   self.__dict__ will be used

        Returns:
            bool -- true if all fields contain valid values
        """

        if fields is None:
            fields = self.__dict__

            # replace not in filter chars
            if fields["id"] is not None and len(fields["id"]) > 0:
                fields["id"] = re.sub(r'[^-0-9a-zA-Z.]', '', fields["id"])

        if (
            fields["name"] is None
            or fields["hostname"] is None
            or fields["homefolder"] is None
        ):
            return False

        return True

    def __repr__(self) -> str:
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
            + "torizonversion : "
            + self.torizonversion
            + os.linesep
            + "hostname : "
            + self.hostname
            + os.linesep
            + "homefolder : "
            + self.homefolder
            + os.linesep
        )

    def get_containers(self) -> List[dict]:
        """Returns a list of containers running on the target device

        Raises:
            ConnectionException -- connection error

        Returns:
            list -- containers
        """

        with remotedocker.RemoteDocker(self) as rd:
            containers = rd.get_containers(None)

            jsoncontainers = []

            for container in containers:
                jsoncontainers.append(container.attrs)

            return jsoncontainers

    def get_container(self, container_id: str) -> docker.models.containers.Container:
        """returns a given container

        Arguments:
            container_id {str} -- id of the container

        Returns:
            docker.models.containers.Container -- container
        """
        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_container(container_id)

    def start_container(self, container_id: str) -> docker.models.containers.Container:
        """starts a given container

        Arguments:
            container_id {str} -- id of the container
        """
        with remotedocker.RemoteDocker(self) as rd:
            container = rd.get_container(container_id)
            container.start()

            if container_id in self.logs:
                del self.logs[container_id]

            return rd.get_container(container_id)

    def stop_container(self, container_id: str) -> docker.models.containers.Container:
        """stops a given container

        Arguments:
            container_id {str} -- id of the container
        """
        with remotedocker.RemoteDocker(self) as rd:
            container = rd.get_container(container_id)
            container.stop()
            return rd.get_container(container_id)

    def get_images(self) -> List[dict]:
        """Returns a list of images available on the target device

        Raises:
            ConnectionException -- connection error

        Returns:
            list -- images
        """

        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_images(None)

    def get_image(self, image_id: str) -> docker.models.images.Image:
        """Returns a specific docker image running on target

        Arguments:
            image_id {str} -- image id

        Returns:
            docker.models.images.Image -- image info
        """

        with remotedocker.RemoteDocker(self) as rd:
            return rd.get_image_by_id(image_id)

    def remove_image(self, image_id: str):
        """Removes specified image

        Arguments:
            image_id {string} -- image id
        """
        with remotedocker.RemoteDocker(self) as rd:
            rd.remove_image_by_id(image_id)

    def remove_container(self, container_id: str):
        """Removes specified image

        Arguments:
            container_id {str} -- container id
        """
        with remotedocker.RemoteDocker(self) as rd:
            rd.remove_container(container_id)

        if container_id in self.logs:
            del self.logs[container_id]

    def expose_docker(self, port: Optional[int]) -> Optional[int]:
        """Exposes remote docker REST interface as local port

        Arguments:
            port {int} -- local port where shell should be exposed,
                          if None system will use random port

        Raises:
            exceptions.SSHError -- Error on SSH layer
            exceptions.SSHTunnelError -- Error on SSH tunnel layer

        Returns:
            int -- local port where the docker socket is exposed
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

    def stop_exposing_docker(self):
        """Disable the docker interface remotized via SSH tunnel
        """

        if self.dockertunnel is None:
            return

        try:
            self.dockertunnel._get_transport().sock.shutdown()
            self.dockertunnel.stop()
        except:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.dockertunnel = None

    def get_docker_port(self) -> Optional[int]:
        """Returns the port where the remote docker socket is exposed on localhost

        Raises:
            exceptions.SSHError -- Error on SSH layer
            exceptions.SSHTunnelError -- Error on SSH tunnel layer

        Returns:
            int -- local port where the docker socket is exposed
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
        """Expose an already connected SSH shell

        Arguments:
            port {int} -- local port where shell should be exposed,
                          if None system will use random port

        Raises:
            exceptions.SSHError -- [description]
            exceptions.SSHTunnelError -- [description]

        Returns:
            int -- [description]
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

    def stop_exposing_ssh(self):
        try:
            if self.sshforwarder is None:
                return

            self.sshforwarder.stop()
        except:
            logging.exception("SSH - Exception closing ssh tunnel")

        self.sshforwarder = None

    def get_ssh_port(self) -> Optional[int]:
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

    def _process_ps_output(self, stream: Iterable[str]) -> List[dict]:
        """Processes output of ps command into a jsonizable dictionary

        Arguments:
            stream {Iterable[str]} -- stream used to parse information

        Returns:
            list -- list of running processes with their properties
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

    def get_process_list(self) -> List[dict]:
        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:
                return self._process_ps_output(ssh.exec_command(PS_CMD_LINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_process_list(self, container_id) -> List[dict]:
        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(PS_CMD_LINE)[1]

            return self._process_ps_output(io.StringIO(plist.decode("utf-8")))

    def _process_free_output(self, stream: Iterable[str]) -> Optional[dict]:
        """Collects relevant information from the output of free command

        Arguments:
            stream {Iterable[str]} -- stdout of free command

        Returns:
            dict -- MemInfo struct (total/free/available kb)
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

    def get_memoryinfo(self) -> Optional[dict]:
        """Retrieves memory information for the device

        Raises:
            exceptions.SSHError -- SHH error

        Returns:
            dict -- MemInfo struct (total/free/available kb)
        """

        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return self._process_free_output(ssh.exec_command(FREE_CMD_LINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_memoryinfo(self, container_id: str) -> Optional[dict]:
        """Retrieves memory information for a specific container

        Arguments:
            container_id {str} -- Container id

        Raises:
            exceptions.SSHError -- SHH error

        Returns:
            dict -- MemInfo struct (total/free/available kb)
        """

        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(FREE_CMD_LINE)[1]

            return self._process_free_output(io.StringIO(plist.decode("utf-8")))

    def _process_df_output(self, stream: Iterable[str]) -> list:
        """Collects relevant information from the output of df command

        Arguments:
            stream {file} -- stdout of df command

        Returns:
            dict -- List of StorageInfo items
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

    def get_storageinfo(self) -> list:
        """Retrieves storage information for the device

        Raises:
            exceptions.SSHError -- SHH error

        Returns:
            list -- List of StorageInfo objects
        """

        try:
            with sharedssh.SharedSSHClient.get_connection(self) as ssh:

                return self._process_df_output(ssh.exec_command(DF_CMDLINE)[1])

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def get_container_storageinfo(self, container_id) -> list:
        """Retrieves storage information for a specific container

        Arguments:
            container_id {str} -- Container id

        Raises:
            exceptions.SSHError -- SHH error

        Returns:
            list -- List of StorageInfo objects
        """

        with remotedocker.RemoteDocker(self) as rd:

            container = rd.get_container(container_id)
            plist = container.exec_run(DF_CMDLINE)[1]

            return self._process_df_output(io.StringIO(plist.decode("utf-8")))

    def sync_folders(self, sourcefolder, destfolder):
        """Syncronizes a local folder and a folder on the target device

        Arguments:
            sourcefolder {str} -- source folder
            destfolder {str} -- destination folder
        """
        rsync.run_rsync(sourcefolder, self.id, destfolder)

    def get_current_ip(self) -> str:
        """Returns the device current ip or the hostname

        Returns:
            str -- device current ip or hostname if ip can't be solved
        """
        ip, mdns = sharedssh.resolve_hostname(self.hostname)

        return ip

    def get_container_logs(self, container_id, restart):
        """Returns container logs

        Arguments:
            container_id {str} -- specific container id
            restart {bool} -- reloads log generator

        Returns:
            line {str} -- log line on None for EOF
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

    def __getstate__(self):
        fields = super().__getstate__()
        del fields["dockertunnel"]
        del fields["sshforwarder"]
        del fields["logs"]
        return fields

    def save(self):

        super().save()


class TargetDevices(Dict[str, TargetDevice], metaclass=singleton.Singleton):
    """ Manages the list of devices

    Works only as a container, Specific properties are accessed
    using the :class:`TargetDevice` class
    """

    def __init__(self):

        # dictionary with supported modules
        self.modeldict = dict.fromkeys(["0014", "0015", "0016", "0017"], "colibri-imx6")
        self.modeldict.update(dict.fromkeys(["0032", "0033", "0039"], "colibri-imx7"))
        self.modeldict.update(
            dict.fromkeys(["0027", "0028", "0029", "0035"], "apalis-imx6")
        )
        self.modeldict.update(dict.fromkeys(["0036"], "colibri-imx6ull"))
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
                self[dev.id] = dev
            except:
                logging.exception("Can't create device from folder %s.", str(dir))

    def __delitem__(self, key):
        if key not in self:
            return

        self[key].destroy()
        dict.__delitem__(self, key)

    def _unlock_ssh(self, console, dev, timeout):
        """Enable ssh connection to the device without having to use a password

        Arguments:
            console {GenericConsole} -- console
            dev {TargetDevice} -- device
            timeout {timeout} -- timeout in seconds
        """
        keysfile = console.send_cmd("ls .ssh/authorized_keys", timeout)

        # file does not exists
        if keysfile != ".ssh/authorized_keys":
            keys = dev.publickey
        else:
            keys = console.send_cmd("cat .ssh/authorized_keys", timeout)

            if dev.publickey not in keys:
                keys += "\n" + dev.publickey

        # regenerates the keys file
        console.send_cmd("mkdir .ssh")
        console.send_cmd('echo "' + keys + '" > .ssh/authorized_keys')
        console.send_cmd("chmod 644 .ssh/authorized_keys")
        console.send_cmd("chmod 700 .ssh")

    def _enable_sudo(self, console, username, password):

        if "sudo enabled" not in console.send_cmd(
            'echo "' + password + '" | sudo -S echo "sudo enabled"'
        ):
            raise exceptions.SudoError(username)

    def _add_debug_warning(self, console, timeout):
        # TODO add a warning to boot scripts
        pass

    def _get_version_info_from_console(self, console, dev, timeout):
        """Collects device version info from a console

        Arguments:
            console {console.GenericConsole} -- console
            dev {TargetDevice} -- device
            timeout {int} -- timeout in seconds
        """
        dev.hwrev = console.send_cmd(
            "cat /proc/device-tree/toradex,board-rev", timeout
        ).rstrip("\x00")

        # Community device
        if "No such file or directory" in dev.hwrev:
            dev.hwrev = "v?.?"

        dev.kernelrelease = console.send_cmd("uname -r", timeout).rstrip("\x00\n")

        dev.kernelversion = console.send_cmd("uname -v", timeout).rstrip("\x00\n")

        dev.torizonversion = (
            console.send_cmd("cat /usr/lib/os-release | grep PRETTY_NAME=", timeout)
            .rstrip("\x00")
            .strip()
        )

        dev.torizonversion = dev.torizonversion.lstrip("PRETTY_NAME=")
        dev.torizonversion = dev.torizonversion.strip('"')

    def _create_device_from_console(self, console, timeout) -> TargetDevice:
        """Create a new device collecting its information from the console

        Arguments:
            console {console.GenericConsole} -- console
            timeout {int} -- Timeout in seconds

        Returns:
            TargetDevice -- [description]

        Raises:
            exceptions.InvalidDeviceIdError: device id is not valid
            exceptions.LoginFailedError: login failed
            exceptions.SSHException: ssh error
            exceptions.SerialException: serial port error
            exceptions.InvalidDeviceError: device data is not valid
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
            dev.community = True

            # Check if the distro have docker
            dockerCheck = console.send_cmd(
                "ls /var/run/docker.sock", timeout
            ).rstrip("\x00")

            if "No such file or directory" in dockerCheck:
                logging.info("Docker socket not present, make sure you have " \
                                + "Docker installed and running on your board.")
                raise exceptions.InvalidDeviceError()

            # Check if the board in running arm or arm64
            archCheck = console.send_cmd(
                "arch", timeout
            ).rstrip("\x00")

            if "arm" not in archCheck:
                logging.info("Unsupported architecture %s", archCheck)
                raise exceptions.InvalidDeviceError()

            # Community Devices has Model name
            dev.model = console.send_cmd(
                "cat /proc/device-tree/model", timeout
            ).rstrip("\x00")

            dev.hostname = console.send_cmd(
                "cat /etc/hostname", timeout
            ).rstrip("\x00")
        else:
            raise exceptions.InvalidDeviceIdError()

        logging.info(
            "DETECT - %s detected :: Model %s",
            dev.hostname,
            dev.model
        )

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

    def _reboot_device(self, console, password):
        """
        Reboots target device at the end of setup process

        Arguments:
            console {Console} -- console
        """

        try:
            console.send_cmd("echo " + password + " | sudo -S reboot", 0)
        except exceptions.TimeoutError:
            pass

    def _enable_docker_interface(self, console, timeout, password):
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

    def _setup_device(self, console, username, password, timeout) -> TargetDevice:

        console.login(username, password, timeout * 2)

        logging.warning("DETECT - Login successful.")

        device = self._create_device_from_console(console, timeout)

        device.username = username

        assert device.id is not None

        # keeps keys
        if device.id in self:
            device.publickey = self[device.id].publickey
            device.privatekey = self[device.id].privatekey

        self._enable_sudo(console, username, password)

        device.save()

        self._unlock_ssh(console, device, timeout)
        self._enable_docker_interface(console, timeout, password)
        self._add_debug_warning(console, timeout)
        self._reboot_device(console, password)
        self[device.id] = device
        return device

    def add_serial_device(self, port, username, password) -> TargetDevice:
        """Initializes a device from serial console

        Arguments:
            port {str} -- serial port name
            username {str} -- username
            password {str} -- password
        """
        timeout = config.ServerConfig().commandtimeout

        logging.info("DETECT - Trying to detect device on port %s.", port)

        with serialconsole.SerialConsole(port) as console:
            return self._setup_device(console, username, password, timeout)

    def add_network_device(self, hostname, username, password) -> TargetDevice:
        """Initializes a device from serial console

        Arguments:
            hostname {str} -- hostname (can be hostname:port)
            username {str} -- username
            password {str} -- password
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

    def refresh_device_info(self, device_id):
        """Reads back version information from a device

        Arguments:
            device_id {str} -- device id (api ensures that is valid)

        Returns:
            TargetDevice -- device with update information or None for failure
        """
        timeout = config.ServerConfig().commandtimeout

        dev = self[device_id]

        with sshconsole.SSHConsole(dev.hostname) as console:
            console.connect(dev.username, dev.privatekey)
            self._get_version_info_from_console(console, dev, timeout)

        dev.save()

    def get_hostname_from_model(self, model: str) -> str:
        """
        return default hostname for specific model

        Arguments:
            model {str} -- model code (ex: "0015")

        Returns:
            str -- standard hostname or None

        Raises:
            exceptions.InvalidModelError
        """

        if model in self.modeldict:
            return self.modeldict[model]
        raise exceptions.InvalidModelError(model)
