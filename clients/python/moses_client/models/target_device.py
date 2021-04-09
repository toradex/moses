# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class TargetDevice(object):
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
        'model': 'str',
        'hwrev': 'str',
        'kernelversion': 'str',
        'kernelrelease': 'str',
        'distroversion': 'str',
        'hostname': 'str',
        'username': 'str',
        'homefolder': 'str',
        'runningtorizon': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'model': 'model',
        'hwrev': 'hwrev',
        'kernelversion': 'kernelversion',
        'kernelrelease': 'kernelrelease',
        'distroversion': 'distroversion',
        'hostname': 'hostname',
        'username': 'username',
        'homefolder': 'homefolder',
        'runningtorizon': 'runningtorizon'
    }

    def __init__(self, id=None, name=None, model=None, hwrev=None, kernelversion=None, kernelrelease=None, distroversion=None, hostname=None, username=None, homefolder=None, runningtorizon=None, local_vars_configuration=None):  # noqa: E501
        """TargetDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._model = None
        self._hwrev = None
        self._kernelversion = None
        self._kernelrelease = None
        self._distroversion = None
        self._hostname = None
        self._username = None
        self._homefolder = None
        self._runningtorizon = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if hwrev is not None:
            self.hwrev = hwrev
        if kernelversion is not None:
            self.kernelversion = kernelversion
        if kernelrelease is not None:
            self.kernelrelease = kernelrelease
        if distroversion is not None:
            self.distroversion = distroversion
        if hostname is not None:
            self.hostname = hostname
        if username is not None:
            self.username = username
        if homefolder is not None:
            self.homefolder = homefolder
        if runningtorizon is not None:
            self.runningtorizon = runningtorizon

    @property
    def id(self):
        """Gets the id of this TargetDevice.  # noqa: E501

        Unique serial number  # noqa: E501

        :return: The id of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetDevice.

        Unique serial number  # noqa: E501

        :param id: The id of this TargetDevice.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TargetDevice.  # noqa: E501

        Device mnemnonic name  # noqa: E501

        :return: The name of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetDevice.

        Device mnemnonic name  # noqa: E501

        :param name: The name of this TargetDevice.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def model(self):
        """Gets the model of this TargetDevice.  # noqa: E501

        Device hardware ID  # noqa: E501

        :return: The model of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TargetDevice.

        Device hardware ID  # noqa: E501

        :param model: The model of this TargetDevice.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def hwrev(self):
        """Gets the hwrev of this TargetDevice.  # noqa: E501

        Device hardware revision  # noqa: E501

        :return: The hwrev of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._hwrev

    @hwrev.setter
    def hwrev(self, hwrev):
        """Sets the hwrev of this TargetDevice.

        Device hardware revision  # noqa: E501

        :param hwrev: The hwrev of this TargetDevice.  # noqa: E501
        :type hwrev: str
        """

        self._hwrev = hwrev

    @property
    def kernelversion(self):
        """Gets the kernelversion of this TargetDevice.  # noqa: E501

        Kernel name  # noqa: E501

        :return: The kernelversion of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._kernelversion

    @kernelversion.setter
    def kernelversion(self, kernelversion):
        """Sets the kernelversion of this TargetDevice.

        Kernel name  # noqa: E501

        :param kernelversion: The kernelversion of this TargetDevice.  # noqa: E501
        :type kernelversion: str
        """

        self._kernelversion = kernelversion

    @property
    def kernelrelease(self):
        """Gets the kernelrelease of this TargetDevice.  # noqa: E501

        Kernel release  # noqa: E501

        :return: The kernelrelease of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._kernelrelease

    @kernelrelease.setter
    def kernelrelease(self, kernelrelease):
        """Sets the kernelrelease of this TargetDevice.

        Kernel release  # noqa: E501

        :param kernelrelease: The kernelrelease of this TargetDevice.  # noqa: E501
        :type kernelrelease: str
        """

        self._kernelrelease = kernelrelease

    @property
    def distroversion(self):
        """Gets the distroversion of this TargetDevice.  # noqa: E501

        Torizon version (date)  # noqa: E501

        :return: The distroversion of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._distroversion

    @distroversion.setter
    def distroversion(self, distroversion):
        """Sets the distroversion of this TargetDevice.

        Torizon version (date)  # noqa: E501

        :param distroversion: The distroversion of this TargetDevice.  # noqa: E501
        :type distroversion: str
        """

        self._distroversion = distroversion

    @property
    def hostname(self):
        """Gets the hostname of this TargetDevice.  # noqa: E501

        Device host name  # noqa: E501

        :return: The hostname of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TargetDevice.

        Device host name  # noqa: E501

        :param hostname: The hostname of this TargetDevice.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def username(self):
        """Gets the username of this TargetDevice.  # noqa: E501

        User account used to connect to device via ssh  # noqa: E501

        :return: The username of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TargetDevice.

        User account used to connect to device via ssh  # noqa: E501

        :param username: The username of this TargetDevice.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def homefolder(self):
        """Gets the homefolder of this TargetDevice.  # noqa: E501

        Home folder of ssh user (used to deploy files and apps, can be different from actual home)  # noqa: E501

        :return: The homefolder of this TargetDevice.  # noqa: E501
        :rtype: str
        """
        return self._homefolder

    @homefolder.setter
    def homefolder(self, homefolder):
        """Sets the homefolder of this TargetDevice.

        Home folder of ssh user (used to deploy files and apps, can be different from actual home)  # noqa: E501

        :param homefolder: The homefolder of this TargetDevice.  # noqa: E501
        :type homefolder: str
        """

        self._homefolder = homefolder

    @property
    def runningtorizon(self):
        """Gets the runningtorizon of this TargetDevice.  # noqa: E501

        True for a target device that is a community device, false for default Toradex devices  # noqa: E501

        :return: The runningtorizon of this TargetDevice.  # noqa: E501
        :rtype: bool
        """
        return self._runningtorizon

    @runningtorizon.setter
    def runningtorizon(self, runningtorizon):
        """Sets the runningtorizon of this TargetDevice.

        True for a target device that is a community device, false for default Toradex devices  # noqa: E501

        :param runningtorizon: The runningtorizon of this TargetDevice.  # noqa: E501
        :type runningtorizon: bool
        """

        self._runningtorizon = runningtorizon

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
        if not isinstance(other, TargetDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetDevice):
            return True

        return self.to_dict() != other.to_dict()
