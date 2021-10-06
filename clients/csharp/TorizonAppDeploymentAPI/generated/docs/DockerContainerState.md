
# TorizonRestAPI.Model.DockerContainerState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;.  | [optional] 
**Running** | **bool** | Whether this container is running.  Note that a running container can be _paused_. The &#x60;Running&#x60; and &#x60;Paused&#x60; booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both &#x60;Running&#x60; _and_ &#x60;Paused&#x60;.  Use the &#x60;Status&#x60; field instead to determine if a container&#39;s state is \&quot;running\&quot;.  | [optional] 
**Paused** | **bool** | Whether this container is paused. | [optional] 
**Restarting** | **bool** | Whether this container is restarting. | [optional] 
**OOMKilled** | **bool** | Whether this container has been killed because it ran out of memory. | [optional] 
**Dead** | **bool** |  | [optional] 
**Pid** | **int** | The process ID of this container | [optional] 
**ExitCode** | **int** | The last e code of this container | [optional] 
**Error** | **string** |  | [optional] 
**StartedAt** | **string** | The time when this container was last started. | [optional] 
**FinishedAt** | **string** | The time when this container last exited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

