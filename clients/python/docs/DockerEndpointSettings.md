# DockerEndpointSettings

Configuration for a network endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipam_config** | [**DockerEndpointIPAMConfig**](DockerEndpointIPAMConfig.md) |  | [optional] 
**links** | **[str]** |  | [optional] 
**aliases** | **[str]** |  | [optional] 
**network_id** | **str** | Unique ID of the network.  | [optional] 
**endpoint_id** | **str** | Unique ID for the service endpoint in a Sandbox.  | [optional] 
**gateway** | **str** | Gateway address for this network.  | [optional] 
**ip_address** | **str** | IPv4 address.  | [optional] 
**ip_prefix_len** | **int** | Mask length of the IPv4 address.  | [optional] 
**ipv6_gateway** | **str** | IPv6 gateway address.  | [optional] 
**global_ipv6_address** | **str** | Global IPv6 address.  | [optional] 
**global_ipv6_prefix_len** | **int** | Mask length of the global IPv6 address.  | [optional] 
**mac_address** | **str** | MAC address for the endpoint on this network.  | [optional] 
**driver_opts** | **{str: (str,)}, none_type** | DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


