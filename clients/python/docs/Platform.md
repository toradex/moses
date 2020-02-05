# Platform

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique name (including version) | [optional] [readonly] 
**name** | **str** | Platform mnemnonic name | [optional] [readonly] 
**standard** | **bool** | true if the platform is provided by Toradex and can&#39;t be modified | [optional] [readonly] 
**version** | **str** | Version of the image (not related to distro version) | [optional] [readonly] 
**runtimes** | **list[str]** |  | [optional] 
**sdkcontainerusername** | **str** |  | [optional] 
**sdkcontainerpassword** | **str** |  | [optional] 
**dockercomposefile** | **dict(str, str)** |  | [optional] 
**startupscript** | **dict(str, str)** |  | [optional] 
**shutdownscript** | **dict(str, str)** |  | [optional] 
**ports** | **dict(str, dict(str, str))** |  | [optional] 
**volumes** | **dict(str, dict(str, str))** |  | [optional] 
**devices** | **dict(str, list[str])** |  | [optional] 
**networks** | **dict(str, list[str])** |  | [optional] 
**extraparms** | **dict(str, dict(str, object))** |  | [optional] 
**props** | **dict(str, dict(str, str))** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


