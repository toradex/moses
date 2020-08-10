# Platform

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique name (should be filesystem-compatible) | [optional] [readonly] 
**name** | **str** | Platform mnemnonic name | [optional] [readonly] 
**standard** | **bool** | true if the platform is provided by Toradex and can&#39;t be modified | [optional] [readonly] 
**version** | **str** | Version of the image (not related to distro version) | [optional] [readonly] 
**runtimes** | **list[str]** | runtimes/languages supported by the container | [optional] 
**sdkcontainerusername** | **str** | ssh user supported by the SDK container | [optional] 
**sdkcontainerpassword** | **str** | password used to ssh inside the SDK container | [optional] 
**dockercomposefile** | **dict(str, str)** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**startupscript** | **dict(str, str)** | path of script to be run when application debugging starts | [optional] 
**shutdownscript** | **dict(str, str)** | path of script to be run when application debugging stops | [optional] 
**ports** | **dict(str, dict(str, str))** | ports to be exposed from the container | [optional] 
**volumes** | **dict(str, dict(str, str))** | Local folders to be mounted as mount points inside a container | [optional] 
**devices** | **dict(str, list[str])** | Additional devices to be shared inside container | [optional] 
**networks** | **dict(str, list[str])** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**extraparms** | **dict(str, dict(str, object))** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**props** | **dict(str, dict(str, str))** | Custom properties (may be used in dockerfile or by extensions) | [optional] 
**description** | **str** | Platform human-readable description | [optional] [readonly] 
**tags** | **list[str]** | strings used to identify specific properties of the platform | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


