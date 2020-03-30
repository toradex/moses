
# TorizonRestAPI.Model.DockerEndpointSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IPAMConfig** | [**DockerEndpointIPAMConfig**](DockerEndpointIPAMConfig.md) |  | [optional] 
**Links** | **List&lt;string&gt;** |  | [optional] 
**Aliases** | **List&lt;string&gt;** |  | [optional] 
**NetworkID** | **string** | Unique ID of the network.  | [optional] 
**EndpointID** | **string** | Unique ID for the service endpoint in a Sandbox.  | [optional] 
**Gateway** | **string** | Gateway address for this network.  | [optional] 
**IPAddress** | **string** | IPv4 address.  | [optional] 
**IPPrefixLen** | **int** | Mask length of the IPv4 address.  | [optional] 
**IPv6Gateway** | **string** | IPv6 gateway address.  | [optional] 
**GlobalIPv6Address** | **string** | Global IPv6 address.  | [optional] 
**GlobalIPv6PrefixLen** | **long** | Mask length of the global IPv6 address.  | [optional] 
**MacAddress** | **string** | MAC address for the endpoint on this network.  | [optional] 
**DriverOpts** | **Dictionary&lt;string, string&gt;** | DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

