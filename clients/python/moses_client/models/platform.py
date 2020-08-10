# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class Platform(object):
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
        'name': 'str',
        'standard': 'bool',
        'version': 'str',
        'runtimes': 'list[str]',
        'sdkcontainerusername': 'str',
        'sdkcontainerpassword': 'str',
        'dockercomposefile': 'dict(str, str)',
        'startupscript': 'dict(str, str)',
        'shutdownscript': 'dict(str, str)',
        'ports': 'dict(str, dict(str, str))',
        'volumes': 'dict(str, dict(str, str))',
        'devices': 'dict(str, list[str])',
        'networks': 'dict(str, list[str])',
        'extraparms': 'dict(str, dict(str, object))',
        'props': 'dict(str, dict(str, str))',
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'standard': 'standard',
        'version': 'version',
        'runtimes': 'runtimes',
        'sdkcontainerusername': 'sdkcontainerusername',
        'sdkcontainerpassword': 'sdkcontainerpassword',
        'dockercomposefile': 'dockercomposefile',
        'startupscript': 'startupscript',
        'shutdownscript': 'shutdownscript',
        'ports': 'ports',
        'volumes': 'volumes',
        'devices': 'devices',
        'networks': 'networks',
        'extraparms': 'extraparms',
        'props': 'props',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, standard=None, version=None, runtimes=None, sdkcontainerusername=None, sdkcontainerpassword=None, dockercomposefile=None, startupscript=None, shutdownscript=None, ports=None, volumes=None, devices=None, networks=None, extraparms=None, props=None, description=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """Platform - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._standard = None
        self._version = None
        self._runtimes = None
        self._sdkcontainerusername = None
        self._sdkcontainerpassword = None
        self._dockercomposefile = None
        self._startupscript = None
        self._shutdownscript = None
        self._ports = None
        self._volumes = None
        self._devices = None
        self._networks = None
        self._extraparms = None
        self._props = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if standard is not None:
            self.standard = standard
        if version is not None:
            self.version = version
        if runtimes is not None:
            self.runtimes = runtimes
        if sdkcontainerusername is not None:
            self.sdkcontainerusername = sdkcontainerusername
        if sdkcontainerpassword is not None:
            self.sdkcontainerpassword = sdkcontainerpassword
        if dockercomposefile is not None:
            self.dockercomposefile = dockercomposefile
        if startupscript is not None:
            self.startupscript = startupscript
        if shutdownscript is not None:
            self.shutdownscript = shutdownscript
        if ports is not None:
            self.ports = ports
        if volumes is not None:
            self.volumes = volumes
        if devices is not None:
            self.devices = devices
        if networks is not None:
            self.networks = networks
        if extraparms is not None:
            self.extraparms = extraparms
        if props is not None:
            self.props = props
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this Platform.  # noqa: E501

        Unique name (should be filesystem-compatible)  # noqa: E501

        :return: The id of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Platform.

        Unique name (should be filesystem-compatible)  # noqa: E501

        :param id: The id of this Platform.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Platform.  # noqa: E501

        Platform mnemnonic name  # noqa: E501

        :return: The name of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Platform.

        Platform mnemnonic name  # noqa: E501

        :param name: The name of this Platform.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def standard(self):
        """Gets the standard of this Platform.  # noqa: E501

        true if the platform is provided by Toradex and can't be modified  # noqa: E501

        :return: The standard of this Platform.  # noqa: E501
        :rtype: bool
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this Platform.

        true if the platform is provided by Toradex and can't be modified  # noqa: E501

        :param standard: The standard of this Platform.  # noqa: E501
        :type standard: bool
        """

        self._standard = standard

    @property
    def version(self):
        """Gets the version of this Platform.  # noqa: E501

        Version of the image (not related to distro version)  # noqa: E501

        :return: The version of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Platform.

        Version of the image (not related to distro version)  # noqa: E501

        :param version: The version of this Platform.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def runtimes(self):
        """Gets the runtimes of this Platform.  # noqa: E501

        runtimes/languages supported by the container  # noqa: E501

        :return: The runtimes of this Platform.  # noqa: E501
        :rtype: list[str]
        """
        return self._runtimes

    @runtimes.setter
    def runtimes(self, runtimes):
        """Sets the runtimes of this Platform.

        runtimes/languages supported by the container  # noqa: E501

        :param runtimes: The runtimes of this Platform.  # noqa: E501
        :type runtimes: list[str]
        """

        self._runtimes = runtimes

    @property
    def sdkcontainerusername(self):
        """Gets the sdkcontainerusername of this Platform.  # noqa: E501

        ssh user supported by the SDK container  # noqa: E501

        :return: The sdkcontainerusername of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._sdkcontainerusername

    @sdkcontainerusername.setter
    def sdkcontainerusername(self, sdkcontainerusername):
        """Sets the sdkcontainerusername of this Platform.

        ssh user supported by the SDK container  # noqa: E501

        :param sdkcontainerusername: The sdkcontainerusername of this Platform.  # noqa: E501
        :type sdkcontainerusername: str
        """

        self._sdkcontainerusername = sdkcontainerusername

    @property
    def sdkcontainerpassword(self):
        """Gets the sdkcontainerpassword of this Platform.  # noqa: E501

        password used to ssh inside the SDK container  # noqa: E501

        :return: The sdkcontainerpassword of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._sdkcontainerpassword

    @sdkcontainerpassword.setter
    def sdkcontainerpassword(self, sdkcontainerpassword):
        """Sets the sdkcontainerpassword of this Platform.

        password used to ssh inside the SDK container  # noqa: E501

        :param sdkcontainerpassword: The sdkcontainerpassword of this Platform.  # noqa: E501
        :type sdkcontainerpassword: str
        """

        self._sdkcontainerpassword = sdkcontainerpassword

    @property
    def dockercomposefile(self):
        """Gets the dockercomposefile of this Platform.  # noqa: E501

        path of docker-compose file to be used to start additional containers needed by the app  # noqa: E501

        :return: The dockercomposefile of this Platform.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._dockercomposefile

    @dockercomposefile.setter
    def dockercomposefile(self, dockercomposefile):
        """Sets the dockercomposefile of this Platform.

        path of docker-compose file to be used to start additional containers needed by the app  # noqa: E501

        :param dockercomposefile: The dockercomposefile of this Platform.  # noqa: E501
        :type dockercomposefile: dict(str, str)
        """

        self._dockercomposefile = dockercomposefile

    @property
    def startupscript(self):
        """Gets the startupscript of this Platform.  # noqa: E501

        path of script to be run when application debugging starts  # noqa: E501

        :return: The startupscript of this Platform.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._startupscript

    @startupscript.setter
    def startupscript(self, startupscript):
        """Sets the startupscript of this Platform.

        path of script to be run when application debugging starts  # noqa: E501

        :param startupscript: The startupscript of this Platform.  # noqa: E501
        :type startupscript: dict(str, str)
        """

        self._startupscript = startupscript

    @property
    def shutdownscript(self):
        """Gets the shutdownscript of this Platform.  # noqa: E501

        path of script to be run when application debugging stops  # noqa: E501

        :return: The shutdownscript of this Platform.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._shutdownscript

    @shutdownscript.setter
    def shutdownscript(self, shutdownscript):
        """Sets the shutdownscript of this Platform.

        path of script to be run when application debugging stops  # noqa: E501

        :param shutdownscript: The shutdownscript of this Platform.  # noqa: E501
        :type shutdownscript: dict(str, str)
        """

        self._shutdownscript = shutdownscript

    @property
    def ports(self):
        """Gets the ports of this Platform.  # noqa: E501

        ports to be exposed from the container  # noqa: E501

        :return: The ports of this Platform.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Platform.

        ports to be exposed from the container  # noqa: E501

        :param ports: The ports of this Platform.  # noqa: E501
        :type ports: dict(str, dict(str, str))
        """

        self._ports = ports

    @property
    def volumes(self):
        """Gets the volumes of this Platform.  # noqa: E501

        Local folders to be mounted as mount points inside a container  # noqa: E501

        :return: The volumes of this Platform.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Platform.

        Local folders to be mounted as mount points inside a container  # noqa: E501

        :param volumes: The volumes of this Platform.  # noqa: E501
        :type volumes: dict(str, dict(str, str))
        """

        self._volumes = volumes

    @property
    def devices(self):
        """Gets the devices of this Platform.  # noqa: E501

        Additional devices to be shared inside container  # noqa: E501

        :return: The devices of this Platform.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this Platform.

        Additional devices to be shared inside container  # noqa: E501

        :param devices: The devices of this Platform.  # noqa: E501
        :type devices: dict(str, list[str])
        """

        self._devices = devices

    @property
    def networks(self):
        """Gets the networks of this Platform.  # noqa: E501

        Networks used by container (in debug it will always be also on bridge)  # noqa: E501

        :return: The networks of this Platform.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this Platform.

        Networks used by container (in debug it will always be also on bridge)  # noqa: E501

        :param networks: The networks of this Platform.  # noqa: E501
        :type networks: dict(str, list[str])
        """

        self._networks = networks

    @property
    def extraparms(self):
        """Gets the extraparms of this Platform.  # noqa: E501

        Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)  # noqa: E501

        :return: The extraparms of this Platform.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._extraparms

    @extraparms.setter
    def extraparms(self, extraparms):
        """Sets the extraparms of this Platform.

        Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)  # noqa: E501

        :param extraparms: The extraparms of this Platform.  # noqa: E501
        :type extraparms: dict(str, dict(str, object))
        """

        self._extraparms = extraparms

    @property
    def props(self):
        """Gets the props of this Platform.  # noqa: E501

        Custom properties (may be used in dockerfile or by extensions)  # noqa: E501

        :return: The props of this Platform.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this Platform.

        Custom properties (may be used in dockerfile or by extensions)  # noqa: E501

        :param props: The props of this Platform.  # noqa: E501
        :type props: dict(str, dict(str, str))
        """

        self._props = props

    @property
    def description(self):
        """Gets the description of this Platform.  # noqa: E501

        Platform human-readable description  # noqa: E501

        :return: The description of this Platform.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Platform.

        Platform human-readable description  # noqa: E501

        :param description: The description of this Platform.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Platform.  # noqa: E501

        strings used to identify specific properties of the platform  # noqa: E501

        :return: The tags of this Platform.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Platform.

        strings used to identify specific properties of the platform  # noqa: E501

        :param tags: The tags of this Platform.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Platform):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Platform):
            return True

        return self.to_dict() != other.to_dict()
