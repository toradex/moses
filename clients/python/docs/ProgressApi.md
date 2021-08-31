# moses_client.ProgressApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**progress_create**](ProgressApi.md#progress_create) | **GET** /progress/create | Create a progress cookie
[**progress_delete**](ProgressApi.md#progress_delete) | **GET** /progress/delete | Releases a progress cookie
[**progress_status**](ProgressApi.md#progress_status) | **GET** /progress/status | Retrieves progress status of an operation


# **progress_create**
> Progress progress_create()

Create a progress cookie

Creates a progress object that could be used to monitor and abort operations. A progress cookie must be used only for one operation and deleted when the operation is completed/terminated. Passing cookies to different operations may lead to unpredictable results.

### Example


```python
import time
import moses_client
from moses_client.api import progress_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.progress import Progress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = progress_api.ProgressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a progress cookie
        api_response = api_instance.progress_create()
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Progress Cookie Information |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress_delete**
> progress_delete()

Releases a progress cookie

Delete the cookie. If the operation is pending this will cause an abort. Abort may not be immediate. After the delete operation is called the progress cookie id is no longer valid and further calls to progress_status will fail.

### Example


```python
import time
import moses_client
from moses_client.api import progress_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = progress_api.ProgressApi(api_client)
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Releases a progress cookie
        api_instance.progress_delete(progress_id=progress_id)
    except moses_client.ApiException as e:
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
> Progress progress_status()

Retrieves progress status of an operation

Return the operation status, progress and messages, it's blocking until status changes or the operation is completed/terminated. Not all operations can return detailed progress information (it may not be possible to estimate it before starting the actual operation), it's anyway granted that an operation will report its completition/failure.

### Example


```python
import time
import moses_client
from moses_client.api import progress_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.progress import Progress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = progress_api.ProgressApi(api_client)
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves progress status of an operation
        api_response = api_instance.progress_status(progress_id=progress_id)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Progress Cookie Information |  -  |
**404** | Object not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

