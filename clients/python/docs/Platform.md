# Platform


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique name (should be filesystem-compatible) | [optional] [readonly] 
**name** | **str** | Platform mnemnonic name | [optional] [readonly] 
**standard** | **bool** | true if the platform is provided by Toradex and can&#39;t be modified | [optional] [readonly] 
**version** | **str** | Version of the image (not related to distro version) | [optional] [readonly] 
**runtimes** | **[str]** | runtimes/languages supported by the container | [optional] 
**sdkcontainerusername** | **str** | ssh user supported by the SDK container | [optional] 
**sdkcontainerpassword** | **str** | password used to ssh inside the SDK container | [optional] 
**dockercomposefile** | **{str: (str,)}** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**startupscript** | **{str: (str,)}** | path of script to be run when application debugging starts | [optional] 
**shutdownscript** | **{str: (str,)}** | path of script to be run when application debugging stops | [optional] 
**ports** | **{str: ({str: (str,)},)}** | ports to be exposed from the container | [optional] 
**volumes** | **{str: ({str: (str,)},)}** | Local folders to be mounted as mount points inside a container | [optional] 
**devices** | **{str: ([str],)}** | Additional devices to be shared inside container | [optional] 
**networks** | **{str: ([str],)}** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**extraparms** | **{str: ({str: (str,)},)}** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**props** | **{str: ({str: (str,)},)}** | Custom properties (may be used in dockerfile or by extensions) | [optional] 
**description** | **str** | Platform human-readable description | [optional] [readonly] 
**tags** | **[str]** | strings used to identify specific properties of the platform | [optional] [readonly] 
**architecture** | **str** | architecture as defined by docker | [optional] [readonly] 
**deprecated** | **bool** | true for platforms that are no longer supported | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


