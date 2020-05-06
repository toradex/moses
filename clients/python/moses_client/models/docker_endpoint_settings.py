# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerEndpointSettings(object):
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
        'ipam_config': 'DockerEndpointIPAMConfig',
        'links': 'list[str]',
        'aliases': 'list[str]',
        'network_id': 'str',
        'endpoint_id': 'str',
        'gateway': 'str',
        'ip_address': 'str',
        'ip_prefix_len': 'int',
        'i_pv6_gateway': 'str',
        'global_i_pv6_address': 'str',
        'global_i_pv6_prefix_len': 'int',
        'mac_address': 'str',
        'driver_opts': 'dict(str, str)'
    }

    attribute_map = {
        'ipam_config': 'IPAMConfig',
        'links': 'Links',
        'aliases': 'Aliases',
        'network_id': 'NetworkID',
        'endpoint_id': 'EndpointID',
        'gateway': 'Gateway',
        'ip_address': 'IPAddress',
        'ip_prefix_len': 'IPPrefixLen',
        'i_pv6_gateway': 'IPv6Gateway',
        'global_i_pv6_address': 'GlobalIPv6Address',
        'global_i_pv6_prefix_len': 'GlobalIPv6PrefixLen',
        'mac_address': 'MacAddress',
        'driver_opts': 'DriverOpts'
    }

    def __init__(self, ipam_config=None, links=None, aliases=None, network_id=None, endpoint_id=None, gateway=None, ip_address=None, ip_prefix_len=None, i_pv6_gateway=None, global_i_pv6_address=None, global_i_pv6_prefix_len=None, mac_address=None, driver_opts=None, local_vars_configuration=None):  # noqa: E501
        """DockerEndpointSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ipam_config = None
        self._links = None
        self._aliases = None
        self._network_id = None
        self._endpoint_id = None
        self._gateway = None
        self._ip_address = None
        self._ip_prefix_len = None
        self._i_pv6_gateway = None
        self._global_i_pv6_address = None
        self._global_i_pv6_prefix_len = None
        self._mac_address = None
        self._driver_opts = None
        self.discriminator = None

        self.ipam_config = ipam_config
        if links is not None:
            self.links = links
        if aliases is not None:
            self.aliases = aliases
        if network_id is not None:
            self.network_id = network_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if gateway is not None:
            self.gateway = gateway
        if ip_address is not None:
            self.ip_address = ip_address
        if ip_prefix_len is not None:
            self.ip_prefix_len = ip_prefix_len
        if i_pv6_gateway is not None:
            self.i_pv6_gateway = i_pv6_gateway
        if global_i_pv6_address is not None:
            self.global_i_pv6_address = global_i_pv6_address
        if global_i_pv6_prefix_len is not None:
            self.global_i_pv6_prefix_len = global_i_pv6_prefix_len
        if mac_address is not None:
            self.mac_address = mac_address
        self.driver_opts = driver_opts

    @property
    def ipam_config(self):
        """Gets the ipam_config of this DockerEndpointSettings.  # noqa: E501


        :return: The ipam_config of this DockerEndpointSettings.  # noqa: E501
        :rtype: DockerEndpointIPAMConfig
        """
        return self._ipam_config

    @ipam_config.setter
    def ipam_config(self, ipam_config):
        """Sets the ipam_config of this DockerEndpointSettings.


        :param ipam_config: The ipam_config of this DockerEndpointSettings.  # noqa: E501
        :type: DockerEndpointIPAMConfig
        """

        self._ipam_config = ipam_config

    @property
    def links(self):
        """Gets the links of this DockerEndpointSettings.  # noqa: E501


        :return: The links of this DockerEndpointSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DockerEndpointSettings.


        :param links: The links of this DockerEndpointSettings.  # noqa: E501
        :type: list[str]
        """

        self._links = links

    @property
    def aliases(self):
        """Gets the aliases of this DockerEndpointSettings.  # noqa: E501


        :return: The aliases of this DockerEndpointSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this DockerEndpointSettings.


        :param aliases: The aliases of this DockerEndpointSettings.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def network_id(self):
        """Gets the network_id of this DockerEndpointSettings.  # noqa: E501

        Unique ID of the network.   # noqa: E501

        :return: The network_id of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this DockerEndpointSettings.

        Unique ID of the network.   # noqa: E501

        :param network_id: The network_id of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this DockerEndpointSettings.  # noqa: E501

        Unique ID for the service endpoint in a Sandbox.   # noqa: E501

        :return: The endpoint_id of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this DockerEndpointSettings.

        Unique ID for the service endpoint in a Sandbox.   # noqa: E501

        :param endpoint_id: The endpoint_id of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._endpoint_id = endpoint_id

    @property
    def gateway(self):
        """Gets the gateway of this DockerEndpointSettings.  # noqa: E501

        Gateway address for this network.   # noqa: E501

        :return: The gateway of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this DockerEndpointSettings.

        Gateway address for this network.   # noqa: E501

        :param gateway: The gateway of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_address(self):
        """Gets the ip_address of this DockerEndpointSettings.  # noqa: E501

        IPv4 address.   # noqa: E501

        :return: The ip_address of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DockerEndpointSettings.

        IPv4 address.   # noqa: E501

        :param ip_address: The ip_address of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_prefix_len(self):
        """Gets the ip_prefix_len of this DockerEndpointSettings.  # noqa: E501

        Mask length of the IPv4 address.   # noqa: E501

        :return: The ip_prefix_len of this DockerEndpointSettings.  # noqa: E501
        :rtype: int
        """
        return self._ip_prefix_len

    @ip_prefix_len.setter
    def ip_prefix_len(self, ip_prefix_len):
        """Sets the ip_prefix_len of this DockerEndpointSettings.

        Mask length of the IPv4 address.   # noqa: E501

        :param ip_prefix_len: The ip_prefix_len of this DockerEndpointSettings.  # noqa: E501
        :type: int
        """

        self._ip_prefix_len = ip_prefix_len

    @property
    def i_pv6_gateway(self):
        """Gets the i_pv6_gateway of this DockerEndpointSettings.  # noqa: E501

        IPv6 gateway address.   # noqa: E501

        :return: The i_pv6_gateway of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._i_pv6_gateway

    @i_pv6_gateway.setter
    def i_pv6_gateway(self, i_pv6_gateway):
        """Sets the i_pv6_gateway of this DockerEndpointSettings.

        IPv6 gateway address.   # noqa: E501

        :param i_pv6_gateway: The i_pv6_gateway of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._i_pv6_gateway = i_pv6_gateway

    @property
    def global_i_pv6_address(self):
        """Gets the global_i_pv6_address of this DockerEndpointSettings.  # noqa: E501

        Global IPv6 address.   # noqa: E501

        :return: The global_i_pv6_address of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._global_i_pv6_address

    @global_i_pv6_address.setter
    def global_i_pv6_address(self, global_i_pv6_address):
        """Sets the global_i_pv6_address of this DockerEndpointSettings.

        Global IPv6 address.   # noqa: E501

        :param global_i_pv6_address: The global_i_pv6_address of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._global_i_pv6_address = global_i_pv6_address

    @property
    def global_i_pv6_prefix_len(self):
        """Gets the global_i_pv6_prefix_len of this DockerEndpointSettings.  # noqa: E501

        Mask length of the global IPv6 address.   # noqa: E501

        :return: The global_i_pv6_prefix_len of this DockerEndpointSettings.  # noqa: E501
        :rtype: int
        """
        return self._global_i_pv6_prefix_len

    @global_i_pv6_prefix_len.setter
    def global_i_pv6_prefix_len(self, global_i_pv6_prefix_len):
        """Sets the global_i_pv6_prefix_len of this DockerEndpointSettings.

        Mask length of the global IPv6 address.   # noqa: E501

        :param global_i_pv6_prefix_len: The global_i_pv6_prefix_len of this DockerEndpointSettings.  # noqa: E501
        :type: int
        """

        self._global_i_pv6_prefix_len = global_i_pv6_prefix_len

    @property
    def mac_address(self):
        """Gets the mac_address of this DockerEndpointSettings.  # noqa: E501

        MAC address for the endpoint on this network.   # noqa: E501

        :return: The mac_address of this DockerEndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DockerEndpointSettings.

        MAC address for the endpoint on this network.   # noqa: E501

        :param mac_address: The mac_address of this DockerEndpointSettings.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def driver_opts(self):
        """Gets the driver_opts of this DockerEndpointSettings.  # noqa: E501

        DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific.   # noqa: E501

        :return: The driver_opts of this DockerEndpointSettings.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._driver_opts

    @driver_opts.setter
    def driver_opts(self, driver_opts):
        """Sets the driver_opts of this DockerEndpointSettings.

        DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific.   # noqa: E501

        :param driver_opts: The driver_opts of this DockerEndpointSettings.  # noqa: E501
        :type: dict(str, str)
        """

        self._driver_opts = driver_opts

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
        if not isinstance(other, DockerEndpointSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerEndpointSettings):
            return True

        return self.to_dict() != other.to_dict()
