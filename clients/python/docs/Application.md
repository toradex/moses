# Application


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id | [optional] [readonly] 
**platformid** | **str** | id of the platform used to generate this application configuration | [optional] [readonly] 
**folder** | **str** | folder where application configuration and extra files are stored | [optional] [readonly] 
**props** | **{str: ({str: (str,)},)}** | Custom application properties | [optional] 
**dockercomposefile** | **{str: (str,)}** | path of docker-compose file to be used to start additional containers needed by the app | [optional] 
**startupscript** | **{str: (str,)}** | path of script to be run when application debugging starts | [optional] 
**shutdownscript** | **{str: (str,)}** | path of script to be run when application debugging stops | [optional] 
**ports** | **{str: ({str: (str,)},)}** | ports to be exposed from the container | [optional] 
**volumes** | **{str: ({str: (str,)},)}** | Local folders to be mounted \&quot;A mount points inside a container | [optional] 
**devices** | **{str: ([str],)}** | Additional devices to be shared inside container | [optional] 
**networks** | **{str: ([str],)}** | Networks used by container (in debug it will always be also on bridge) | [optional] 
**extraparms** | **{str: ({str: (str,)},)}** | Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML) | [optional] 
**username** | **str** | user account used to run the application inside the container | [optional] 
**images** | **{str: (str,)}** | SHA-ids of the debug and release images | [optional] 
**sdkimages** | **{str: (str,)}** | SHA-ids of the debug and release SDK images | [optional] 
**imagetags** | **{str: (str,)}** | unique tag used for the images | [optional] 
**sdkimagetags** | **{str: (str,)}** | unique tag used for the SDK images (if application uses an SDK) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


