# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerThrottleDevice(object):
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
        'path': 'str',
        'rate': 'int'
    }

    attribute_map = {
        'path': 'Path',
        'rate': 'Rate'
    }

    def __init__(self, path=None, rate=None, local_vars_configuration=None):  # noqa: E501
        """DockerThrottleDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._rate = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if rate is not None:
            self.rate = rate

    @property
    def path(self):
        """Gets the path of this DockerThrottleDevice.  # noqa: E501

        Device path  # noqa: E501

        :return: The path of this DockerThrottleDevice.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DockerThrottleDevice.

        Device path  # noqa: E501

        :param path: The path of this DockerThrottleDevice.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def rate(self):
        """Gets the rate of this DockerThrottleDevice.  # noqa: E501

        Rate  # noqa: E501

        :return: The rate of this DockerThrottleDevice.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this DockerThrottleDevice.

        Rate  # noqa: E501

        :param rate: The rate of this DockerThrottleDevice.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                rate is not None and rate < 0):  # noqa: E501
            raise ValueError("Invalid value for `rate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._rate = rate

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
        if not isinstance(other, DockerThrottleDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerThrottleDevice):
            return True

        return self.to_dict() != other.to_dict()
