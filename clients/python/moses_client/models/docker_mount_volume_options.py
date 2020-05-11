# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerMountVolumeOptions(object):
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
        'no_copy': 'bool',
        'labels': 'dict(str, str)',
        'driver_config': 'DockerMountVolumeOptionsDriverConfig'
    }

    attribute_map = {
        'no_copy': 'NoCopy',
        'labels': 'Labels',
        'driver_config': 'DriverConfig'
    }

    def __init__(self, no_copy=False, labels=None, driver_config=None, local_vars_configuration=None):  # noqa: E501
        """DockerMountVolumeOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._no_copy = None
        self._labels = None
        self._driver_config = None
        self.discriminator = None

        if no_copy is not None:
            self.no_copy = no_copy
        if labels is not None:
            self.labels = labels
        if driver_config is not None:
            self.driver_config = driver_config

    @property
    def no_copy(self):
        """Gets the no_copy of this DockerMountVolumeOptions.  # noqa: E501

        Populate volume with data from the target.  # noqa: E501

        :return: The no_copy of this DockerMountVolumeOptions.  # noqa: E501
        :rtype: bool
        """
        return self._no_copy

    @no_copy.setter
    def no_copy(self, no_copy):
        """Sets the no_copy of this DockerMountVolumeOptions.

        Populate volume with data from the target.  # noqa: E501

        :param no_copy: The no_copy of this DockerMountVolumeOptions.  # noqa: E501
        :type: bool
        """

        self._no_copy = no_copy

    @property
    def labels(self):
        """Gets the labels of this DockerMountVolumeOptions.  # noqa: E501

        User-defined key/value metadata.  # noqa: E501

        :return: The labels of this DockerMountVolumeOptions.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DockerMountVolumeOptions.

        User-defined key/value metadata.  # noqa: E501

        :param labels: The labels of this DockerMountVolumeOptions.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def driver_config(self):
        """Gets the driver_config of this DockerMountVolumeOptions.  # noqa: E501


        :return: The driver_config of this DockerMountVolumeOptions.  # noqa: E501
        :rtype: DockerMountVolumeOptionsDriverConfig
        """
        return self._driver_config

    @driver_config.setter
    def driver_config(self, driver_config):
        """Sets the driver_config of this DockerMountVolumeOptions.


        :param driver_config: The driver_config of this DockerMountVolumeOptions.  # noqa: E501
        :type: DockerMountVolumeOptionsDriverConfig
        """

        self._driver_config = driver_config

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
        if not isinstance(other, DockerMountVolumeOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerMountVolumeOptions):
            return True

        return self.to_dict() != other.to_dict()
