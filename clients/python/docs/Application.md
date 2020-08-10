# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id | [optional] [readonly] 
**platformid** | **str** | id of the platform used to generate this application configuration | [optional] [readonly] 
**folder** | **str** | folder where application configuration and extra files are stored | [optional] [readonly] 
**props** | **dict(str, dict(str, str))** | Custom application properties | [optional] 
**dockercomposefile** | **dict(str, str)** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**startupscript** | **dict(str, str)** | path of script to be run when application debugging starts | [optional] 
**shutdownscript** | **dict(str, str)** | path of script to be run when application debugging stops | [optional] 
**ports** | **dict(str, dict(str, str))** | ports to be exposed from the container | [optional] 
**volumes** | **dict(str, dict(str, str))** | Local folders to be mounted \&quot;A mount points inside a container | [optional] 
**devices** | **dict(str, list[str])** | Additional devices to be shared inside container | [optional] 
**networks** | **dict(str, list[str])** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**extraparms** | **dict(str, dict(str, str))** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**username** | **str** | user account used to run the application inside the container | [optional] 
**images** | **dict(str, str)** | SHA-ids of the debug and release images | [optional] 
**sdkimages** | **dict(str, str)** | SHA-ids of the debug and release SDK images | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


