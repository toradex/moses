# moses_client.SetupApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setup_pullcontainers**](SetupApi.md#setup_pullcontainers) | **GET** /setup/pullcontainers | pulls containers from docker repo


# **setup_pullcontainers**
> setup_pullcontainers()

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
    
    try:
        # pulls containers from docker repo
        api_instance.setup_pullcontainers()
    except ApiException as e:
        print("Exception when calling SetupApi->setup_pullcontainers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Sysroot updated |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |
**542** | Error pulling images from docker registry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

