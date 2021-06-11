# DockerMountVolumeOptions

Optional configuration for the `volume` type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_copy** | **bool** | Populate volume with data from the target. | [optional]  if omitted the server will use the default value of False
**labels** | **{str: (str,)}** | User-defined key/value metadata. | [optional] 
**driver_config** | [**DockerMountVolumeOptionsDriverConfig**](DockerMountVolumeOptionsDriverConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


