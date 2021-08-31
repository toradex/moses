
# TorizonRestAPI.Model.Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique id | [optional] [readonly] 
**Platformid** | **string** | id of the platform used to generate this application configuration | [optional] [readonly] 
**Folder** | **string** | folder where application configuration and extra files are stored | [optional] [readonly] 
**Props** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | Custom application properties | [optional] 
**Dockercomposefile** | **Dictionary&lt;string, string&gt;** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**Startupscript** | **Dictionary&lt;string, string&gt;** | path of script to be run when application debugging starts | [optional] 
**Shutdownscript** | **Dictionary&lt;string, string&gt;** | path of script to be run when application debugging stops | [optional] 
**Ports** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | ports to be exposed from the container | [optional] 
**Volumes** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | Local folders to be mounted \&quot;A mount points inside a container | [optional] 
**Devices** | **Dictionary&lt;string, List&lt;string&gt;&gt;** | Additional devices to be shared inside container | [optional] 
**Networks** | **Dictionary&lt;string, List&lt;string&gt;&gt;** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**Extraparms** | **Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt;** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**Username** | **string** | user account used to run the application inside the container | [optional] 
**Images** | **Dictionary&lt;string, string&gt;** | SHA-ids of the debug and release images | [optional] 
**Sdkimages** | **Dictionary&lt;string, string&gt;** | SHA-ids of the debug and release SDK images | [optional] 
**Imagetags** | **Dictionary&lt;string, string&gt;** | unique tag used for the images | [optional] 
**Sdkimagetags** | **Dictionary&lt;string, string&gt;** | unique tag used for the SDK images (if application uses an SDK) | [optional] 
**Otapackagename** | **string** | name of the OTA package | [optional] 
**Otapackageversion** | **string** | version of the OTA package | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

