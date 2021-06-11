# TargetDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique serial number | [optional] [readonly] 
**name** | **str** | Device mnemnonic name | [optional] 
**model** | **str** | Device hardware ID | [optional] [readonly] 
**hwrev** | **str** | Device hardware revision | [optional] [readonly] 
**kernelversion** | **str** | Kernel name | [optional] [readonly] 
**kernelrelease** | **str** | Kernel release | [optional] [readonly] 
**distroversion** | **str** | Torizon version (date) | [optional] [readonly] 
**hostname** | **str** | Device host name | [optional] 
**username** | **str** | User account used to connect to device via ssh | [optional] 
**homefolder** | **str** | Home folder of ssh user (used to deploy files and apps, can be different from actual home) | [optional] 
**runningtorizon** | **bool** | True for a target device that is a community device, false for default Toradex devices | [optional] 
**cpu_architecture** | **str** | CPU architecture | [optional] 
**model_description** | **str** | detailed model description | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


