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



class Platform(ModelNormal):
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
        return {
            'id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'standard': (bool,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'runtimes': ([str],),  # noqa: E501
            'sdkcontainerusername': (str,),  # noqa: E501
            'sdkcontainerpassword': (str,),  # noqa: E501
            'dockercomposefile': ({str: (str,)},),  # noqa: E501
            'startupscript': ({str: (str,)},),  # noqa: E501
            'shutdownscript': ({str: (str,)},),  # noqa: E501
            'ports': ({str: ({str: (str,)},)},),  # noqa: E501
            'volumes': ({str: ({str: (str,)},)},),  # noqa: E501
            'devices': ({str: ([str],)},),  # noqa: E501
            'networks': ({str: ([str],)},),  # noqa: E501
            'extraparms': ({str: ({str: (str,)},)},),  # noqa: E501
            'props': ({str: ({str: (str,)},)},),  # noqa: E501
            'description': (str,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'architecture': (str,),  # noqa: E501
            'deprecated': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'standard': 'standard',  # noqa: E501
        'version': 'version',  # noqa: E501
        'runtimes': 'runtimes',  # noqa: E501
        'sdkcontainerusername': 'sdkcontainerusername',  # noqa: E501
        'sdkcontainerpassword': 'sdkcontainerpassword',  # noqa: E501
        'dockercomposefile': 'dockercomposefile',  # noqa: E501
        'startupscript': 'startupscript',  # noqa: E501
        'shutdownscript': 'shutdownscript',  # noqa: E501
        'ports': 'ports',  # noqa: E501
        'volumes': 'volumes',  # noqa: E501
        'devices': 'devices',  # noqa: E501
        'networks': 'networks',  # noqa: E501
        'extraparms': 'extraparms',  # noqa: E501
        'props': 'props',  # noqa: E501
        'description': 'description',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'architecture': 'architecture',  # noqa: E501
        'deprecated': 'deprecated',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'name',  # noqa: E501
        'standard',  # noqa: E501
        'version',  # noqa: E501
        'description',  # noqa: E501
        'tags',  # noqa: E501
        'architecture',  # noqa: E501
        'deprecated',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Platform - a model defined in OpenAPI

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
            id (str): Unique name (should be filesystem-compatible). [optional]  # noqa: E501
            name (str): Platform mnemnonic name. [optional]  # noqa: E501
            standard (bool): true if the platform is provided by Toradex and can't be modified. [optional]  # noqa: E501
            version (str): Version of the image (not related to distro version). [optional]  # noqa: E501
            runtimes ([str]): runtimes/languages supported by the container. [optional]  # noqa: E501
            sdkcontainerusername (str): ssh user supported by the SDK container. [optional]  # noqa: E501
            sdkcontainerpassword (str): password used to ssh inside the SDK container. [optional]  # noqa: E501
            dockercomposefile ({str: (str,)}): path of docker-compose file to be used to start additional containers needed by the app. [optional]  # noqa: E501
            startupscript ({str: (str,)}): path of script to be run when application debugging starts. [optional]  # noqa: E501
            shutdownscript ({str: (str,)}): path of script to be run when application debugging stops. [optional]  # noqa: E501
            ports ({str: ({str: (str,)},)}): ports to be exposed from the container. [optional]  # noqa: E501
            volumes ({str: ({str: (str,)},)}): Local folders to be mounted as mount points inside a container. [optional]  # noqa: E501
            devices ({str: ([str],)}): Additional devices to be shared inside container. [optional]  # noqa: E501
            networks ({str: ([str],)}): Networks used by container (in debug it will always be also on bridge). [optional]  # noqa: E501
            extraparms ({str: ({str: (str,)},)}): Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML). [optional]  # noqa: E501
            props ({str: ({str: (str,)},)}): Custom properties (may be used in dockerfile or by extensions). [optional]  # noqa: E501
            description (str): Platform human-readable description. [optional]  # noqa: E501
            tags ([str]): strings used to identify specific properties of the platform. [optional]  # noqa: E501
            architecture (str): architecture as defined by docker. [optional]  # noqa: E501
            deprecated (bool): true for platforms that are no longer supported. [optional]  # noqa: E501
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
        """Platform - a model defined in OpenAPI

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
            id (str): Unique name (should be filesystem-compatible). [optional]  # noqa: E501
            name (str): Platform mnemnonic name. [optional]  # noqa: E501
            standard (bool): true if the platform is provided by Toradex and can't be modified. [optional]  # noqa: E501
            version (str): Version of the image (not related to distro version). [optional]  # noqa: E501
            runtimes ([str]): runtimes/languages supported by the container. [optional]  # noqa: E501
            sdkcontainerusername (str): ssh user supported by the SDK container. [optional]  # noqa: E501
            sdkcontainerpassword (str): password used to ssh inside the SDK container. [optional]  # noqa: E501
            dockercomposefile ({str: (str,)}): path of docker-compose file to be used to start additional containers needed by the app. [optional]  # noqa: E501
            startupscript ({str: (str,)}): path of script to be run when application debugging starts. [optional]  # noqa: E501
            shutdownscript ({str: (str,)}): path of script to be run when application debugging stops. [optional]  # noqa: E501
            ports ({str: ({str: (str,)},)}): ports to be exposed from the container. [optional]  # noqa: E501
            volumes ({str: ({str: (str,)},)}): Local folders to be mounted as mount points inside a container. [optional]  # noqa: E501
            devices ({str: ([str],)}): Additional devices to be shared inside container. [optional]  # noqa: E501
            networks ({str: ([str],)}): Networks used by container (in debug it will always be also on bridge). [optional]  # noqa: E501
            extraparms ({str: ({str: (str,)},)}): Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML). [optional]  # noqa: E501
            props ({str: ({str: (str,)},)}): Custom properties (may be used in dockerfile or by extensions). [optional]  # noqa: E501
            description (str): Platform human-readable description. [optional]  # noqa: E501
            tags ([str]): strings used to identify specific properties of the platform. [optional]  # noqa: E501
            architecture (str): architecture as defined by docker. [optional]  # noqa: E501
            deprecated (bool): true for platforms that are no longer supported. [optional]  # noqa: E501
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
