
# TorizonRestAPI.Model.Platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique name (including version) | [optional] [readonly] 
**Name** | **string** | Platform mnemnonic name | [optional] [readonly] 
**Standard** | **bool** | true if the platform is provided by Toradex and can&#39;t be modified | [optional] [readonly] 
**Version** | **string** | Version of the image (not related to distro version) | [optional] [readonly] 
**Runtimes** | **List&lt;string&gt;** |  | [optional] 
**Sdkcontainerusername** | **string** |  | [optional] 
**Sdkcontainerpassword** | **string** |  | [optional] 
**Dockercomposefile** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Startupscript** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Shutdownscript** | **Dictionary&lt;string, string&gt;** |  | [optional] 
**Ports** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Volumes** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 
**Devices** | **Dictionary&lt;string, List&lt;string&gt;&gt;** |  | [optional] 
**Networks** | **Dictionary&lt;string, List&lt;string&gt;&gt;** |  | [optional] 
**Extraparms** | **Dictionary&lt;string, Dictionary&lt;string, Object&gt;&gt;** |  | [optional] 
**Props** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

