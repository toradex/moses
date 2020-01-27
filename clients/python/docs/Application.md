# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id | [optional] [readonly] 
**platformid** | **str** | id of the platform used to generate this application configuration | [optional] [readonly] 
**folder** | **str** | folder where application configuration and extra files are stored | [optional] [readonly] 
**props** | **dict(str, dict(str, str))** |  | [optional] 
**dockercomposefile** | **dict(str, str)** |  | [optional] 
**startupscript** | **dict(str, str)** |  | [optional] 
**shutdownscript** | **dict(str, str)** |  | [optional] 
**ports** | **dict(str, dict(str, str))** |  | [optional] 
**volumes** | **dict(str, dict(str, str))** |  | [optional] 
**devices** | **dict(str, list[str])** |  | [optional] 
**networks** | **dict(str, list[str])** |  | [optional] 
**extraparms** | **dict(str, dict(str, object))** |  | [optional] 
**username** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


