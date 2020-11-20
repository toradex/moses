# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class MountPoint(object):
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
        'mountpoint': 'str',
        'filesystem': 'str',
        'size': 'int',
        'available': 'int'
    }

    attribute_map = {
        'mountpoint': 'mountpoint',
        'filesystem': 'filesystem',
        'size': 'size',
        'available': 'available'
    }

    def __init__(self, mountpoint=None, filesystem=None, size=None, available=None, local_vars_configuration=None):  # noqa: E501
        """MountPoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mountpoint = None
        self._filesystem = None
        self._size = None
        self._available = None
        self.discriminator = None

        if mountpoint is not None:
            self.mountpoint = mountpoint
        if filesystem is not None:
            self.filesystem = filesystem
        if size is not None:
            self.size = size
        if available is not None:
            self.available = available

    @property
    def mountpoint(self):
        """Gets the mountpoint of this MountPoint.  # noqa: E501

        mount point  # noqa: E501

        :return: The mountpoint of this MountPoint.  # noqa: E501
        :rtype: str
        """
        return self._mountpoint

    @mountpoint.setter
    def mountpoint(self, mountpoint):
        """Sets the mountpoint of this MountPoint.

        mount point  # noqa: E501

        :param mountpoint: The mountpoint of this MountPoint.  # noqa: E501
        :type mountpoint: str
        """

        self._mountpoint = mountpoint

    @property
    def filesystem(self):
        """Gets the filesystem of this MountPoint.  # noqa: E501

        file system  # noqa: E501

        :return: The filesystem of this MountPoint.  # noqa: E501
        :rtype: str
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this MountPoint.

        file system  # noqa: E501

        :param filesystem: The filesystem of this MountPoint.  # noqa: E501
        :type filesystem: str
        """

        self._filesystem = filesystem

    @property
    def size(self):
        """Gets the size of this MountPoint.  # noqa: E501

        total size in 1Kb blocks  # noqa: E501

        :return: The size of this MountPoint.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MountPoint.

        total size in 1Kb blocks  # noqa: E501

        :param size: The size of this MountPoint.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def available(self):
        """Gets the available of this MountPoint.  # noqa: E501

        available space in 1kb blocks  # noqa: E501

        :return: The available of this MountPoint.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this MountPoint.

        available space in 1kb blocks  # noqa: E501

        :param available: The available of this MountPoint.  # noqa: E501
        :type available: int
        """

        self._available = available

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
        if not isinstance(other, MountPoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MountPoint):
            return True

        return self.to_dict() != other.to_dict()
