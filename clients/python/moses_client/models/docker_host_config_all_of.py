# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerHostConfigAllOf(object):
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
        'binds': 'list[str]',
        'container_id_file': 'str',
        'log_config': 'DockerHostConfigAllOfLogConfig',
        'network_mode': 'str',
        'port_bindings': 'dict(str, list[DockerPortBinding])',
        'restart_policy': 'DockerRestartPolicy',
        'auto_remove': 'bool',
        'volume_driver': 'str',
        'volumes_from': 'list[str]',
        'mounts': 'list[DockerMount]',
        'cap_add': 'list[str]',
        'cap_drop': 'list[str]',
        'dns': 'list[str]',
        'dns_options': 'list[str]',
        'dns_search': 'list[str]',
        'extra_hosts': 'list[str]',
        'group_add': 'list[str]',
        'ipc_mode': 'str',
        'cgroup': 'str',
        'links': 'list[str]',
        'oom_score_adj': 'int',
        'pid_mode': 'str',
        'privileged': 'bool',
        'publish_all_ports': 'bool',
        'readonly_rootfs': 'bool',
        'security_opt': 'list[str]',
        'storage_opt': 'dict(str, str)',
        'tmpfs': 'dict(str, str)',
        'uts_mode': 'str',
        'userns_mode': 'str',
        'shm_size': 'int',
        'sysctls': 'dict(str, str)',
        'runtime': 'str'
    }

    attribute_map = {
        'binds': 'Binds',
        'container_id_file': 'ContainerIDFile',
        'log_config': 'LogConfig',
        'network_mode': 'NetworkMode',
        'port_bindings': 'PortBindings',
        'restart_policy': 'RestartPolicy',
        'auto_remove': 'AutoRemove',
        'volume_driver': 'VolumeDriver',
        'volumes_from': 'VolumesFrom',
        'mounts': 'Mounts',
        'cap_add': 'CapAdd',
        'cap_drop': 'CapDrop',
        'dns': 'Dns',
        'dns_options': 'DnsOptions',
        'dns_search': 'DnsSearch',
        'extra_hosts': 'ExtraHosts',
        'group_add': 'GroupAdd',
        'ipc_mode': 'IpcMode',
        'cgroup': 'Cgroup',
        'links': 'Links',
        'oom_score_adj': 'OomScoreAdj',
        'pid_mode': 'PidMode',
        'privileged': 'Privileged',
        'publish_all_ports': 'PublishAllPorts',
        'readonly_rootfs': 'ReadonlyRootfs',
        'security_opt': 'SecurityOpt',
        'storage_opt': 'StorageOpt',
        'tmpfs': 'Tmpfs',
        'uts_mode': 'UTSMode',
        'userns_mode': 'UsernsMode',
        'shm_size': 'ShmSize',
        'sysctls': 'Sysctls',
        'runtime': 'Runtime'
    }

    def __init__(self, binds=None, container_id_file=None, log_config=None, network_mode=None, port_bindings=None, restart_policy=None, auto_remove=None, volume_driver=None, volumes_from=None, mounts=None, cap_add=None, cap_drop=None, dns=None, dns_options=None, dns_search=None, extra_hosts=None, group_add=None, ipc_mode=None, cgroup=None, links=None, oom_score_adj=None, pid_mode=None, privileged=None, publish_all_ports=None, readonly_rootfs=None, security_opt=None, storage_opt=None, tmpfs=None, uts_mode=None, userns_mode=None, shm_size=None, sysctls=None, runtime=None, local_vars_configuration=None):  # noqa: E501
        """DockerHostConfigAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._binds = None
        self._container_id_file = None
        self._log_config = None
        self._network_mode = None
        self._port_bindings = None
        self._restart_policy = None
        self._auto_remove = None
        self._volume_driver = None
        self._volumes_from = None
        self._mounts = None
        self._cap_add = None
        self._cap_drop = None
        self._dns = None
        self._dns_options = None
        self._dns_search = None
        self._extra_hosts = None
        self._group_add = None
        self._ipc_mode = None
        self._cgroup = None
        self._links = None
        self._oom_score_adj = None
        self._pid_mode = None
        self._privileged = None
        self._publish_all_ports = None
        self._readonly_rootfs = None
        self._security_opt = None
        self._storage_opt = None
        self._tmpfs = None
        self._uts_mode = None
        self._userns_mode = None
        self._shm_size = None
        self._sysctls = None
        self._runtime = None
        self.discriminator = None

        if binds is not None:
            self.binds = binds
        if container_id_file is not None:
            self.container_id_file = container_id_file
        if log_config is not None:
            self.log_config = log_config
        if network_mode is not None:
            self.network_mode = network_mode
        if port_bindings is not None:
            self.port_bindings = port_bindings
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if auto_remove is not None:
            self.auto_remove = auto_remove
        if volume_driver is not None:
            self.volume_driver = volume_driver
        if volumes_from is not None:
            self.volumes_from = volumes_from
        if mounts is not None:
            self.mounts = mounts
        if cap_add is not None:
            self.cap_add = cap_add
        if cap_drop is not None:
            self.cap_drop = cap_drop
        if dns is not None:
            self.dns = dns
        if dns_options is not None:
            self.dns_options = dns_options
        if dns_search is not None:
            self.dns_search = dns_search
        if extra_hosts is not None:
            self.extra_hosts = extra_hosts
        if group_add is not None:
            self.group_add = group_add
        if ipc_mode is not None:
            self.ipc_mode = ipc_mode
        if cgroup is not None:
            self.cgroup = cgroup
        if links is not None:
            self.links = links
        if oom_score_adj is not None:
            self.oom_score_adj = oom_score_adj
        if pid_mode is not None:
            self.pid_mode = pid_mode
        if privileged is not None:
            self.privileged = privileged
        if publish_all_ports is not None:
            self.publish_all_ports = publish_all_ports
        if readonly_rootfs is not None:
            self.readonly_rootfs = readonly_rootfs
        if security_opt is not None:
            self.security_opt = security_opt
        if storage_opt is not None:
            self.storage_opt = storage_opt
        if tmpfs is not None:
            self.tmpfs = tmpfs
        if uts_mode is not None:
            self.uts_mode = uts_mode
        if userns_mode is not None:
            self.userns_mode = userns_mode
        if shm_size is not None:
            self.shm_size = shm_size
        if sysctls is not None:
            self.sysctls = sysctls
        if runtime is not None:
            self.runtime = runtime

    @property
    def binds(self):
        """Gets the binds of this DockerHostConfigAllOf.  # noqa: E501

        A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - `host-src:container-dest` to bind-mount a host path into the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `host-src:container-dest:ro` to make the bind mount read-only inside the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `volume-name:container-dest` to bind-mount a volume managed by a volume driver into the container. `container-dest` must be an _absolute_ path. - `volume-name:container-dest:ro` to mount the volume read-only inside the container.  `container-dest` must be an _absolute_ path.   # noqa: E501

        :return: The binds of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._binds

    @binds.setter
    def binds(self, binds):
        """Sets the binds of this DockerHostConfigAllOf.

        A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - `host-src:container-dest` to bind-mount a host path into the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `host-src:container-dest:ro` to make the bind mount read-only inside the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `volume-name:container-dest` to bind-mount a volume managed by a volume driver into the container. `container-dest` must be an _absolute_ path. - `volume-name:container-dest:ro` to mount the volume read-only inside the container.  `container-dest` must be an _absolute_ path.   # noqa: E501

        :param binds: The binds of this DockerHostConfigAllOf.  # noqa: E501
        :type binds: list[str]
        """

        self._binds = binds

    @property
    def container_id_file(self):
        """Gets the container_id_file of this DockerHostConfigAllOf.  # noqa: E501

        Path to a file where the container ID is written  # noqa: E501

        :return: The container_id_file of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._container_id_file

    @container_id_file.setter
    def container_id_file(self, container_id_file):
        """Sets the container_id_file of this DockerHostConfigAllOf.

        Path to a file where the container ID is written  # noqa: E501

        :param container_id_file: The container_id_file of this DockerHostConfigAllOf.  # noqa: E501
        :type container_id_file: str
        """

        self._container_id_file = container_id_file

    @property
    def log_config(self):
        """Gets the log_config of this DockerHostConfigAllOf.  # noqa: E501


        :return: The log_config of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: DockerHostConfigAllOfLogConfig
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        """Sets the log_config of this DockerHostConfigAllOf.


        :param log_config: The log_config of this DockerHostConfigAllOf.  # noqa: E501
        :type log_config: DockerHostConfigAllOfLogConfig
        """

        self._log_config = log_config

    @property
    def network_mode(self):
        """Gets the network_mode of this DockerHostConfigAllOf.  # noqa: E501

        Network mode to use for this container. Supported standard values are: `bridge`, `host`, `none`, and `container:<name|id>`. Any other value is taken as a custom network's name to which this container should connect to.  # noqa: E501

        :return: The network_mode of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        """Sets the network_mode of this DockerHostConfigAllOf.

        Network mode to use for this container. Supported standard values are: `bridge`, `host`, `none`, and `container:<name|id>`. Any other value is taken as a custom network's name to which this container should connect to.  # noqa: E501

        :param network_mode: The network_mode of this DockerHostConfigAllOf.  # noqa: E501
        :type network_mode: str
        """

        self._network_mode = network_mode

    @property
    def port_bindings(self):
        """Gets the port_bindings of this DockerHostConfigAllOf.  # noqa: E501

        PortMap describes the mapping of container ports to host ports, using the container's port-number and protocol as key in the format `<port>/<protocol>`, for example, `80/udp`.  If a container's port is mapped for multiple protocols, separate entries are added to the mapping table.   # noqa: E501

        :return: The port_bindings of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: dict(str, list[DockerPortBinding])
        """
        return self._port_bindings

    @port_bindings.setter
    def port_bindings(self, port_bindings):
        """Sets the port_bindings of this DockerHostConfigAllOf.

        PortMap describes the mapping of container ports to host ports, using the container's port-number and protocol as key in the format `<port>/<protocol>`, for example, `80/udp`.  If a container's port is mapped for multiple protocols, separate entries are added to the mapping table.   # noqa: E501

        :param port_bindings: The port_bindings of this DockerHostConfigAllOf.  # noqa: E501
        :type port_bindings: dict(str, list[DockerPortBinding])
        """

        self._port_bindings = port_bindings

    @property
    def restart_policy(self):
        """Gets the restart_policy of this DockerHostConfigAllOf.  # noqa: E501


        :return: The restart_policy of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: DockerRestartPolicy
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this DockerHostConfigAllOf.


        :param restart_policy: The restart_policy of this DockerHostConfigAllOf.  # noqa: E501
        :type restart_policy: DockerRestartPolicy
        """

        self._restart_policy = restart_policy

    @property
    def auto_remove(self):
        """Gets the auto_remove of this DockerHostConfigAllOf.  # noqa: E501

        Automatically remove the container when the container's process exits. This has no effect if `RestartPolicy` is set.  # noqa: E501

        :return: The auto_remove of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._auto_remove

    @auto_remove.setter
    def auto_remove(self, auto_remove):
        """Sets the auto_remove of this DockerHostConfigAllOf.

        Automatically remove the container when the container's process exits. This has no effect if `RestartPolicy` is set.  # noqa: E501

        :param auto_remove: The auto_remove of this DockerHostConfigAllOf.  # noqa: E501
        :type auto_remove: bool
        """

        self._auto_remove = auto_remove

    @property
    def volume_driver(self):
        """Gets the volume_driver of this DockerHostConfigAllOf.  # noqa: E501

        Driver that this container uses to mount volumes.  # noqa: E501

        :return: The volume_driver of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._volume_driver

    @volume_driver.setter
    def volume_driver(self, volume_driver):
        """Sets the volume_driver of this DockerHostConfigAllOf.

        Driver that this container uses to mount volumes.  # noqa: E501

        :param volume_driver: The volume_driver of this DockerHostConfigAllOf.  # noqa: E501
        :type volume_driver: str
        """

        self._volume_driver = volume_driver

    @property
    def volumes_from(self):
        """Gets the volumes_from of this DockerHostConfigAllOf.  # noqa: E501

        A list of volumes to inherit from another container, specified in the form `<container name>[:<ro|rw>]`.  # noqa: E501

        :return: The volumes_from of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._volumes_from

    @volumes_from.setter
    def volumes_from(self, volumes_from):
        """Sets the volumes_from of this DockerHostConfigAllOf.

        A list of volumes to inherit from another container, specified in the form `<container name>[:<ro|rw>]`.  # noqa: E501

        :param volumes_from: The volumes_from of this DockerHostConfigAllOf.  # noqa: E501
        :type volumes_from: list[str]
        """

        self._volumes_from = volumes_from

    @property
    def mounts(self):
        """Gets the mounts of this DockerHostConfigAllOf.  # noqa: E501

        Specification for mounts to be added to the container.  # noqa: E501

        :return: The mounts of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[DockerMount]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this DockerHostConfigAllOf.

        Specification for mounts to be added to the container.  # noqa: E501

        :param mounts: The mounts of this DockerHostConfigAllOf.  # noqa: E501
        :type mounts: list[DockerMount]
        """

        self._mounts = mounts

    @property
    def cap_add(self):
        """Gets the cap_add of this DockerHostConfigAllOf.  # noqa: E501

        A list of kernel capabilities to add to the container.  # noqa: E501

        :return: The cap_add of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._cap_add

    @cap_add.setter
    def cap_add(self, cap_add):
        """Sets the cap_add of this DockerHostConfigAllOf.

        A list of kernel capabilities to add to the container.  # noqa: E501

        :param cap_add: The cap_add of this DockerHostConfigAllOf.  # noqa: E501
        :type cap_add: list[str]
        """

        self._cap_add = cap_add

    @property
    def cap_drop(self):
        """Gets the cap_drop of this DockerHostConfigAllOf.  # noqa: E501

        A list of kernel capabilities to drop from the container.  # noqa: E501

        :return: The cap_drop of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._cap_drop

    @cap_drop.setter
    def cap_drop(self, cap_drop):
        """Sets the cap_drop of this DockerHostConfigAllOf.

        A list of kernel capabilities to drop from the container.  # noqa: E501

        :param cap_drop: The cap_drop of this DockerHostConfigAllOf.  # noqa: E501
        :type cap_drop: list[str]
        """

        self._cap_drop = cap_drop

    @property
    def dns(self):
        """Gets the dns of this DockerHostConfigAllOf.  # noqa: E501

        A list of DNS servers for the container to use.  # noqa: E501

        :return: The dns of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this DockerHostConfigAllOf.

        A list of DNS servers for the container to use.  # noqa: E501

        :param dns: The dns of this DockerHostConfigAllOf.  # noqa: E501
        :type dns: list[str]
        """

        self._dns = dns

    @property
    def dns_options(self):
        """Gets the dns_options of this DockerHostConfigAllOf.  # noqa: E501

        A list of DNS options.  # noqa: E501

        :return: The dns_options of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_options

    @dns_options.setter
    def dns_options(self, dns_options):
        """Sets the dns_options of this DockerHostConfigAllOf.

        A list of DNS options.  # noqa: E501

        :param dns_options: The dns_options of this DockerHostConfigAllOf.  # noqa: E501
        :type dns_options: list[str]
        """

        self._dns_options = dns_options

    @property
    def dns_search(self):
        """Gets the dns_search of this DockerHostConfigAllOf.  # noqa: E501

        A list of DNS search domains.  # noqa: E501

        :return: The dns_search of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_search

    @dns_search.setter
    def dns_search(self, dns_search):
        """Sets the dns_search of this DockerHostConfigAllOf.

        A list of DNS search domains.  # noqa: E501

        :param dns_search: The dns_search of this DockerHostConfigAllOf.  # noqa: E501
        :type dns_search: list[str]
        """

        self._dns_search = dns_search

    @property
    def extra_hosts(self):
        """Gets the extra_hosts of this DockerHostConfigAllOf.  # noqa: E501

        A list of hostnames/IP mappings to add to the container's `/etc/hosts` file. Specified in the form `[\"hostname:IP\"]`.   # noqa: E501

        :return: The extra_hosts of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._extra_hosts

    @extra_hosts.setter
    def extra_hosts(self, extra_hosts):
        """Sets the extra_hosts of this DockerHostConfigAllOf.

        A list of hostnames/IP mappings to add to the container's `/etc/hosts` file. Specified in the form `[\"hostname:IP\"]`.   # noqa: E501

        :param extra_hosts: The extra_hosts of this DockerHostConfigAllOf.  # noqa: E501
        :type extra_hosts: list[str]
        """

        self._extra_hosts = extra_hosts

    @property
    def group_add(self):
        """Gets the group_add of this DockerHostConfigAllOf.  # noqa: E501

        A list of additional groups that the container process will run as.  # noqa: E501

        :return: The group_add of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_add

    @group_add.setter
    def group_add(self, group_add):
        """Sets the group_add of this DockerHostConfigAllOf.

        A list of additional groups that the container process will run as.  # noqa: E501

        :param group_add: The group_add of this DockerHostConfigAllOf.  # noqa: E501
        :type group_add: list[str]
        """

        self._group_add = group_add

    @property
    def ipc_mode(self):
        """Gets the ipc_mode of this DockerHostConfigAllOf.  # noqa: E501

        IPC sharing mode for the container. Possible values are:  - `\"none\"`: own private IPC namespace, with /dev/shm not mounted - `\"private\"`: own private IPC namespace - `\"shareable\"`: own private IPC namespace, with a possibility to share it with other containers - `\"container:<name|id>\"`: join another (shareable) container's IPC namespace - `\"host\"`: use the host system's IPC namespace  If not specified, daemon default is used, which can either be `\"private\"` or `\"shareable\"`, depending on daemon version and configuration.   # noqa: E501

        :return: The ipc_mode of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipc_mode

    @ipc_mode.setter
    def ipc_mode(self, ipc_mode):
        """Sets the ipc_mode of this DockerHostConfigAllOf.

        IPC sharing mode for the container. Possible values are:  - `\"none\"`: own private IPC namespace, with /dev/shm not mounted - `\"private\"`: own private IPC namespace - `\"shareable\"`: own private IPC namespace, with a possibility to share it with other containers - `\"container:<name|id>\"`: join another (shareable) container's IPC namespace - `\"host\"`: use the host system's IPC namespace  If not specified, daemon default is used, which can either be `\"private\"` or `\"shareable\"`, depending on daemon version and configuration.   # noqa: E501

        :param ipc_mode: The ipc_mode of this DockerHostConfigAllOf.  # noqa: E501
        :type ipc_mode: str
        """

        self._ipc_mode = ipc_mode

    @property
    def cgroup(self):
        """Gets the cgroup of this DockerHostConfigAllOf.  # noqa: E501

        Cgroup to use for the container.  # noqa: E501

        :return: The cgroup of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cgroup

    @cgroup.setter
    def cgroup(self, cgroup):
        """Sets the cgroup of this DockerHostConfigAllOf.

        Cgroup to use for the container.  # noqa: E501

        :param cgroup: The cgroup of this DockerHostConfigAllOf.  # noqa: E501
        :type cgroup: str
        """

        self._cgroup = cgroup

    @property
    def links(self):
        """Gets the links of this DockerHostConfigAllOf.  # noqa: E501

        A list of links for the container in the form `container_name:alias`.  # noqa: E501

        :return: The links of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DockerHostConfigAllOf.

        A list of links for the container in the form `container_name:alias`.  # noqa: E501

        :param links: The links of this DockerHostConfigAllOf.  # noqa: E501
        :type links: list[str]
        """

        self._links = links

    @property
    def oom_score_adj(self):
        """Gets the oom_score_adj of this DockerHostConfigAllOf.  # noqa: E501

        An integer value containing the score given to the container in order to tune OOM killer preferences.  # noqa: E501

        :return: The oom_score_adj of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: int
        """
        return self._oom_score_adj

    @oom_score_adj.setter
    def oom_score_adj(self, oom_score_adj):
        """Sets the oom_score_adj of this DockerHostConfigAllOf.

        An integer value containing the score given to the container in order to tune OOM killer preferences.  # noqa: E501

        :param oom_score_adj: The oom_score_adj of this DockerHostConfigAllOf.  # noqa: E501
        :type oom_score_adj: int
        """

        self._oom_score_adj = oom_score_adj

    @property
    def pid_mode(self):
        """Gets the pid_mode of this DockerHostConfigAllOf.  # noqa: E501

        Set the PID (Process) Namespace mode for the container. It can be either:  - `\"container:<name|id>\"`: joins another container's PID namespace - `\"host\"`: use the host's PID namespace inside the container   # noqa: E501

        :return: The pid_mode of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pid_mode

    @pid_mode.setter
    def pid_mode(self, pid_mode):
        """Sets the pid_mode of this DockerHostConfigAllOf.

        Set the PID (Process) Namespace mode for the container. It can be either:  - `\"container:<name|id>\"`: joins another container's PID namespace - `\"host\"`: use the host's PID namespace inside the container   # noqa: E501

        :param pid_mode: The pid_mode of this DockerHostConfigAllOf.  # noqa: E501
        :type pid_mode: str
        """

        self._pid_mode = pid_mode

    @property
    def privileged(self):
        """Gets the privileged of this DockerHostConfigAllOf.  # noqa: E501

        Gives the container full access to the host.  # noqa: E501

        :return: The privileged of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this DockerHostConfigAllOf.

        Gives the container full access to the host.  # noqa: E501

        :param privileged: The privileged of this DockerHostConfigAllOf.  # noqa: E501
        :type privileged: bool
        """

        self._privileged = privileged

    @property
    def publish_all_ports(self):
        """Gets the publish_all_ports of this DockerHostConfigAllOf.  # noqa: E501

        Allocates an ephemeral host port for all of a container's exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by `/proc/sys/net/ipv4/ip_local_port_range`.   # noqa: E501

        :return: The publish_all_ports of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._publish_all_ports

    @publish_all_ports.setter
    def publish_all_ports(self, publish_all_ports):
        """Sets the publish_all_ports of this DockerHostConfigAllOf.

        Allocates an ephemeral host port for all of a container's exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by `/proc/sys/net/ipv4/ip_local_port_range`.   # noqa: E501

        :param publish_all_ports: The publish_all_ports of this DockerHostConfigAllOf.  # noqa: E501
        :type publish_all_ports: bool
        """

        self._publish_all_ports = publish_all_ports

    @property
    def readonly_rootfs(self):
        """Gets the readonly_rootfs of this DockerHostConfigAllOf.  # noqa: E501

        Mount the container's root filesystem as read only.  # noqa: E501

        :return: The readonly_rootfs of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._readonly_rootfs

    @readonly_rootfs.setter
    def readonly_rootfs(self, readonly_rootfs):
        """Sets the readonly_rootfs of this DockerHostConfigAllOf.

        Mount the container's root filesystem as read only.  # noqa: E501

        :param readonly_rootfs: The readonly_rootfs of this DockerHostConfigAllOf.  # noqa: E501
        :type readonly_rootfs: bool
        """

        self._readonly_rootfs = readonly_rootfs

    @property
    def security_opt(self):
        """Gets the security_opt of this DockerHostConfigAllOf.  # noqa: E501

        A list of string values to customize labels for MLS systems, such as SELinux.  # noqa: E501

        :return: The security_opt of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_opt

    @security_opt.setter
    def security_opt(self, security_opt):
        """Sets the security_opt of this DockerHostConfigAllOf.

        A list of string values to customize labels for MLS systems, such as SELinux.  # noqa: E501

        :param security_opt: The security_opt of this DockerHostConfigAllOf.  # noqa: E501
        :type security_opt: list[str]
        """

        self._security_opt = security_opt

    @property
    def storage_opt(self):
        """Gets the storage_opt of this DockerHostConfigAllOf.  # noqa: E501

        Storage driver options for this container, in the form `{\"size\": \"120G\"}`.   # noqa: E501

        :return: The storage_opt of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._storage_opt

    @storage_opt.setter
    def storage_opt(self, storage_opt):
        """Sets the storage_opt of this DockerHostConfigAllOf.

        Storage driver options for this container, in the form `{\"size\": \"120G\"}`.   # noqa: E501

        :param storage_opt: The storage_opt of this DockerHostConfigAllOf.  # noqa: E501
        :type storage_opt: dict(str, str)
        """

        self._storage_opt = storage_opt

    @property
    def tmpfs(self):
        """Gets the tmpfs of this DockerHostConfigAllOf.  # noqa: E501

        A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: `{ \"/run\": \"rw,noexec,nosuid,size=65536k\" }`.   # noqa: E501

        :return: The tmpfs of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tmpfs

    @tmpfs.setter
    def tmpfs(self, tmpfs):
        """Sets the tmpfs of this DockerHostConfigAllOf.

        A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: `{ \"/run\": \"rw,noexec,nosuid,size=65536k\" }`.   # noqa: E501

        :param tmpfs: The tmpfs of this DockerHostConfigAllOf.  # noqa: E501
        :type tmpfs: dict(str, str)
        """

        self._tmpfs = tmpfs

    @property
    def uts_mode(self):
        """Gets the uts_mode of this DockerHostConfigAllOf.  # noqa: E501

        UTS namespace to use for the container.  # noqa: E501

        :return: The uts_mode of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uts_mode

    @uts_mode.setter
    def uts_mode(self, uts_mode):
        """Sets the uts_mode of this DockerHostConfigAllOf.

        UTS namespace to use for the container.  # noqa: E501

        :param uts_mode: The uts_mode of this DockerHostConfigAllOf.  # noqa: E501
        :type uts_mode: str
        """

        self._uts_mode = uts_mode

    @property
    def userns_mode(self):
        """Gets the userns_mode of this DockerHostConfigAllOf.  # noqa: E501

        Sets the usernamespace mode for the container when usernamespace remapping option is enabled.  # noqa: E501

        :return: The userns_mode of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._userns_mode

    @userns_mode.setter
    def userns_mode(self, userns_mode):
        """Sets the userns_mode of this DockerHostConfigAllOf.

        Sets the usernamespace mode for the container when usernamespace remapping option is enabled.  # noqa: E501

        :param userns_mode: The userns_mode of this DockerHostConfigAllOf.  # noqa: E501
        :type userns_mode: str
        """

        self._userns_mode = userns_mode

    @property
    def shm_size(self):
        """Gets the shm_size of this DockerHostConfigAllOf.  # noqa: E501

        Size of `/dev/shm` in bytes. If omitted, the system uses 64MB.  # noqa: E501

        :return: The shm_size of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: int
        """
        return self._shm_size

    @shm_size.setter
    def shm_size(self, shm_size):
        """Sets the shm_size of this DockerHostConfigAllOf.

        Size of `/dev/shm` in bytes. If omitted, the system uses 64MB.  # noqa: E501

        :param shm_size: The shm_size of this DockerHostConfigAllOf.  # noqa: E501
        :type shm_size: int
        """
        if (self.local_vars_configuration.client_side_validation and
                shm_size is not None and shm_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `shm_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._shm_size = shm_size

    @property
    def sysctls(self):
        """Gets the sysctls of this DockerHostConfigAllOf.  # noqa: E501

        A list of kernel parameters (sysctls) to set in the container. For example: `{\"net.ipv4.ip_forward\": \"1\"}`   # noqa: E501

        :return: The sysctls of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._sysctls

    @sysctls.setter
    def sysctls(self, sysctls):
        """Sets the sysctls of this DockerHostConfigAllOf.

        A list of kernel parameters (sysctls) to set in the container. For example: `{\"net.ipv4.ip_forward\": \"1\"}`   # noqa: E501

        :param sysctls: The sysctls of this DockerHostConfigAllOf.  # noqa: E501
        :type sysctls: dict(str, str)
        """

        self._sysctls = sysctls

    @property
    def runtime(self):
        """Gets the runtime of this DockerHostConfigAllOf.  # noqa: E501

        Runtime to use with this container.  # noqa: E501

        :return: The runtime of this DockerHostConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this DockerHostConfigAllOf.

        Runtime to use with this container.  # noqa: E501

        :param runtime: The runtime of this DockerHostConfigAllOf.  # noqa: E501
        :type runtime: str
        """

        self._runtime = runtime

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
        if not isinstance(other, DockerHostConfigAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerHostConfigAllOf):
            return True

        return self.to_dict() != other.to_dict()
