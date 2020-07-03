# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class MemInfo(object):
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
        'total': 'float',
        'available': 'float',
        'free': 'float'
    }

    attribute_map = {
        'total': 'total',
        'available': 'available',
        'free': 'free'
    }

    def __init__(self, total=None, available=None, free=None, local_vars_configuration=None):  # noqa: E501
        """MemInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._available = None
        self._free = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if available is not None:
            self.available = available
        if free is not None:
            self.free = free

    @property
    def total(self):
        """Gets the total of this MemInfo.  # noqa: E501

        total memory in kb  # noqa: E501

        :return: The total of this MemInfo.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MemInfo.

        total memory in kb  # noqa: E501

        :param total: The total of this MemInfo.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def available(self):
        """Gets the available of this MemInfo.  # noqa: E501

        available memory in kb  # noqa: E501

        :return: The available of this MemInfo.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this MemInfo.

        available memory in kb  # noqa: E501

        :param available: The available of this MemInfo.  # noqa: E501
        :type: float
        """

        self._available = available

    @property
    def free(self):
        """Gets the free of this MemInfo.  # noqa: E501

        free memory in kb  # noqa: E501

        :return: The free of this MemInfo.  # noqa: E501
        :rtype: float
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this MemInfo.

        free memory in kb  # noqa: E501

        :param free: The free of this MemInfo.  # noqa: E501
        :type: float
        """

        self._free = free

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
        if not isinstance(other, MemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemInfo):
            return True

        return self.to_dict() != other.to_dict()
