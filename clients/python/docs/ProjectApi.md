# moses_client.ProjectApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_build**](ProjectApi.md#project_build) | **GET** /project/build | Builds a project using torizoncore-builder


# **project_build**
> Application project_build(project_path, clean_build, generate_installer_image, generate_ota_update, output_dir=output_dir)

Builds a project using torizoncore-builder

This operation can be used to build a project. The IDE backend will take care of running torizoncore-builder container.

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.ProjectApi(api_client)
    project_path = 'project_path_example' # str | 
clean_build = True # bool | 
generate_installer_image = True # bool | 
generate_ota_update = True # bool | 
output_dir = 'output_dir_example' # str |  (optional)

    try:
        # Builds a project using torizoncore-builder
        api_response = api_instance.project_build(project_path, clean_build, generate_installer_image, generate_ota_update, output_dir=output_dir)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_path** | **str**|  | 
 **clean_build** | **bool**|  | 
 **generate_installer_image** | **bool**|  | 
 **generate_ota_update** | **bool**|  | 
 **output_dir** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an application |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**540** | Invalid path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

