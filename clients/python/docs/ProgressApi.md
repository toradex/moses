# moses_client.ProgressApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**progress_create**](ProgressApi.md#progress_create) | **GET** /progress/create | 
[**progress_delete**](ProgressApi.md#progress_delete) | **GET** /progress/delete | 
[**progress_status**](ProgressApi.md#progress_status) | **GET** /progress/status | 


# **progress_create**
> Progress progress_create()



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
    api_instance = moses_client.ProgressApi(api_client)
    
    try:
        api_response = api_instance.progress_create()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgressApi->progress_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Progress**](Progress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns new empty object |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress_delete**
> progress_delete(progress_id=progress_id)



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
    api_instance = moses_client.ProgressApi(api_client)
    progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        api_instance.progress_delete(progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling ProgressApi->progress_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **progress_id** | **str**| Id of a progress cookie (uuid) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress_status**
> Progress progress_status(progress_id=progress_id)



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
    api_instance = moses_client.ProgressApi(api_client)
    progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        api_response = api_instance.progress_status(progress_id=progress_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgressApi->progress_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **progress_id** | **str**| Id of a progress cookie (uuid) | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return object with up to date information |  -  |
**404** | Object not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

