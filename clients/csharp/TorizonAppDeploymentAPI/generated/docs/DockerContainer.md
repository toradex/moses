
# TorizonRestAPI.Model.DockerContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | The ID of the container | [optional] 
**Created** | **string** | The time the container was created | [optional] 
**Path** | **string** | The path to the command being run | [optional] 
**Args** | **List&lt;string&gt;** | The arguments to the command being run | [optional] 
**State** | [**DockerContainerState**](DockerContainerState.md) |  | [optional] 
**Image** | **string** | The container&#39;s image | [optional] 
**ResolvConfPath** | **string** |  | [optional] 
**HostnamePath** | **string** |  | [optional] 
**HostsPath** | **string** |  | [optional] 
**LogPath** | **string** |  | [optional] 
**Node** | [**Object**](.md) | TODO | [optional] 
**Name** | **string** |  | [optional] 
**RestartCount** | **int** |  | [optional] 
**Driver** | **string** |  | [optional] 
**MountLabel** | **string** |  | [optional] 
**ProcessLabel** | **string** |  | [optional] 
**AppArmorProfile** | **string** |  | [optional] 
**ExecIDs** | **List&lt;string&gt;** |  | [optional] 
**HostConfig** | [**DockerHostConfig**](DockerHostConfig.md) |  | [optional] 
**GraphDriver** | [**DockerGraphDriverData**](DockerGraphDriverData.md) |  | [optional] 
**SizeRw** | **long** | The size of files that have been created or changed by this container. | [optional] 
**SizeRootFs** | **long** | The total size of all the files in this container. | [optional] 
**Mounts** | [**List&lt;DockerMountPoint&gt;**](DockerMountPoint.md) |  | [optional] 
**Config** | [**DockerContainerConfig**](DockerContainerConfig.md) |  | [optional] 
**NetworkSettings** | [**DockerNetworkSettings**](DockerNetworkSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

