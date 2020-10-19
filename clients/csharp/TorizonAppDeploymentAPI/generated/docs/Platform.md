
# TorizonRestAPI.Model.Platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique name (should be filesystem-compatible) | [optional] [readonly] 
**Name** | **string** | Platform mnemnonic name | [optional] [readonly] 
**Standard** | **bool** | true if the platform is provided by Toradex and can&#39;t be modified | [optional] [readonly] 
**Version** | **string** | Version of the image (not related to distro version) | [optional] [readonly] 
**Runtimes** | **List&lt;string&gt;** | runtimes/languages supported by the container | [optional] 
**Sdkcontainerusername** | **string** | ssh user supported by the SDK container | [optional] 
**Sdkcontainerpassword** | **string** | password used to ssh inside the SDK container | [optional] 
**Dockercomposefile** | **Dictionary&lt;string, string&gt;** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**Startupscript** | **Dictionary&lt;string, string&gt;** | path of script to be run when application debugging starts | [optional] 
**Shutdownscript** | **Dictionary&lt;string, string&gt;** | path of script to be run when application debugging stops | [optional] 
**Ports** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | ports to be exposed from the container | [optional] 
**Volumes** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | Local folders to be mounted as mount points inside a container | [optional] 
**Devices** | **Dictionary&lt;string, List&lt;string&gt;&gt;** | Additional devices to be shared inside container | [optional] 
**Networks** | **Dictionary&lt;string, List&lt;string&gt;&gt;** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**Extraparms** | **Dictionary&lt;string, Dictionary&lt;string, Object&gt;&gt;** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**Props** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | Custom properties (may be used in dockerfile or by extensions) | [optional] 
**Description** | **string** | Platform human-readable description | [optional] [readonly] 
**Tags** | **List&lt;string&gt;** | strings used to identify specific properties of the platform | [optional] [readonly] 
**Architecture** | **string** | architecture as defined by docker | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

