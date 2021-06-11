
# TorizonRestAPI.Model.TargetDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique serial number | [optional] [readonly] 
**Name** | **string** | Device mnemnonic name | [optional] 
**Model** | **string** | Device hardware ID | [optional] [readonly] 
**Hwrev** | **string** | Device hardware revision | [optional] [readonly] 
**Kernelversion** | **string** | Kernel name | [optional] [readonly] 
**Kernelrelease** | **string** | Kernel release | [optional] [readonly] 
**Distroversion** | **string** | Torizon version (date) | [optional] [readonly] 
**Hostname** | **string** | Device host name | [optional] 
**Username** | **string** | User account used to connect to device via ssh | [optional] 
**Homefolder** | **string** | Home folder of ssh user (used to deploy files and apps, can be different from actual home) | [optional] 
**Runningtorizon** | **bool** | True for a target device that is a community device, false for default Toradex devices | [optional] 
**CpuArchitecture** | **string** | CPU architecture | [optional] 
**ModelDescription** | **string** | detailed model description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

