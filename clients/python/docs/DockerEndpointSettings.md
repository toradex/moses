# DockerEndpointSettings

Configuration for a network endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipam_config** | [**DockerEndpointIPAMConfig**](DockerEndpointIPAMConfig.md) |  | [optional] 
**links** | **list[str]** |  | [optional] 
**aliases** | **list[str]** |  | [optional] 
**network_id** | **str** | Unique ID of the network.  | [optional] 
**endpoint_id** | **str** | Unique ID for the service endpoint in a Sandbox.  | [optional] 
**gateway** | **str** | Gateway address for this network.  | [optional] 
**ip_address** | **str** | IPv4 address.  | [optional] 
**ip_prefix_len** | **int** | Mask length of the IPv4 address.  | [optional] 
**i_pv6_gateway** | **str** | IPv6 gateway address.  | [optional] 
**global_i_pv6_address** | **str** | Global IPv6 address.  | [optional] 
**global_i_pv6_prefix_len** | **int** | Mask length of the global IPv6 address.  | [optional] 
**mac_address** | **str** | MAC address for the endpoint on this network.  | [optional] 
**driver_opts** | **dict(str, str)** | DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


