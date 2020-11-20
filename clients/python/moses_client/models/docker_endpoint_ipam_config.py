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


class DockerEndpointIPAMConfig(object):
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
        'i_pv4_address': 'str',
        'i_pv6_address': 'str',
        'link_local_i_ps': 'list[str]'
    }

    attribute_map = {
        'i_pv4_address': 'IPv4Address',
        'i_pv6_address': 'IPv6Address',
        'link_local_i_ps': 'LinkLocalIPs'
    }

    def __init__(self, i_pv4_address=None, i_pv6_address=None, link_local_i_ps=None, local_vars_configuration=None):  # noqa: E501
        """DockerEndpointIPAMConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._i_pv4_address = None
        self._i_pv6_address = None
        self._link_local_i_ps = None
        self.discriminator = None

        if i_pv4_address is not None:
            self.i_pv4_address = i_pv4_address
        if i_pv6_address is not None:
            self.i_pv6_address = i_pv6_address
        if link_local_i_ps is not None:
            self.link_local_i_ps = link_local_i_ps

    @property
    def i_pv4_address(self):
        """Gets the i_pv4_address of this DockerEndpointIPAMConfig.  # noqa: E501


        :return: The i_pv4_address of this DockerEndpointIPAMConfig.  # noqa: E501
        :rtype: str
        """
        return self._i_pv4_address

    @i_pv4_address.setter
    def i_pv4_address(self, i_pv4_address):
        """Sets the i_pv4_address of this DockerEndpointIPAMConfig.


        :param i_pv4_address: The i_pv4_address of this DockerEndpointIPAMConfig.  # noqa: E501
        :type i_pv4_address: str
        """

        self._i_pv4_address = i_pv4_address

    @property
    def i_pv6_address(self):
        """Gets the i_pv6_address of this DockerEndpointIPAMConfig.  # noqa: E501


        :return: The i_pv6_address of this DockerEndpointIPAMConfig.  # noqa: E501
        :rtype: str
        """
        return self._i_pv6_address

    @i_pv6_address.setter
    def i_pv6_address(self, i_pv6_address):
        """Sets the i_pv6_address of this DockerEndpointIPAMConfig.


        :param i_pv6_address: The i_pv6_address of this DockerEndpointIPAMConfig.  # noqa: E501
        :type i_pv6_address: str
        """

        self._i_pv6_address = i_pv6_address

    @property
    def link_local_i_ps(self):
        """Gets the link_local_i_ps of this DockerEndpointIPAMConfig.  # noqa: E501


        :return: The link_local_i_ps of this DockerEndpointIPAMConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._link_local_i_ps

    @link_local_i_ps.setter
    def link_local_i_ps(self, link_local_i_ps):
        """Sets the link_local_i_ps of this DockerEndpointIPAMConfig.


        :param link_local_i_ps: The link_local_i_ps of this DockerEndpointIPAMConfig.  # noqa: E501
        :type link_local_i_ps: list[str]
        """

        self._link_local_i_ps = link_local_i_ps

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
        if not isinstance(other, DockerEndpointIPAMConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerEndpointIPAMConfig):
            return True

        return self.to_dict() != other.to_dict()
