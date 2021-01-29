# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerNetworkSettings(object):
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
        'bridge': 'str',
        'sandbox_id': 'str',
        'hairpin_mode': 'bool',
        'link_local_i_pv6_address': 'str',
        'link_local_i_pv6_prefix_len': 'int',
        'ports': 'dict(str, list[DockerPortBinding])',
        'sandbox_key': 'str',
        'secondary_ip_addresses': 'list[DockerAddress]',
        'secondary_i_pv6_addresses': 'list[DockerAddress]',
        'endpoint_id': 'str',
        'gateway': 'str',
        'global_i_pv6_address': 'str',
        'global_i_pv6_prefix_len': 'int',
        'ip_address': 'str',
        'ip_prefix_len': 'int',
        'i_pv6_gateway': 'str',
        'mac_address': 'str',
        'networks': 'dict(str, DockerEndpointSettings)'
    }

    attribute_map = {
        'bridge': 'Bridge',
        'sandbox_id': 'SandboxID',
        'hairpin_mode': 'HairpinMode',
        'link_local_i_pv6_address': 'LinkLocalIPv6Address',
        'link_local_i_pv6_prefix_len': 'LinkLocalIPv6PrefixLen',
        'ports': 'Ports',
        'sandbox_key': 'SandboxKey',
        'secondary_ip_addresses': 'SecondaryIPAddresses',
        'secondary_i_pv6_addresses': 'SecondaryIPv6Addresses',
        'endpoint_id': 'EndpointID',
        'gateway': 'Gateway',
        'global_i_pv6_address': 'GlobalIPv6Address',
        'global_i_pv6_prefix_len': 'GlobalIPv6PrefixLen',
        'ip_address': 'IPAddress',
        'ip_prefix_len': 'IPPrefixLen',
        'i_pv6_gateway': 'IPv6Gateway',
        'mac_address': 'MacAddress',
        'networks': 'Networks'
    }

    def __init__(self, bridge=None, sandbox_id=None, hairpin_mode=None, link_local_i_pv6_address=None, link_local_i_pv6_prefix_len=None, ports=None, sandbox_key=None, secondary_ip_addresses=None, secondary_i_pv6_addresses=None, endpoint_id=None, gateway=None, global_i_pv6_address=None, global_i_pv6_prefix_len=None, ip_address=None, ip_prefix_len=None, i_pv6_gateway=None, mac_address=None, networks=None, local_vars_configuration=None):  # noqa: E501
        """DockerNetworkSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bridge = None
        self._sandbox_id = None
        self._hairpin_mode = None
        self._link_local_i_pv6_address = None
        self._link_local_i_pv6_prefix_len = None
        self._ports = None
        self._sandbox_key = None
        self._secondary_ip_addresses = None
        self._secondary_i_pv6_addresses = None
        self._endpoint_id = None
        self._gateway = None
        self._global_i_pv6_address = None
        self._global_i_pv6_prefix_len = None
        self._ip_address = None
        self._ip_prefix_len = None
        self._i_pv6_gateway = None
        self._mac_address = None
        self._networks = None
        self.discriminator = None

        if bridge is not None:
            self.bridge = bridge
        if sandbox_id is not None:
            self.sandbox_id = sandbox_id
        if hairpin_mode is not None:
            self.hairpin_mode = hairpin_mode
        if link_local_i_pv6_address is not None:
            self.link_local_i_pv6_address = link_local_i_pv6_address
        if link_local_i_pv6_prefix_len is not None:
            self.link_local_i_pv6_prefix_len = link_local_i_pv6_prefix_len
        if ports is not None:
            self.ports = ports
        if sandbox_key is not None:
            self.sandbox_key = sandbox_key
        self.secondary_ip_addresses = secondary_ip_addresses
        self.secondary_i_pv6_addresses = secondary_i_pv6_addresses
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if gateway is not None:
            self.gateway = gateway
        if global_i_pv6_address is not None:
            self.global_i_pv6_address = global_i_pv6_address
        if global_i_pv6_prefix_len is not None:
            self.global_i_pv6_prefix_len = global_i_pv6_prefix_len
        if ip_address is not None:
            self.ip_address = ip_address
        if ip_prefix_len is not None:
            self.ip_prefix_len = ip_prefix_len
        if i_pv6_gateway is not None:
            self.i_pv6_gateway = i_pv6_gateway
        if mac_address is not None:
            self.mac_address = mac_address
        if networks is not None:
            self.networks = networks

    @property
    def bridge(self):
        """Gets the bridge of this DockerNetworkSettings.  # noqa: E501

        Name of the network'a bridge (for example, `docker0`).  # noqa: E501

        :return: The bridge of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this DockerNetworkSettings.

        Name of the network'a bridge (for example, `docker0`).  # noqa: E501

        :param bridge: The bridge of this DockerNetworkSettings.  # noqa: E501
        :type bridge: str
        """

        self._bridge = bridge

    @property
    def sandbox_id(self):
        """Gets the sandbox_id of this DockerNetworkSettings.  # noqa: E501

        SandboxID uniquely represents a container's network stack.  # noqa: E501

        :return: The sandbox_id of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._sandbox_id

    @sandbox_id.setter
    def sandbox_id(self, sandbox_id):
        """Sets the sandbox_id of this DockerNetworkSettings.

        SandboxID uniquely represents a container's network stack.  # noqa: E501

        :param sandbox_id: The sandbox_id of this DockerNetworkSettings.  # noqa: E501
        :type sandbox_id: str
        """

        self._sandbox_id = sandbox_id

    @property
    def hairpin_mode(self):
        """Gets the hairpin_mode of this DockerNetworkSettings.  # noqa: E501

        Indicates if hairpin NAT should be enabled on the virtual interface.   # noqa: E501

        :return: The hairpin_mode of this DockerNetworkSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hairpin_mode

    @hairpin_mode.setter
    def hairpin_mode(self, hairpin_mode):
        """Sets the hairpin_mode of this DockerNetworkSettings.

        Indicates if hairpin NAT should be enabled on the virtual interface.   # noqa: E501

        :param hairpin_mode: The hairpin_mode of this DockerNetworkSettings.  # noqa: E501
        :type hairpin_mode: bool
        """

        self._hairpin_mode = hairpin_mode

    @property
    def link_local_i_pv6_address(self):
        """Gets the link_local_i_pv6_address of this DockerNetworkSettings.  # noqa: E501

        IPv6 unicast address using the link-local prefix.  # noqa: E501

        :return: The link_local_i_pv6_address of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._link_local_i_pv6_address

    @link_local_i_pv6_address.setter
    def link_local_i_pv6_address(self, link_local_i_pv6_address):
        """Sets the link_local_i_pv6_address of this DockerNetworkSettings.

        IPv6 unicast address using the link-local prefix.  # noqa: E501

        :param link_local_i_pv6_address: The link_local_i_pv6_address of this DockerNetworkSettings.  # noqa: E501
        :type link_local_i_pv6_address: str
        """

        self._link_local_i_pv6_address = link_local_i_pv6_address

    @property
    def link_local_i_pv6_prefix_len(self):
        """Gets the link_local_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501

        Prefix length of the IPv6 unicast address.  # noqa: E501

        :return: The link_local_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :rtype: int
        """
        return self._link_local_i_pv6_prefix_len

    @link_local_i_pv6_prefix_len.setter
    def link_local_i_pv6_prefix_len(self, link_local_i_pv6_prefix_len):
        """Sets the link_local_i_pv6_prefix_len of this DockerNetworkSettings.

        Prefix length of the IPv6 unicast address.  # noqa: E501

        :param link_local_i_pv6_prefix_len: The link_local_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :type link_local_i_pv6_prefix_len: int
        """

        self._link_local_i_pv6_prefix_len = link_local_i_pv6_prefix_len

    @property
    def ports(self):
        """Gets the ports of this DockerNetworkSettings.  # noqa: E501

        PortMap describes the mapping of container ports to host ports, using the container's port-number and protocol as key in the format `<port>/<protocol>`, for example, `80/udp`.  If a container's port is mapped for multiple protocols, separate entries are added to the mapping table.   # noqa: E501

        :return: The ports of this DockerNetworkSettings.  # noqa: E501
        :rtype: dict(str, list[DockerPortBinding])
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this DockerNetworkSettings.

        PortMap describes the mapping of container ports to host ports, using the container's port-number and protocol as key in the format `<port>/<protocol>`, for example, `80/udp`.  If a container's port is mapped for multiple protocols, separate entries are added to the mapping table.   # noqa: E501

        :param ports: The ports of this DockerNetworkSettings.  # noqa: E501
        :type ports: dict(str, list[DockerPortBinding])
        """

        self._ports = ports

    @property
    def sandbox_key(self):
        """Gets the sandbox_key of this DockerNetworkSettings.  # noqa: E501

        SandboxKey identifies the sandbox  # noqa: E501

        :return: The sandbox_key of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._sandbox_key

    @sandbox_key.setter
    def sandbox_key(self, sandbox_key):
        """Sets the sandbox_key of this DockerNetworkSettings.

        SandboxKey identifies the sandbox  # noqa: E501

        :param sandbox_key: The sandbox_key of this DockerNetworkSettings.  # noqa: E501
        :type sandbox_key: str
        """

        self._sandbox_key = sandbox_key

    @property
    def secondary_ip_addresses(self):
        """Gets the secondary_ip_addresses of this DockerNetworkSettings.  # noqa: E501

          # noqa: E501

        :return: The secondary_ip_addresses of this DockerNetworkSettings.  # noqa: E501
        :rtype: list[DockerAddress]
        """
        return self._secondary_ip_addresses

    @secondary_ip_addresses.setter
    def secondary_ip_addresses(self, secondary_ip_addresses):
        """Sets the secondary_ip_addresses of this DockerNetworkSettings.

          # noqa: E501

        :param secondary_ip_addresses: The secondary_ip_addresses of this DockerNetworkSettings.  # noqa: E501
        :type secondary_ip_addresses: list[DockerAddress]
        """

        self._secondary_ip_addresses = secondary_ip_addresses

    @property
    def secondary_i_pv6_addresses(self):
        """Gets the secondary_i_pv6_addresses of this DockerNetworkSettings.  # noqa: E501

          # noqa: E501

        :return: The secondary_i_pv6_addresses of this DockerNetworkSettings.  # noqa: E501
        :rtype: list[DockerAddress]
        """
        return self._secondary_i_pv6_addresses

    @secondary_i_pv6_addresses.setter
    def secondary_i_pv6_addresses(self, secondary_i_pv6_addresses):
        """Sets the secondary_i_pv6_addresses of this DockerNetworkSettings.

          # noqa: E501

        :param secondary_i_pv6_addresses: The secondary_i_pv6_addresses of this DockerNetworkSettings.  # noqa: E501
        :type secondary_i_pv6_addresses: list[DockerAddress]
        """

        self._secondary_i_pv6_addresses = secondary_i_pv6_addresses

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this DockerNetworkSettings.  # noqa: E501

        EndpointID uniquely represents a service endpoint in a Sandbox.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The endpoint_id of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this DockerNetworkSettings.

        EndpointID uniquely represents a service endpoint in a Sandbox.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param endpoint_id: The endpoint_id of this DockerNetworkSettings.  # noqa: E501
        :type endpoint_id: str
        """

        self._endpoint_id = endpoint_id

    @property
    def gateway(self):
        """Gets the gateway of this DockerNetworkSettings.  # noqa: E501

        Gateway address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The gateway of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this DockerNetworkSettings.

        Gateway address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param gateway: The gateway of this DockerNetworkSettings.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def global_i_pv6_address(self):
        """Gets the global_i_pv6_address of this DockerNetworkSettings.  # noqa: E501

        Global IPv6 address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The global_i_pv6_address of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._global_i_pv6_address

    @global_i_pv6_address.setter
    def global_i_pv6_address(self, global_i_pv6_address):
        """Sets the global_i_pv6_address of this DockerNetworkSettings.

        Global IPv6 address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param global_i_pv6_address: The global_i_pv6_address of this DockerNetworkSettings.  # noqa: E501
        :type global_i_pv6_address: str
        """

        self._global_i_pv6_address = global_i_pv6_address

    @property
    def global_i_pv6_prefix_len(self):
        """Gets the global_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501

        Mask length of the global IPv6 address.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The global_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :rtype: int
        """
        return self._global_i_pv6_prefix_len

    @global_i_pv6_prefix_len.setter
    def global_i_pv6_prefix_len(self, global_i_pv6_prefix_len):
        """Sets the global_i_pv6_prefix_len of this DockerNetworkSettings.

        Mask length of the global IPv6 address.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param global_i_pv6_prefix_len: The global_i_pv6_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :type global_i_pv6_prefix_len: int
        """

        self._global_i_pv6_prefix_len = global_i_pv6_prefix_len

    @property
    def ip_address(self):
        """Gets the ip_address of this DockerNetworkSettings.  # noqa: E501

        IPv4 address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The ip_address of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DockerNetworkSettings.

        IPv4 address for the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param ip_address: The ip_address of this DockerNetworkSettings.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def ip_prefix_len(self):
        """Gets the ip_prefix_len of this DockerNetworkSettings.  # noqa: E501

        Mask length of the IPv4 address.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The ip_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :rtype: int
        """
        return self._ip_prefix_len

    @ip_prefix_len.setter
    def ip_prefix_len(self, ip_prefix_len):
        """Sets the ip_prefix_len of this DockerNetworkSettings.

        Mask length of the IPv4 address.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param ip_prefix_len: The ip_prefix_len of this DockerNetworkSettings.  # noqa: E501
        :type ip_prefix_len: int
        """

        self._ip_prefix_len = ip_prefix_len

    @property
    def i_pv6_gateway(self):
        """Gets the i_pv6_gateway of this DockerNetworkSettings.  # noqa: E501

        IPv6 gateway address for this network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The i_pv6_gateway of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._i_pv6_gateway

    @i_pv6_gateway.setter
    def i_pv6_gateway(self, i_pv6_gateway):
        """Sets the i_pv6_gateway of this DockerNetworkSettings.

        IPv6 gateway address for this network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param i_pv6_gateway: The i_pv6_gateway of this DockerNetworkSettings.  # noqa: E501
        :type i_pv6_gateway: str
        """

        self._i_pv6_gateway = i_pv6_gateway

    @property
    def mac_address(self):
        """Gets the mac_address of this DockerNetworkSettings.  # noqa: E501

        MAC address for the container on the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :return: The mac_address of this DockerNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DockerNetworkSettings.

        MAC address for the container on the default \"bridge\" network.  <p><br /></p>  > **Deprecated**: This field is only propagated when attached to the > default \"bridge\" network. Use the information from the \"bridge\" > network inside the `Networks` map instead, which contains the same > information. This field was deprecated in Docker 1.9 and is scheduled > to be removed in Docker 17.12.0   # noqa: E501

        :param mac_address: The mac_address of this DockerNetworkSettings.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def networks(self):
        """Gets the networks of this DockerNetworkSettings.  # noqa: E501

        Information about all networks that the container is connected to.   # noqa: E501

        :return: The networks of this DockerNetworkSettings.  # noqa: E501
        :rtype: dict(str, DockerEndpointSettings)
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this DockerNetworkSettings.

        Information about all networks that the container is connected to.   # noqa: E501

        :param networks: The networks of this DockerNetworkSettings.  # noqa: E501
        :type networks: dict(str, DockerEndpointSettings)
        """

        self._networks = networks

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
        if not isinstance(other, DockerNetworkSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerNetworkSettings):
            return True

        return self.to_dict() != other.to_dict()
