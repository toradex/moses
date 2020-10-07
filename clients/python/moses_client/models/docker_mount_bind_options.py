# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerMountBindOptions(object):
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
        'propagation': 'str'
    }

    attribute_map = {
        'propagation': 'Propagation'
    }

    def __init__(self, propagation=None, local_vars_configuration=None):  # noqa: E501
        """DockerMountBindOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._propagation = None
        self.discriminator = None

        if propagation is not None:
            self.propagation = propagation

    @property
    def propagation(self):
        """Gets the propagation of this DockerMountBindOptions.  # noqa: E501

        A propagation mode with the value `[r]private`, `[r]shared`, or `[r]slave`.  # noqa: E501

        :return: The propagation of this DockerMountBindOptions.  # noqa: E501
        :rtype: str
        """
        return self._propagation

    @propagation.setter
    def propagation(self, propagation):
        """Sets the propagation of this DockerMountBindOptions.

        A propagation mode with the value `[r]private`, `[r]shared`, or `[r]slave`.  # noqa: E501

        :param propagation: The propagation of this DockerMountBindOptions.  # noqa: E501
        :type propagation: str
        """
        allowed_values = ["private", "rprivate", "shared", "rshared", "slave", "rslave"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and propagation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `propagation` ({0}), must be one of {1}"  # noqa: E501
                .format(propagation, allowed_values)
            )

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
        if not isinstance(other, DockerMountBindOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerMountBindOptions):
            return True

        return self.to_dict() != other.to_dict()
