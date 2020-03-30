# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerContainerConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'hostname': 'str',
        'domainname': 'str',
        'user': 'str',
        'attach_stdin': 'bool',
        'attach_stdout': 'bool',
        'attach_stderr': 'bool',
        'exposed_ports': 'dict(str, object)',
        'tty': 'bool',
        'open_stdin': 'bool',
        'stdin_once': 'bool',
        'env': 'list[str]',
        'cmd': 'list[str]',
        'healthcheck': 'DockerHealthConfig',
        'args_escaped': 'bool',
        'image': 'str',
        'volumes': 'dict(str, object)',
        'working_dir': 'str',
        'entrypoint': 'list[str]',
        'network_disabled': 'bool',
        'mac_address': 'str',
        'on_build': 'list[str]',
        'labels': 'dict(str, str)',
        'stop_signal': 'str',
        'stop_timeout': 'int',
        'shell': 'list[str]'
    }

    attribute_map = {
        'hostname': 'Hostname',
        'domainname': 'Domainname',
        'user': 'User',
        'attach_stdin': 'AttachStdin',
        'attach_stdout': 'AttachStdout',
        'attach_stderr': 'AttachStderr',
        'exposed_ports': 'ExposedPorts',
        'tty': 'Tty',
        'open_stdin': 'OpenStdin',
        'stdin_once': 'StdinOnce',
        'env': 'Env',
        'cmd': 'Cmd',
        'healthcheck': 'Healthcheck',
        'args_escaped': 'ArgsEscaped',
        'image': 'Image',
        'volumes': 'Volumes',
        'working_dir': 'WorkingDir',
        'entrypoint': 'Entrypoint',
        'network_disabled': 'NetworkDisabled',
        'mac_address': 'MacAddress',
        'on_build': 'OnBuild',
        'labels': 'Labels',
        'stop_signal': 'StopSignal',
        'stop_timeout': 'StopTimeout',
        'shell': 'Shell'
    }

    def __init__(self, hostname=None, domainname=None, user=None, attach_stdin=False, attach_stdout=True, attach_stderr=True, exposed_ports=None, tty=False, open_stdin=False, stdin_once=False, env=None, cmd=None, healthcheck=None, args_escaped=None, image=None, volumes=None, working_dir=None, entrypoint=None, network_disabled=None, mac_address=None, on_build=None, labels=None, stop_signal='SIGTERM', stop_timeout=None, shell=None, local_vars_configuration=None):  # noqa: E501
        """DockerContainerConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._domainname = None
        self._user = None
        self._attach_stdin = None
        self._attach_stdout = None
        self._attach_stderr = None
        self._exposed_ports = None
        self._tty = None
        self._open_stdin = None
        self._stdin_once = None
        self._env = None
        self._cmd = None
        self._healthcheck = None
        self._args_escaped = None
        self._image = None
        self._volumes = None
        self._working_dir = None
        self._entrypoint = None
        self._network_disabled = None
        self._mac_address = None
        self._on_build = None
        self._labels = None
        self._stop_signal = None
        self._stop_timeout = None
        self._shell = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if domainname is not None:
            self.domainname = domainname
        if user is not None:
            self.user = user
        if attach_stdin is not None:
            self.attach_stdin = attach_stdin
        if attach_stdout is not None:
            self.attach_stdout = attach_stdout
        if attach_stderr is not None:
            self.attach_stderr = attach_stderr
        if exposed_ports is not None:
            self.exposed_ports = exposed_ports
        if tty is not None:
            self.tty = tty
        if open_stdin is not None:
            self.open_stdin = open_stdin
        if stdin_once is not None:
            self.stdin_once = stdin_once
        if env is not None:
            self.env = env
        if cmd is not None:
            self.cmd = cmd
        if healthcheck is not None:
            self.healthcheck = healthcheck
        if args_escaped is not None:
            self.args_escaped = args_escaped
        if image is not None:
            self.image = image
        if volumes is not None:
            self.volumes = volumes
        if working_dir is not None:
            self.working_dir = working_dir
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if network_disabled is not None:
            self.network_disabled = network_disabled
        if mac_address is not None:
            self.mac_address = mac_address
        if on_build is not None:
            self.on_build = on_build
        if labels is not None:
            self.labels = labels
        if stop_signal is not None:
            self.stop_signal = stop_signal
        if stop_timeout is not None:
            self.stop_timeout = stop_timeout
        if shell is not None:
            self.shell = shell

    @property
    def hostname(self):
        """Gets the hostname of this DockerContainerConfig.  # noqa: E501

        The hostname to use for the container, as a valid RFC 1123 hostname.  # noqa: E501

        :return: The hostname of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DockerContainerConfig.

        The hostname to use for the container, as a valid RFC 1123 hostname.  # noqa: E501

        :param hostname: The hostname of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def domainname(self):
        """Gets the domainname of this DockerContainerConfig.  # noqa: E501

        The domain name to use for the container.  # noqa: E501

        :return: The domainname of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._domainname

    @domainname.setter
    def domainname(self, domainname):
        """Sets the domainname of this DockerContainerConfig.

        The domain name to use for the container.  # noqa: E501

        :param domainname: The domainname of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._domainname = domainname

    @property
    def user(self):
        """Gets the user of this DockerContainerConfig.  # noqa: E501

        The user that commands are run as inside the container.  # noqa: E501

        :return: The user of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DockerContainerConfig.

        The user that commands are run as inside the container.  # noqa: E501

        :param user: The user of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def attach_stdin(self):
        """Gets the attach_stdin of this DockerContainerConfig.  # noqa: E501

        Whether to attach to `stdin`.  # noqa: E501

        :return: The attach_stdin of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._attach_stdin

    @attach_stdin.setter
    def attach_stdin(self, attach_stdin):
        """Sets the attach_stdin of this DockerContainerConfig.

        Whether to attach to `stdin`.  # noqa: E501

        :param attach_stdin: The attach_stdin of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._attach_stdin = attach_stdin

    @property
    def attach_stdout(self):
        """Gets the attach_stdout of this DockerContainerConfig.  # noqa: E501

        Whether to attach to `stdout`.  # noqa: E501

        :return: The attach_stdout of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._attach_stdout

    @attach_stdout.setter
    def attach_stdout(self, attach_stdout):
        """Sets the attach_stdout of this DockerContainerConfig.

        Whether to attach to `stdout`.  # noqa: E501

        :param attach_stdout: The attach_stdout of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._attach_stdout = attach_stdout

    @property
    def attach_stderr(self):
        """Gets the attach_stderr of this DockerContainerConfig.  # noqa: E501

        Whether to attach to `stderr`.  # noqa: E501

        :return: The attach_stderr of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._attach_stderr

    @attach_stderr.setter
    def attach_stderr(self, attach_stderr):
        """Sets the attach_stderr of this DockerContainerConfig.

        Whether to attach to `stderr`.  # noqa: E501

        :param attach_stderr: The attach_stderr of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._attach_stderr = attach_stderr

    @property
    def exposed_ports(self):
        """Gets the exposed_ports of this DockerContainerConfig.  # noqa: E501

        An object mapping ports to an empty object in the form:  `{\"<port>/<tcp|udp|sctp>\": {}}`   # noqa: E501

        :return: The exposed_ports of this DockerContainerConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._exposed_ports

    @exposed_ports.setter
    def exposed_ports(self, exposed_ports):
        """Sets the exposed_ports of this DockerContainerConfig.

        An object mapping ports to an empty object in the form:  `{\"<port>/<tcp|udp|sctp>\": {}}`   # noqa: E501

        :param exposed_ports: The exposed_ports of this DockerContainerConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._exposed_ports = exposed_ports

    @property
    def tty(self):
        """Gets the tty of this DockerContainerConfig.  # noqa: E501

        Attach standard streams to a TTY, including `stdin` if it is not closed.  # noqa: E501

        :return: The tty of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """Sets the tty of this DockerContainerConfig.

        Attach standard streams to a TTY, including `stdin` if it is not closed.  # noqa: E501

        :param tty: The tty of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._tty = tty

    @property
    def open_stdin(self):
        """Gets the open_stdin of this DockerContainerConfig.  # noqa: E501

        Open `stdin`  # noqa: E501

        :return: The open_stdin of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._open_stdin

    @open_stdin.setter
    def open_stdin(self, open_stdin):
        """Sets the open_stdin of this DockerContainerConfig.

        Open `stdin`  # noqa: E501

        :param open_stdin: The open_stdin of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._open_stdin = open_stdin

    @property
    def stdin_once(self):
        """Gets the stdin_once of this DockerContainerConfig.  # noqa: E501

        Close `stdin` after one attached client disconnects  # noqa: E501

        :return: The stdin_once of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._stdin_once

    @stdin_once.setter
    def stdin_once(self, stdin_once):
        """Sets the stdin_once of this DockerContainerConfig.

        Close `stdin` after one attached client disconnects  # noqa: E501

        :param stdin_once: The stdin_once of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._stdin_once = stdin_once

    @property
    def env(self):
        """Gets the env of this DockerContainerConfig.  # noqa: E501

        A list of environment variables to set inside the container in the form `[\"VAR=value\", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value.   # noqa: E501

        :return: The env of this DockerContainerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this DockerContainerConfig.

        A list of environment variables to set inside the container in the form `[\"VAR=value\", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value.   # noqa: E501

        :param env: The env of this DockerContainerConfig.  # noqa: E501
        :type: list[str]
        """

        self._env = env

    @property
    def cmd(self):
        """Gets the cmd of this DockerContainerConfig.  # noqa: E501

        Command to run specified as a string or an array of strings.  # noqa: E501

        :return: The cmd of this DockerContainerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this DockerContainerConfig.

        Command to run specified as a string or an array of strings.  # noqa: E501

        :param cmd: The cmd of this DockerContainerConfig.  # noqa: E501
        :type: list[str]
        """

        self._cmd = cmd

    @property
    def healthcheck(self):
        """Gets the healthcheck of this DockerContainerConfig.  # noqa: E501


        :return: The healthcheck of this DockerContainerConfig.  # noqa: E501
        :rtype: DockerHealthConfig
        """
        return self._healthcheck

    @healthcheck.setter
    def healthcheck(self, healthcheck):
        """Sets the healthcheck of this DockerContainerConfig.


        :param healthcheck: The healthcheck of this DockerContainerConfig.  # noqa: E501
        :type: DockerHealthConfig
        """

        self._healthcheck = healthcheck

    @property
    def args_escaped(self):
        """Gets the args_escaped of this DockerContainerConfig.  # noqa: E501

        Command is already escaped (Windows only)  # noqa: E501

        :return: The args_escaped of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._args_escaped

    @args_escaped.setter
    def args_escaped(self, args_escaped):
        """Sets the args_escaped of this DockerContainerConfig.

        Command is already escaped (Windows only)  # noqa: E501

        :param args_escaped: The args_escaped of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._args_escaped = args_escaped

    @property
    def image(self):
        """Gets the image of this DockerContainerConfig.  # noqa: E501

        The name of the image to use when creating the container  # noqa: E501

        :return: The image of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DockerContainerConfig.

        The name of the image to use when creating the container  # noqa: E501

        :param image: The image of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def volumes(self):
        """Gets the volumes of this DockerContainerConfig.  # noqa: E501

        An object mapping mount point paths inside the container to empty objects.  # noqa: E501

        :return: The volumes of this DockerContainerConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this DockerContainerConfig.

        An object mapping mount point paths inside the container to empty objects.  # noqa: E501

        :param volumes: The volumes of this DockerContainerConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._volumes = volumes

    @property
    def working_dir(self):
        """Gets the working_dir of this DockerContainerConfig.  # noqa: E501

        The working directory for commands to run in.  # noqa: E501

        :return: The working_dir of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this DockerContainerConfig.

        The working directory for commands to run in.  # noqa: E501

        :param working_dir: The working_dir of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

    @property
    def entrypoint(self):
        """Gets the entrypoint of this DockerContainerConfig.  # noqa: E501

        The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (`[\"\"]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`).   # noqa: E501

        :return: The entrypoint of this DockerContainerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this DockerContainerConfig.

        The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (`[\"\"]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`).   # noqa: E501

        :param entrypoint: The entrypoint of this DockerContainerConfig.  # noqa: E501
        :type: list[str]
        """

        self._entrypoint = entrypoint

    @property
    def network_disabled(self):
        """Gets the network_disabled of this DockerContainerConfig.  # noqa: E501

        Disable networking for the container.  # noqa: E501

        :return: The network_disabled of this DockerContainerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._network_disabled

    @network_disabled.setter
    def network_disabled(self, network_disabled):
        """Sets the network_disabled of this DockerContainerConfig.

        Disable networking for the container.  # noqa: E501

        :param network_disabled: The network_disabled of this DockerContainerConfig.  # noqa: E501
        :type: bool
        """

        self._network_disabled = network_disabled

    @property
    def mac_address(self):
        """Gets the mac_address of this DockerContainerConfig.  # noqa: E501

        MAC address of the container.  # noqa: E501

        :return: The mac_address of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DockerContainerConfig.

        MAC address of the container.  # noqa: E501

        :param mac_address: The mac_address of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def on_build(self):
        """Gets the on_build of this DockerContainerConfig.  # noqa: E501

        `ONBUILD` metadata that were defined in the image's `Dockerfile`.  # noqa: E501

        :return: The on_build of this DockerContainerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._on_build

    @on_build.setter
    def on_build(self, on_build):
        """Sets the on_build of this DockerContainerConfig.

        `ONBUILD` metadata that were defined in the image's `Dockerfile`.  # noqa: E501

        :param on_build: The on_build of this DockerContainerConfig.  # noqa: E501
        :type: list[str]
        """

        self._on_build = on_build

    @property
    def labels(self):
        """Gets the labels of this DockerContainerConfig.  # noqa: E501

        User-defined key/value metadata.  # noqa: E501

        :return: The labels of this DockerContainerConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DockerContainerConfig.

        User-defined key/value metadata.  # noqa: E501

        :param labels: The labels of this DockerContainerConfig.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def stop_signal(self):
        """Gets the stop_signal of this DockerContainerConfig.  # noqa: E501

        Signal to stop a container as a string or unsigned integer.  # noqa: E501

        :return: The stop_signal of this DockerContainerConfig.  # noqa: E501
        :rtype: str
        """
        return self._stop_signal

    @stop_signal.setter
    def stop_signal(self, stop_signal):
        """Sets the stop_signal of this DockerContainerConfig.

        Signal to stop a container as a string or unsigned integer.  # noqa: E501

        :param stop_signal: The stop_signal of this DockerContainerConfig.  # noqa: E501
        :type: str
        """

        self._stop_signal = stop_signal

    @property
    def stop_timeout(self):
        """Gets the stop_timeout of this DockerContainerConfig.  # noqa: E501

        Timeout to stop a container in seconds.  # noqa: E501

        :return: The stop_timeout of this DockerContainerConfig.  # noqa: E501
        :rtype: int
        """
        return self._stop_timeout

    @stop_timeout.setter
    def stop_timeout(self, stop_timeout):
        """Sets the stop_timeout of this DockerContainerConfig.

        Timeout to stop a container in seconds.  # noqa: E501

        :param stop_timeout: The stop_timeout of this DockerContainerConfig.  # noqa: E501
        :type: int
        """

        self._stop_timeout = stop_timeout

    @property
    def shell(self):
        """Gets the shell of this DockerContainerConfig.  # noqa: E501

        Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell.  # noqa: E501

        :return: The shell of this DockerContainerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this DockerContainerConfig.

        Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell.  # noqa: E501

        :param shell: The shell of this DockerContainerConfig.  # noqa: E501
        :type: list[str]
        """

        self._shell = shell

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerContainerConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerContainerConfig):
            return True

        return self.to_dict() != other.to_dict()
