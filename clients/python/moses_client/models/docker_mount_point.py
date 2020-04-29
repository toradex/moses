# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerMountPoint(object):
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
        'type': 'str',
        'name': 'str',
        'source': 'str',
        'destination': 'str',
        'driver': 'str',
        'mode': 'str',
        'rw': 'bool',
        'propagation': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'name': 'Name',
        'source': 'Source',
        'destination': 'Destination',
        'driver': 'Driver',
        'mode': 'Mode',
        'rw': 'RW',
        'propagation': 'Propagation'
    }

    def __init__(self, type=None, name=None, source=None, destination=None, driver=None, mode=None, rw=None, propagation=None, local_vars_configuration=None):  # noqa: E501
        """DockerMountPoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._source = None
        self._destination = None
        self._driver = None
        self._mode = None
        self._rw = None
        self._propagation = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if driver is not None:
            self.driver = driver
        if mode is not None:
            self.mode = mode
        if rw is not None:
            self.rw = rw
        if propagation is not None:
            self.propagation = propagation

    @property
    def type(self):
        """Gets the type of this DockerMountPoint.  # noqa: E501


        :return: The type of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DockerMountPoint.


        :param type: The type of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this DockerMountPoint.  # noqa: E501


        :return: The name of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DockerMountPoint.


        :param name: The name of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source(self):
        """Gets the source of this DockerMountPoint.  # noqa: E501


        :return: The source of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DockerMountPoint.


        :param source: The source of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this DockerMountPoint.  # noqa: E501


        :return: The destination of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DockerMountPoint.


        :param destination: The destination of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def driver(self):
        """Gets the driver of this DockerMountPoint.  # noqa: E501


        :return: The driver of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this DockerMountPoint.


        :param driver: The driver of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def mode(self):
        """Gets the mode of this DockerMountPoint.  # noqa: E501


        :return: The mode of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DockerMountPoint.


        :param mode: The mode of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def rw(self):
        """Gets the rw of this DockerMountPoint.  # noqa: E501


        :return: The rw of this DockerMountPoint.  # noqa: E501
        :rtype: bool
        """
        return self._rw

    @rw.setter
    def rw(self, rw):
        """Sets the rw of this DockerMountPoint.


        :param rw: The rw of this DockerMountPoint.  # noqa: E501
        :type: bool
        """

        self._rw = rw

    @property
    def propagation(self):
        """Gets the propagation of this DockerMountPoint.  # noqa: E501


        :return: The propagation of this DockerMountPoint.  # noqa: E501
        :rtype: str
        """
        return self._propagation

    @propagation.setter
    def propagation(self, propagation):
        """Sets the propagation of this DockerMountPoint.


        :param propagation: The propagation of this DockerMountPoint.  # noqa: E501
        :type: str
        """

        self._propagation = propagation

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
        if not isinstance(other, DockerMountPoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerMountPoint):
            return True

        return self.to_dict() != other.to_dict()
