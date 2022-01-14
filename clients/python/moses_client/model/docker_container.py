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
    from moses_client.model.docker_container_config import DockerContainerConfig
    from moses_client.model.docker_container_state import DockerContainerState
    from moses_client.model.docker_graph_driver_data import DockerGraphDriverData
    from moses_client.model.docker_host_config import DockerHostConfig
    from moses_client.model.docker_mount_point import DockerMountPoint
    from moses_client.model.docker_network_settings import DockerNetworkSettings
    globals()['DockerContainerConfig'] = DockerContainerConfig
    globals()['DockerContainerState'] = DockerContainerState
    globals()['DockerGraphDriverData'] = DockerGraphDriverData
    globals()['DockerHostConfig'] = DockerHostConfig
    globals()['DockerMountPoint'] = DockerMountPoint
    globals()['DockerNetworkSettings'] = DockerNetworkSettings


class DockerContainer(ModelNormal):
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
            'id': (str,),  # noqa: E501
            'created': (str,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'args': ([str],),  # noqa: E501
            'state': (DockerContainerState,),  # noqa: E501
            'image': (str,),  # noqa: E501
            'resolv_conf_path': (str,),  # noqa: E501
            'hostname_path': (str,),  # noqa: E501
            'hosts_path': (str,),  # noqa: E501
            'log_path': (str,),  # noqa: E501
            'node': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'restart_count': (int,),  # noqa: E501
            'driver': (str,),  # noqa: E501
            'mount_label': (str,),  # noqa: E501
            'process_label': (str,),  # noqa: E501
            'app_armor_profile': (str,),  # noqa: E501
            'exec_ids': ([str],),  # noqa: E501
            'host_config': (DockerHostConfig,),  # noqa: E501
            'graph_driver': (DockerGraphDriverData,),  # noqa: E501
            'size_rw': (int,),  # noqa: E501
            'size_root_fs': (int,),  # noqa: E501
            'mounts': ([DockerMountPoint],),  # noqa: E501
            'config': (DockerContainerConfig,),  # noqa: E501
            'network_settings': (DockerNetworkSettings,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'Id',  # noqa: E501
        'created': 'Created',  # noqa: E501
        'path': 'Path',  # noqa: E501
        'args': 'Args',  # noqa: E501
        'state': 'State',  # noqa: E501
        'image': 'Image',  # noqa: E501
        'resolv_conf_path': 'ResolvConfPath',  # noqa: E501
        'hostname_path': 'HostnamePath',  # noqa: E501
        'hosts_path': 'HostsPath',  # noqa: E501
        'log_path': 'LogPath',  # noqa: E501
        'node': 'Node',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'restart_count': 'RestartCount',  # noqa: E501
        'driver': 'Driver',  # noqa: E501
        'mount_label': 'MountLabel',  # noqa: E501
        'process_label': 'ProcessLabel',  # noqa: E501
        'app_armor_profile': 'AppArmorProfile',  # noqa: E501
        'exec_ids': 'ExecIDs',  # noqa: E501
        'host_config': 'HostConfig',  # noqa: E501
        'graph_driver': 'GraphDriver',  # noqa: E501
        'size_rw': 'SizeRw',  # noqa: E501
        'size_root_fs': 'SizeRootFs',  # noqa: E501
        'mounts': 'Mounts',  # noqa: E501
        'config': 'Config',  # noqa: E501
        'network_settings': 'NetworkSettings',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DockerContainer - a model defined in OpenAPI

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
            id (str): The ID of the container. [optional]  # noqa: E501
            created (str): The time the container was created. [optional]  # noqa: E501
            path (str): The path to the command being run. [optional]  # noqa: E501
            args ([str]): The arguments to the command being run. [optional]  # noqa: E501
            state (DockerContainerState): [optional]  # noqa: E501
            image (str): The container's image. [optional]  # noqa: E501
            resolv_conf_path (str): [optional]  # noqa: E501
            hostname_path (str): [optional]  # noqa: E501
            hosts_path (str): [optional]  # noqa: E501
            log_path (str): [optional]  # noqa: E501
            node (bool, date, datetime, dict, float, int, list, str, none_type): TODO. [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            restart_count (int): [optional]  # noqa: E501
            driver (str): [optional]  # noqa: E501
            mount_label (str): [optional]  # noqa: E501
            process_label (str): [optional]  # noqa: E501
            app_armor_profile (str): [optional]  # noqa: E501
            exec_ids ([str]): [optional]  # noqa: E501
            host_config (DockerHostConfig): [optional]  # noqa: E501
            graph_driver (DockerGraphDriverData): [optional]  # noqa: E501
            size_rw (int): The size of files that have been created or changed by this container.. [optional]  # noqa: E501
            size_root_fs (int): The total size of all the files in this container.. [optional]  # noqa: E501
            mounts ([DockerMountPoint]): [optional]  # noqa: E501
            config (DockerContainerConfig): [optional]  # noqa: E501
            network_settings (DockerNetworkSettings): [optional]  # noqa: E501
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
        """DockerContainer - a model defined in OpenAPI

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
            id (str): The ID of the container. [optional]  # noqa: E501
            created (str): The time the container was created. [optional]  # noqa: E501
            path (str): The path to the command being run. [optional]  # noqa: E501
            args ([str]): The arguments to the command being run. [optional]  # noqa: E501
            state (DockerContainerState): [optional]  # noqa: E501
            image (str): The container's image. [optional]  # noqa: E501
            resolv_conf_path (str): [optional]  # noqa: E501
            hostname_path (str): [optional]  # noqa: E501
            hosts_path (str): [optional]  # noqa: E501
            log_path (str): [optional]  # noqa: E501
            node (bool, date, datetime, dict, float, int, list, str, none_type): TODO. [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            restart_count (int): [optional]  # noqa: E501
            driver (str): [optional]  # noqa: E501
            mount_label (str): [optional]  # noqa: E501
            process_label (str): [optional]  # noqa: E501
            app_armor_profile (str): [optional]  # noqa: E501
            exec_ids ([str]): [optional]  # noqa: E501
            host_config (DockerHostConfig): [optional]  # noqa: E501
            graph_driver (DockerGraphDriverData): [optional]  # noqa: E501
            size_rw (int): The size of files that have been created or changed by this container.. [optional]  # noqa: E501
            size_root_fs (int): The total size of all the files in this container.. [optional]  # noqa: E501
            mounts ([DockerMountPoint]): [optional]  # noqa: E501
            config (DockerContainerConfig): [optional]  # noqa: E501
            network_settings (DockerNetworkSettings): [optional]  # noqa: E501
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
