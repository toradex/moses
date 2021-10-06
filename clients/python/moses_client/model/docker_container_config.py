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
)
from ..model_utils import OpenApiModel
from moses_client.exceptions import ApiAttributeError


def lazy_import():
    from moses_client.model.docker_health_config import DockerHealthConfig
    globals()['DockerHealthConfig'] = DockerHealthConfig


class DockerContainerConfig(ModelNormal):
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
            'hostname': (str,),  # noqa: E501
            'domainname': (str,),  # noqa: E501
            'user': (str,),  # noqa: E501
            'attach_stdin': (bool,),  # noqa: E501
            'attach_stdout': (bool,),  # noqa: E501
            'attach_stderr': (bool,),  # noqa: E501
            'exposed_ports': ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)},),  # noqa: E501
            'tty': (bool,),  # noqa: E501
            'open_stdin': (bool,),  # noqa: E501
            'stdin_once': (bool,),  # noqa: E501
            'env': ([str],),  # noqa: E501
            'cmd': ([str],),  # noqa: E501
            'healthcheck': (DockerHealthConfig,),  # noqa: E501
            'args_escaped': (bool,),  # noqa: E501
            'image': (str,),  # noqa: E501
            'volumes': ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)},),  # noqa: E501
            'working_dir': (str,),  # noqa: E501
            'entrypoint': ([str],),  # noqa: E501
            'network_disabled': (bool,),  # noqa: E501
            'mac_address': (str,),  # noqa: E501
            'on_build': ([str],),  # noqa: E501
            'labels': ({str: (str,)},),  # noqa: E501
            'stop_signal': (str,),  # noqa: E501
            'stop_timeout': (int,),  # noqa: E501
            'shell': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'hostname': 'Hostname',  # noqa: E501
        'domainname': 'Domainname',  # noqa: E501
        'user': 'User',  # noqa: E501
        'attach_stdin': 'AttachStdin',  # noqa: E501
        'attach_stdout': 'AttachStdout',  # noqa: E501
        'attach_stderr': 'AttachStderr',  # noqa: E501
        'exposed_ports': 'ExposedPorts',  # noqa: E501
        'tty': 'Tty',  # noqa: E501
        'open_stdin': 'OpenStdin',  # noqa: E501
        'stdin_once': 'StdinOnce',  # noqa: E501
        'env': 'Env',  # noqa: E501
        'cmd': 'Cmd',  # noqa: E501
        'healthcheck': 'Healthcheck',  # noqa: E501
        'args_escaped': 'ArgsEscaped',  # noqa: E501
        'image': 'Image',  # noqa: E501
        'volumes': 'Volumes',  # noqa: E501
        'working_dir': 'WorkingDir',  # noqa: E501
        'entrypoint': 'Entrypoint',  # noqa: E501
        'network_disabled': 'NetworkDisabled',  # noqa: E501
        'mac_address': 'MacAddress',  # noqa: E501
        'on_build': 'OnBuild',  # noqa: E501
        'labels': 'Labels',  # noqa: E501
        'stop_signal': 'StopSignal',  # noqa: E501
        'stop_timeout': 'StopTimeout',  # noqa: E501
        'shell': 'Shell',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DockerContainerConfig - a model defined in OpenAPI

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
            hostname (str): The hostname to use for the container, as a valid RFC 1123 hostname.. [optional]  # noqa: E501
            domainname (str): The domain name to use for the container.. [optional]  # noqa: E501
            user (str): The user that commands are run as inside the container.. [optional]  # noqa: E501
            attach_stdin (bool): Whether to attach to `stdin`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            attach_stdout (bool): Whether to attach to `stdout`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            attach_stderr (bool): Whether to attach to `stderr`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            exposed_ports ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): An object mapping ports to an empty object in the form:  `{\"<port>/<tcp|udp|sctp>\": {}}` . [optional]  # noqa: E501
            tty (bool): Attach standard streams to a TTY, including `stdin` if it is not closed.. [optional] if omitted the server will use the default value of False  # noqa: E501
            open_stdin (bool): Open `stdin`. [optional] if omitted the server will use the default value of False  # noqa: E501
            stdin_once (bool): Close `stdin` after one attached client disconnects. [optional] if omitted the server will use the default value of False  # noqa: E501
            env ([str]): A list of environment variables to set inside the container in the form `[\"VAR=value\", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value. . [optional]  # noqa: E501
            cmd ([str]): Command to run specified as a string or an array of strings.. [optional]  # noqa: E501
            healthcheck (DockerHealthConfig): [optional]  # noqa: E501
            args_escaped (bool): Command is already escaped (Windows only). [optional]  # noqa: E501
            image (str): The name of the image to use when creating the container. [optional]  # noqa: E501
            volumes ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): An object mapping mount point paths inside the container to empty objects.. [optional]  # noqa: E501
            working_dir (str): The working directory for commands to run in.. [optional]  # noqa: E501
            entrypoint ([str]): The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (`[\"\"]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`). . [optional]  # noqa: E501
            network_disabled (bool): Disable networking for the container.. [optional]  # noqa: E501
            mac_address (str): MAC address of the container.. [optional]  # noqa: E501
            on_build ([str]): `ONBUILD` metadata that were defined in the image's `Dockerfile`.. [optional]  # noqa: E501
            labels ({str: (str,)}): User-defined key/value metadata.. [optional]  # noqa: E501
            stop_signal (str): Signal to stop a container as a string or unsigned integer.. [optional] if omitted the server will use the default value of "SIGTERM"  # noqa: E501
            stop_timeout (int): Timeout to stop a container in seconds.. [optional]  # noqa: E501
            shell ([str]): Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell.. [optional]  # noqa: E501
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
        """DockerContainerConfig - a model defined in OpenAPI

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
            hostname (str): The hostname to use for the container, as a valid RFC 1123 hostname.. [optional]  # noqa: E501
            domainname (str): The domain name to use for the container.. [optional]  # noqa: E501
            user (str): The user that commands are run as inside the container.. [optional]  # noqa: E501
            attach_stdin (bool): Whether to attach to `stdin`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            attach_stdout (bool): Whether to attach to `stdout`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            attach_stderr (bool): Whether to attach to `stderr`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            exposed_ports ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): An object mapping ports to an empty object in the form:  `{\"<port>/<tcp|udp|sctp>\": {}}` . [optional]  # noqa: E501
            tty (bool): Attach standard streams to a TTY, including `stdin` if it is not closed.. [optional] if omitted the server will use the default value of False  # noqa: E501
            open_stdin (bool): Open `stdin`. [optional] if omitted the server will use the default value of False  # noqa: E501
            stdin_once (bool): Close `stdin` after one attached client disconnects. [optional] if omitted the server will use the default value of False  # noqa: E501
            env ([str]): A list of environment variables to set inside the container in the form `[\"VAR=value\", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value. . [optional]  # noqa: E501
            cmd ([str]): Command to run specified as a string or an array of strings.. [optional]  # noqa: E501
            healthcheck (DockerHealthConfig): [optional]  # noqa: E501
            args_escaped (bool): Command is already escaped (Windows only). [optional]  # noqa: E501
            image (str): The name of the image to use when creating the container. [optional]  # noqa: E501
            volumes ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): An object mapping mount point paths inside the container to empty objects.. [optional]  # noqa: E501
            working_dir (str): The working directory for commands to run in.. [optional]  # noqa: E501
            entrypoint ([str]): The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (`[\"\"]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`). . [optional]  # noqa: E501
            network_disabled (bool): Disable networking for the container.. [optional]  # noqa: E501
            mac_address (str): MAC address of the container.. [optional]  # noqa: E501
            on_build ([str]): `ONBUILD` metadata that were defined in the image's `Dockerfile`.. [optional]  # noqa: E501
            labels ({str: (str,)}): User-defined key/value metadata.. [optional]  # noqa: E501
            stop_signal (str): Signal to stop a container as a string or unsigned integer.. [optional] if omitted the server will use the default value of "SIGTERM"  # noqa: E501
            stop_timeout (int): Timeout to stop a container in seconds.. [optional]  # noqa: E501
            shell ([str]): Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell.. [optional]  # noqa: E501
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
