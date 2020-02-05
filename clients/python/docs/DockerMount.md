# DockerMount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | Container path. | [optional] 
**source** | **str** | Mount source (e.g. a volume name, a host path). | [optional] 
**type** | **str** | The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs.  | [optional] 
**read_only** | **bool** | Whether the mount should be read-only. | [optional] 
**consistency** | **str** | The consistency requirement for the mount: &#x60;default&#x60;, &#x60;consistent&#x60;, &#x60;cached&#x60;, or &#x60;delegated&#x60;. | [optional] 
**bind_options** | [**DockerMountBindOptions**](DockerMountBindOptions.md) |  | [optional] 
**volume_options** | [**DockerMountVolumeOptions**](DockerMountVolumeOptions.md) |  | [optional] 
**tmpfs_options** | [**DockerMountTmpfsOptions**](DockerMountTmpfsOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


