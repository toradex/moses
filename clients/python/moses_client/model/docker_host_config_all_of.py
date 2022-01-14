"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from moses_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from moses_client.exceptions import ApiAttributeError


def lazy_import():
    from moses_client.model.docker_host_config_all_of_log_config import DockerHostConfigAllOfLogConfig
    from moses_client.model.docker_mount import DockerMount
    from moses_client.model.docker_port_map import DockerPortMap
    from moses_client.model.docker_restart_policy import DockerRestartPolicy
    globals()['DockerHostConfigAllOfLogConfig'] = DockerHostConfigAllOfLogConfig
    globals()['DockerMount'] = DockerMount
    globals()['DockerPortMap'] = DockerPortMap
    globals()['DockerRestartPolicy'] = DockerRestartPolicy


class DockerHostConfigAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('shm_size',): {
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'binds': ([str],),  # noqa: E501
            'container_id_file': (str,),  # noqa: E501
            'log_config': (DockerHostConfigAllOfLogConfig,),  # noqa: E501
            'network_mode': (str,),  # noqa: E501
            'port_bindings': (DockerPortMap,),  # noqa: E501
            'restart_policy': (DockerRestartPolicy,),  # noqa: E501
            'auto_remove': (bool,),  # noqa: E501
            'volume_driver': (str,),  # noqa: E501
            'volumes_from': ([str],),  # noqa: E501
            'mounts': ([DockerMount],),  # noqa: E501
            'cap_add': ([str],),  # noqa: E501
            'cap_drop': ([str],),  # noqa: E501
            'dns': ([str],),  # noqa: E501
            'dns_options': ([str],),  # noqa: E501
            'dns_search': ([str],),  # noqa: E501
            'extra_hosts': ([str],),  # noqa: E501
            'group_add': ([str],),  # noqa: E501
            'ipc_mode': (str,),  # noqa: E501
            'cgroup': (str,),  # noqa: E501
            'links': ([str],),  # noqa: E501
            'oom_score_adj': (int,),  # noqa: E501
            'pid_mode': (str,),  # noqa: E501
            'privileged': (bool,),  # noqa: E501
            'publish_all_ports': (bool,),  # noqa: E501
            'readonly_rootfs': (bool,),  # noqa: E501
            'security_opt': ([str],),  # noqa: E501
            'storage_opt': ({str: (str,)},),  # noqa: E501
            'tmpfs': ({str: (str,)},),  # noqa: E501
            'uts_mode': (str,),  # noqa: E501
            'userns_mode': (str,),  # noqa: E501
            'shm_size': (int,),  # noqa: E501
            'sysctls': ({str: (str,)},),  # noqa: E501
            'runtime': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'binds': 'Binds',  # noqa: E501
        'container_id_file': 'ContainerIDFile',  # noqa: E501
        'log_config': 'LogConfig',  # noqa: E501
        'network_mode': 'NetworkMode',  # noqa: E501
        'port_bindings': 'PortBindings',  # noqa: E501
        'restart_policy': 'RestartPolicy',  # noqa: E501
        'auto_remove': 'AutoRemove',  # noqa: E501
        'volume_driver': 'VolumeDriver',  # noqa: E501
        'volumes_from': 'VolumesFrom',  # noqa: E501
        'mounts': 'Mounts',  # noqa: E501
        'cap_add': 'CapAdd',  # noqa: E501
        'cap_drop': 'CapDrop',  # noqa: E501
        'dns': 'Dns',  # noqa: E501
        'dns_options': 'DnsOptions',  # noqa: E501
        'dns_search': 'DnsSearch',  # noqa: E501
        'extra_hosts': 'ExtraHosts',  # noqa: E501
        'group_add': 'GroupAdd',  # noqa: E501
        'ipc_mode': 'IpcMode',  # noqa: E501
        'cgroup': 'Cgroup',  # noqa: E501
        'links': 'Links',  # noqa: E501
        'oom_score_adj': 'OomScoreAdj',  # noqa: E501
        'pid_mode': 'PidMode',  # noqa: E501
        'privileged': 'Privileged',  # noqa: E501
        'publish_all_ports': 'PublishAllPorts',  # noqa: E501
        'readonly_rootfs': 'ReadonlyRootfs',  # noqa: E501
        'security_opt': 'SecurityOpt',  # noqa: E501
        'storage_opt': 'StorageOpt',  # noqa: E501
        'tmpfs': 'Tmpfs',  # noqa: E501
        'uts_mode': 'UTSMode',  # noqa: E501
        'userns_mode': 'UsernsMode',  # noqa: E501
        'shm_size': 'ShmSize',  # noqa: E501
        'sysctls': 'Sysctls',  # noqa: E501
        'runtime': 'Runtime',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DockerHostConfigAllOf - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            binds ([str]): A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - `host-src:container-dest` to bind-mount a host path into the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `host-src:container-dest:ro` to make the bind mount read-only inside the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `volume-name:container-dest` to bind-mount a volume managed by a volume driver into the container. `container-dest` must be an _absolute_ path. - `volume-name:container-dest:ro` to mount the volume read-only inside the container.  `container-dest` must be an _absolute_ path. . [optional]  # noqa: E501
            container_id_file (str): Path to a file where the container ID is written. [optional]  # noqa: E501
            log_config (DockerHostConfigAllOfLogConfig): [optional]  # noqa: E501
            network_mode (str): Network mode to use for this container. Supported standard values are: `bridge`, `host`, `none`, and `container:<name|id>`. Any other value is taken as a custom network's name to which this container should connect to.. [optional]  # noqa: E501
            port_bindings (DockerPortMap): [optional]  # noqa: E501
            restart_policy (DockerRestartPolicy): [optional]  # noqa: E501
            auto_remove (bool): Automatically remove the container when the container's process exits. This has no effect if `RestartPolicy` is set.. [optional]  # noqa: E501
            volume_driver (str): Driver that this container uses to mount volumes.. [optional]  # noqa: E501
            volumes_from ([str]): A list of volumes to inherit from another container, specified in the form `<container name>[:<ro|rw>]`.. [optional]  # noqa: E501
            mounts ([DockerMount]): Specification for mounts to be added to the container.. [optional]  # noqa: E501
            cap_add ([str]): A list of kernel capabilities to add to the container.. [optional]  # noqa: E501
            cap_drop ([str]): A list of kernel capabilities to drop from the container.. [optional]  # noqa: E501
            dns ([str]): A list of DNS servers for the container to use.. [optional]  # noqa: E501
            dns_options ([str]): A list of DNS options.. [optional]  # noqa: E501
            dns_search ([str]): A list of DNS search domains.. [optional]  # noqa: E501
            extra_hosts ([str]): A list of hostnames/IP mappings to add to the container's `/etc/hosts` file. Specified in the form `[\"hostname:IP\"]`. . [optional]  # noqa: E501
            group_add ([str]): A list of additional groups that the container process will run as.. [optional]  # noqa: E501
            ipc_mode (str): IPC sharing mode for the container. Possible values are:  - `\"none\"`: own private IPC namespace, with /dev/shm not mounted - `\"private\"`: own private IPC namespace - `\"shareable\"`: own private IPC namespace, with a possibility to share it with other containers - `\"container:<name|id>\"`: join another (shareable) container's IPC namespace - `\"host\"`: use the host system's IPC namespace  If not specified, daemon default is used, which can either be `\"private\"` or `\"shareable\"`, depending on daemon version and configuration. . [optional]  # noqa: E501
            cgroup (str): Cgroup to use for the container.. [optional]  # noqa: E501
            links ([str]): A list of links for the container in the form `container_name:alias`.. [optional]  # noqa: E501
            oom_score_adj (int): An integer value containing the score given to the container in order to tune OOM killer preferences.. [optional]  # noqa: E501
            pid_mode (str): Set the PID (Process) Namespace mode for the container. It can be either:  - `\"container:<name|id>\"`: joins another container's PID namespace - `\"host\"`: use the host's PID namespace inside the container . [optional]  # noqa: E501
            privileged (bool): Gives the container full access to the host.. [optional]  # noqa: E501
            publish_all_ports (bool): Allocates an ephemeral host port for all of a container's exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by `/proc/sys/net/ipv4/ip_local_port_range`. . [optional]  # noqa: E501
            readonly_rootfs (bool): Mount the container's root filesystem as read only.. [optional]  # noqa: E501
            security_opt ([str]): A list of string values to customize labels for MLS systems, such as SELinux.. [optional]  # noqa: E501
            storage_opt ({str: (str,)}): Storage driver options for this container, in the form `{\"size\": \"120G\"}`. . [optional]  # noqa: E501
            tmpfs ({str: (str,)}): A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: `{ \"/run\": \"rw,noexec,nosuid,size=65536k\" }`. . [optional]  # noqa: E501
            uts_mode (str): UTS namespace to use for the container.. [optional]  # noqa: E501
            userns_mode (str): Sets the usernamespace mode for the container when usernamespace remapping option is enabled.. [optional]  # noqa: E501
            shm_size (int): Size of `/dev/shm` in bytes. If omitted, the system uses 64MB.. [optional]  # noqa: E501
            sysctls ({str: (str,)}): A list of kernel parameters (sysctls) to set in the container. For example: `{\"net.ipv4.ip_forward\": \"1\"}` . [optional]  # noqa: E501
            runtime (str): Runtime to use with this container.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DockerHostConfigAllOf - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            binds ([str]): A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - `host-src:container-dest` to bind-mount a host path into the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `host-src:container-dest:ro` to make the bind mount read-only inside the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `volume-name:container-dest` to bind-mount a volume managed by a volume driver into the container. `container-dest` must be an _absolute_ path. - `volume-name:container-dest:ro` to mount the volume read-only inside the container.  `container-dest` must be an _absolute_ path. . [optional]  # noqa: E501
            container_id_file (str): Path to a file where the container ID is written. [optional]  # noqa: E501
            log_config (DockerHostConfigAllOfLogConfig): [optional]  # noqa: E501
            network_mode (str): Network mode to use for this container. Supported standard values are: `bridge`, `host`, `none`, and `container:<name|id>`. Any other value is taken as a custom network's name to which this container should connect to.. [optional]  # noqa: E501
            port_bindings (DockerPortMap): [optional]  # noqa: E501
            restart_policy (DockerRestartPolicy): [optional]  # noqa: E501
            auto_remove (bool): Automatically remove the container when the container's process exits. This has no effect if `RestartPolicy` is set.. [optional]  # noqa: E501
            volume_driver (str): Driver that this container uses to mount volumes.. [optional]  # noqa: E501
            volumes_from ([str]): A list of volumes to inherit from another container, specified in the form `<container name>[:<ro|rw>]`.. [optional]  # noqa: E501
            mounts ([DockerMount]): Specification for mounts to be added to the container.. [optional]  # noqa: E501
            cap_add ([str]): A list of kernel capabilities to add to the container.. [optional]  # noqa: E501
            cap_drop ([str]): A list of kernel capabilities to drop from the container.. [optional]  # noqa: E501
            dns ([str]): A list of DNS servers for the container to use.. [optional]  # noqa: E501
            dns_options ([str]): A list of DNS options.. [optional]  # noqa: E501
            dns_search ([str]): A list of DNS search domains.. [optional]  # noqa: E501
            extra_hosts ([str]): A list of hostnames/IP mappings to add to the container's `/etc/hosts` file. Specified in the form `[\"hostname:IP\"]`. . [optional]  # noqa: E501
            group_add ([str]): A list of additional groups that the container process will run as.. [optional]  # noqa: E501
            ipc_mode (str): IPC sharing mode for the container. Possible values are:  - `\"none\"`: own private IPC namespace, with /dev/shm not mounted - `\"private\"`: own private IPC namespace - `\"shareable\"`: own private IPC namespace, with a possibility to share it with other containers - `\"container:<name|id>\"`: join another (shareable) container's IPC namespace - `\"host\"`: use the host system's IPC namespace  If not specified, daemon default is used, which can either be `\"private\"` or `\"shareable\"`, depending on daemon version and configuration. . [optional]  # noqa: E501
            cgroup (str): Cgroup to use for the container.. [optional]  # noqa: E501
            links ([str]): A list of links for the container in the form `container_name:alias`.. [optional]  # noqa: E501
            oom_score_adj (int): An integer value containing the score given to the container in order to tune OOM killer preferences.. [optional]  # noqa: E501
            pid_mode (str): Set the PID (Process) Namespace mode for the container. It can be either:  - `\"container:<name|id>\"`: joins another container's PID namespace - `\"host\"`: use the host's PID namespace inside the container . [optional]  # noqa: E501
            privileged (bool): Gives the container full access to the host.. [optional]  # noqa: E501
            publish_all_ports (bool): Allocates an ephemeral host port for all of a container's exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by `/proc/sys/net/ipv4/ip_local_port_range`. . [optional]  # noqa: E501
            readonly_rootfs (bool): Mount the container's root filesystem as read only.. [optional]  # noqa: E501
            security_opt ([str]): A list of string values to customize labels for MLS systems, such as SELinux.. [optional]  # noqa: E501
            storage_opt ({str: (str,)}): Storage driver options for this container, in the form `{\"size\": \"120G\"}`. . [optional]  # noqa: E501
            tmpfs ({str: (str,)}): A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: `{ \"/run\": \"rw,noexec,nosuid,size=65536k\" }`. . [optional]  # noqa: E501
            uts_mode (str): UTS namespace to use for the container.. [optional]  # noqa: E501
            userns_mode (str): Sets the usernamespace mode for the container when usernamespace remapping option is enabled.. [optional]  # noqa: E501
            shm_size (int): Size of `/dev/shm` in bytes. If omitted, the system uses 64MB.. [optional]  # noqa: E501
            sysctls ({str: (str,)}): A list of kernel parameters (sysctls) to set in the container. For example: `{\"net.ipv4.ip_forward\": \"1\"}` . [optional]  # noqa: E501
            runtime (str): Runtime to use with this container.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
