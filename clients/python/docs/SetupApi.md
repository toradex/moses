# moses_client.SetupApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setup_enableemulation**](SetupApi.md#setup_enableemulation) | **GET** /setup/enableemulation | enables ARM emulation using qemu
[**setup_pullcontainers**](SetupApi.md#setup_pullcontainers) | **GET** /setup/pullcontainers | pulls containers from docker repo


# **setup_enableemulation**
> setup_enableemulation(progress_id=progress_id)

enables ARM emulation using qemu

uses binfmt and qemu to enable ARM emulation on non-ARM devices

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
    api_instance = moses_client.SetupApi(api_client)
    progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # enables ARM emulation using qemu
        api_instance.setup_enableemulation(progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling SetupApi->setup_enableemulation: %s\n" % e)
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
**200** | Emulation enabled |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_pullcontainers**
> setup_pullcontainers(progress_id=progress_id)

pulls containers from docker repo

installs base and sdk containers for supported platforms

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
    api_instance = moses_client.SetupApi(api_client)
    progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # pulls containers from docker repo
        api_instance.setup_pullcontainers(progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling SetupApi->setup_pullcontainers: %s\n" % e)
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
**200** | Containers pulled |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |
**542** | Error pulling images from docker registry. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

