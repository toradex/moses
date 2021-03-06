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


class DockerContainer(object):
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
        'id': 'str',
        'created': 'str',
        'path': 'str',
        'args': 'list[str]',
        'state': 'DockerContainerState',
        'image': 'str',
        'resolv_conf_path': 'str',
        'hostname_path': 'str',
        'hosts_path': 'str',
        'log_path': 'str',
        'node': 'object',
        'name': 'str',
        'restart_count': 'int',
        'driver': 'str',
        'mount_label': 'str',
        'process_label': 'str',
        'app_armor_profile': 'str',
        'exec_i_ds': 'list[str]',
        'host_config': 'DockerHostConfig',
        'graph_driver': 'DockerGraphDriverData',
        'size_rw': 'int',
        'size_root_fs': 'int',
        'mounts': 'list[DockerMountPoint]',
        'config': 'DockerContainerConfig',
        'network_settings': 'DockerNetworkSettings'
    }

    attribute_map = {
        'id': 'Id',
        'created': 'Created',
        'path': 'Path',
        'args': 'Args',
        'state': 'State',
        'image': 'Image',
        'resolv_conf_path': 'ResolvConfPath',
        'hostname_path': 'HostnamePath',
        'hosts_path': 'HostsPath',
        'log_path': 'LogPath',
        'node': 'Node',
        'name': 'Name',
        'restart_count': 'RestartCount',
        'driver': 'Driver',
        'mount_label': 'MountLabel',
        'process_label': 'ProcessLabel',
        'app_armor_profile': 'AppArmorProfile',
        'exec_i_ds': 'ExecIDs',
        'host_config': 'HostConfig',
        'graph_driver': 'GraphDriver',
        'size_rw': 'SizeRw',
        'size_root_fs': 'SizeRootFs',
        'mounts': 'Mounts',
        'config': 'Config',
        'network_settings': 'NetworkSettings'
    }

    def __init__(self, id=None, created=None, path=None, args=None, state=None, image=None, resolv_conf_path=None, hostname_path=None, hosts_path=None, log_path=None, node=None, name=None, restart_count=None, driver=None, mount_label=None, process_label=None, app_armor_profile=None, exec_i_ds=None, host_config=None, graph_driver=None, size_rw=None, size_root_fs=None, mounts=None, config=None, network_settings=None, local_vars_configuration=None):  # noqa: E501
        """DockerContainer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._path = None
        self._args = None
        self._state = None
        self._image = None
        self._resolv_conf_path = None
        self._hostname_path = None
        self._hosts_path = None
        self._log_path = None
        self._node = None
        self._name = None
        self._restart_count = None
        self._driver = None
        self._mount_label = None
        self._process_label = None
        self._app_armor_profile = None
        self._exec_i_ds = None
        self._host_config = None
        self._graph_driver = None
        self._size_rw = None
        self._size_root_fs = None
        self._mounts = None
        self._config = None
        self._network_settings = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if path is not None:
            self.path = path
        if args is not None:
            self.args = args
        if state is not None:
            self.state = state
        if image is not None:
            self.image = image
        if resolv_conf_path is not None:
            self.resolv_conf_path = resolv_conf_path
        if hostname_path is not None:
            self.hostname_path = hostname_path
        if hosts_path is not None:
            self.hosts_path = hosts_path
        if log_path is not None:
            self.log_path = log_path
        if node is not None:
            self.node = node
        if name is not None:
            self.name = name
        if restart_count is not None:
            self.restart_count = restart_count
        if driver is not None:
            self.driver = driver
        if mount_label is not None:
            self.mount_label = mount_label
        if process_label is not None:
            self.process_label = process_label
        if app_armor_profile is not None:
            self.app_armor_profile = app_armor_profile
        if exec_i_ds is not None:
            self.exec_i_ds = exec_i_ds
        if host_config is not None:
            self.host_config = host_config
        if graph_driver is not None:
            self.graph_driver = graph_driver
        if size_rw is not None:
            self.size_rw = size_rw
        if size_root_fs is not None:
            self.size_root_fs = size_root_fs
        if mounts is not None:
            self.mounts = mounts
        if config is not None:
            self.config = config
        if network_settings is not None:
            self.network_settings = network_settings

    @property
    def id(self):
        """Gets the id of this DockerContainer.  # noqa: E501

        The ID of the container  # noqa: E501

        :return: The id of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DockerContainer.

        The ID of the container  # noqa: E501

        :param id: The id of this DockerContainer.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this DockerContainer.  # noqa: E501

        The time the container was created  # noqa: E501

        :return: The created of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DockerContainer.

        The time the container was created  # noqa: E501

        :param created: The created of this DockerContainer.  # noqa: E501
        :type created: str
        """

        self._created = created

    @property
    def path(self):
        """Gets the path of this DockerContainer.  # noqa: E501

        The path to the command being run  # noqa: E501

        :return: The path of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DockerContainer.

        The path to the command being run  # noqa: E501

        :param path: The path of this DockerContainer.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def args(self):
        """Gets the args of this DockerContainer.  # noqa: E501

        The arguments to the command being run  # noqa: E501

        :return: The args of this DockerContainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this DockerContainer.

        The arguments to the command being run  # noqa: E501

        :param args: The args of this DockerContainer.  # noqa: E501
        :type args: list[str]
        """

        self._args = args

    @property
    def state(self):
        """Gets the state of this DockerContainer.  # noqa: E501


        :return: The state of this DockerContainer.  # noqa: E501
        :rtype: DockerContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DockerContainer.


        :param state: The state of this DockerContainer.  # noqa: E501
        :type state: DockerContainerState
        """

        self._state = state

    @property
    def image(self):
        """Gets the image of this DockerContainer.  # noqa: E501

        The container's image  # noqa: E501

        :return: The image of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DockerContainer.

        The container's image  # noqa: E501

        :param image: The image of this DockerContainer.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def resolv_conf_path(self):
        """Gets the resolv_conf_path of this DockerContainer.  # noqa: E501


        :return: The resolv_conf_path of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._resolv_conf_path

    @resolv_conf_path.setter
    def resolv_conf_path(self, resolv_conf_path):
        """Sets the resolv_conf_path of this DockerContainer.


        :param resolv_conf_path: The resolv_conf_path of this DockerContainer.  # noqa: E501
        :type resolv_conf_path: str
        """

        self._resolv_conf_path = resolv_conf_path

    @property
    def hostname_path(self):
        """Gets the hostname_path of this DockerContainer.  # noqa: E501


        :return: The hostname_path of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._hostname_path

    @hostname_path.setter
    def hostname_path(self, hostname_path):
        """Sets the hostname_path of this DockerContainer.


        :param hostname_path: The hostname_path of this DockerContainer.  # noqa: E501
        :type hostname_path: str
        """

        self._hostname_path = hostname_path

    @property
    def hosts_path(self):
        """Gets the hosts_path of this DockerContainer.  # noqa: E501


        :return: The hosts_path of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._hosts_path

    @hosts_path.setter
    def hosts_path(self, hosts_path):
        """Sets the hosts_path of this DockerContainer.


        :param hosts_path: The hosts_path of this DockerContainer.  # noqa: E501
        :type hosts_path: str
        """

        self._hosts_path = hosts_path

    @property
    def log_path(self):
        """Gets the log_path of this DockerContainer.  # noqa: E501


        :return: The log_path of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this DockerContainer.


        :param log_path: The log_path of this DockerContainer.  # noqa: E501
        :type log_path: str
        """

        self._log_path = log_path

    @property
    def node(self):
        """Gets the node of this DockerContainer.  # noqa: E501

        TODO  # noqa: E501

        :return: The node of this DockerContainer.  # noqa: E501
        :rtype: object
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this DockerContainer.

        TODO  # noqa: E501

        :param node: The node of this DockerContainer.  # noqa: E501
        :type node: object
        """

        self._node = node

    @property
    def name(self):
        """Gets the name of this DockerContainer.  # noqa: E501


        :return: The name of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DockerContainer.


        :param name: The name of this DockerContainer.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def restart_count(self):
        """Gets the restart_count of this DockerContainer.  # noqa: E501


        :return: The restart_count of this DockerContainer.  # noqa: E501
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """Sets the restart_count of this DockerContainer.


        :param restart_count: The restart_count of this DockerContainer.  # noqa: E501
        :type restart_count: int
        """

        self._restart_count = restart_count

    @property
    def driver(self):
        """Gets the driver of this DockerContainer.  # noqa: E501


        :return: The driver of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this DockerContainer.


        :param driver: The driver of this DockerContainer.  # noqa: E501
        :type driver: str
        """

        self._driver = driver

    @property
    def mount_label(self):
        """Gets the mount_label of this DockerContainer.  # noqa: E501


        :return: The mount_label of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._mount_label

    @mount_label.setter
    def mount_label(self, mount_label):
        """Sets the mount_label of this DockerContainer.


        :param mount_label: The mount_label of this DockerContainer.  # noqa: E501
        :type mount_label: str
        """

        self._mount_label = mount_label

    @property
    def process_label(self):
        """Gets the process_label of this DockerContainer.  # noqa: E501


        :return: The process_label of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._process_label

    @process_label.setter
    def process_label(self, process_label):
        """Sets the process_label of this DockerContainer.


        :param process_label: The process_label of this DockerContainer.  # noqa: E501
        :type process_label: str
        """

        self._process_label = process_label

    @property
    def app_armor_profile(self):
        """Gets the app_armor_profile of this DockerContainer.  # noqa: E501


        :return: The app_armor_profile of this DockerContainer.  # noqa: E501
        :rtype: str
        """
        return self._app_armor_profile

    @app_armor_profile.setter
    def app_armor_profile(self, app_armor_profile):
        """Sets the app_armor_profile of this DockerContainer.


        :param app_armor_profile: The app_armor_profile of this DockerContainer.  # noqa: E501
        :type app_armor_profile: str
        """

        self._app_armor_profile = app_armor_profile

    @property
    def exec_i_ds(self):
        """Gets the exec_i_ds of this DockerContainer.  # noqa: E501


        :return: The exec_i_ds of this DockerContainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._exec_i_ds

    @exec_i_ds.setter
    def exec_i_ds(self, exec_i_ds):
        """Sets the exec_i_ds of this DockerContainer.


        :param exec_i_ds: The exec_i_ds of this DockerContainer.  # noqa: E501
        :type exec_i_ds: list[str]
        """

        self._exec_i_ds = exec_i_ds

    @property
    def host_config(self):
        """Gets the host_config of this DockerContainer.  # noqa: E501


        :return: The host_config of this DockerContainer.  # noqa: E501
        :rtype: DockerHostConfig
        """
        return self._host_config

    @host_config.setter
    def host_config(self, host_config):
        """Sets the host_config of this DockerContainer.


        :param host_config: The host_config of this DockerContainer.  # noqa: E501
        :type host_config: DockerHostConfig
        """

        self._host_config = host_config

    @property
    def graph_driver(self):
        """Gets the graph_driver of this DockerContainer.  # noqa: E501


        :return: The graph_driver of this DockerContainer.  # noqa: E501
        :rtype: DockerGraphDriverData
        """
        return self._graph_driver

    @graph_driver.setter
    def graph_driver(self, graph_driver):
        """Sets the graph_driver of this DockerContainer.


        :param graph_driver: The graph_driver of this DockerContainer.  # noqa: E501
        :type graph_driver: DockerGraphDriverData
        """

        self._graph_driver = graph_driver

    @property
    def size_rw(self):
        """Gets the size_rw of this DockerContainer.  # noqa: E501

        The size of files that have been created or changed by this container.  # noqa: E501

        :return: The size_rw of this DockerContainer.  # noqa: E501
        :rtype: int
        """
        return self._size_rw

    @size_rw.setter
    def size_rw(self, size_rw):
        """Sets the size_rw of this DockerContainer.

        The size of files that have been created or changed by this container.  # noqa: E501

        :param size_rw: The size_rw of this DockerContainer.  # noqa: E501
        :type size_rw: int
        """

        self._size_rw = size_rw

    @property
    def size_root_fs(self):
        """Gets the size_root_fs of this DockerContainer.  # noqa: E501

        The total size of all the files in this container.  # noqa: E501

        :return: The size_root_fs of this DockerContainer.  # noqa: E501
        :rtype: int
        """
        return self._size_root_fs

    @size_root_fs.setter
    def size_root_fs(self, size_root_fs):
        """Sets the size_root_fs of this DockerContainer.

        The total size of all the files in this container.  # noqa: E501

        :param size_root_fs: The size_root_fs of this DockerContainer.  # noqa: E501
        :type size_root_fs: int
        """

        self._size_root_fs = size_root_fs

    @property
    def mounts(self):
        """Gets the mounts of this DockerContainer.  # noqa: E501


        :return: The mounts of this DockerContainer.  # noqa: E501
        :rtype: list[DockerMountPoint]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this DockerContainer.


        :param mounts: The mounts of this DockerContainer.  # noqa: E501
        :type mounts: list[DockerMountPoint]
        """

        self._mounts = mounts

    @property
    def config(self):
        """Gets the config of this DockerContainer.  # noqa: E501


        :return: The config of this DockerContainer.  # noqa: E501
        :rtype: DockerContainerConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this DockerContainer.


        :param config: The config of this DockerContainer.  # noqa: E501
        :type config: DockerContainerConfig
        """

        self._config = config

    @property
    def network_settings(self):
        """Gets the network_settings of this DockerContainer.  # noqa: E501


        :return: The network_settings of this DockerContainer.  # noqa: E501
        :rtype: DockerNetworkSettings
        """
        return self._network_settings

    @network_settings.setter
    def network_settings(self, network_settings):
        """Sets the network_settings of this DockerContainer.


        :param network_settings: The network_settings of this DockerContainer.  # noqa: E501
        :type network_settings: DockerNetworkSettings
        """

        self._network_settings = network_settings

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
        if not isinstance(other, DockerContainer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerContainer):
            return True

        return self.to_dict() != other.to_dict()
