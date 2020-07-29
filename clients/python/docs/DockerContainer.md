# DockerContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the container | [optional] 
**created** | **str** | The time the container was created | [optional] 
**path** | **str** | The path to the command being run | [optional] 
**args** | **list[str]** | The arguments to the command being run | [optional] 
**state** | [**DockerContainerState**](DockerContainerState.md) |  | [optional] 
**image** | **str** | The container&#39;s image | [optional] 
**resolv_conf_path** | **str** |  | [optional] 
**hostname_path** | **str** |  | [optional] 
**hosts_path** | **str** |  | [optional] 
**log_path** | **str** |  | [optional] 
**node** | **object** | TODO | [optional] 
**name** | **str** |  | [optional] 
**restart_count** | **int** |  | [optional] 
**driver** | **str** |  | [optional] 
**mount_label** | **str** |  | [optional] 
**process_label** | **str** |  | [optional] 
**app_armor_profile** | **str** |  | [optional] 
**exec_i_ds** | **list[str]** |  | [optional] 
**host_config** | [**DockerHostConfig**](DockerHostConfig.md) |  | [optional] 
**graph_driver** | [**DockerGraphDriverData**](DockerGraphDriverData.md) |  | [optional] 
**size_rw** | **int** | The size of files that have been created or changed by this container. | [optional] 
**size_root_fs** | **int** | The total size of all the files in this container. | [optional] 
**mounts** | [**list[DockerMountPoint]**](DockerMountPoint.md) |  | [optional] 
**config** | [**DockerContainerConfig**](DockerContainerConfig.md) |  | [optional] 
**network_settings** | [**DockerNetworkSettings**](DockerNetworkSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


