
# TorizonRestAPI.Model.Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique id | [optional] [readonly] 
**Platformid** | **string** | id of the platform used to generate this application configuration | [optional] [readonly] 
**Folder** | **string** | folder where application configuration and extra files are stored | [optional] [readonly] 
**Props** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Dockercomposefile** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Startupscript** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Shutdownscript** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Ports** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Volumes** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Devices** | **Dictionary&lt;string, List&lt;string&gt;&gt;** |  | [optional] 
**Networks** | **Dictionary&lt;string, List&lt;string&gt;&gt;** |  | [optional] 
**Extraparms** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Username** | **string** |  | [optional] 
**Images** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Sdkimages** | **Dictionary&lt;string, string&gt;** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

