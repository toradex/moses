# moses_client.VersionApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_docker**](VersionApi.md#version_docker) | **GET** /version/docker | Docker version info
[**version_get**](VersionApi.md#version_get) | **GET** /version | APP/API version


# **version_docker**
> DockerVersion version_docker()

Docker version info

Return docker version information

### Example


```python
import time
import moses_client
from moses_client.api import version_api
from moses_client.model.docker_version import DockerVersion
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
    api_instance = version_api.VersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Docker version info
        api_response = api_instance.version_docker()
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling VersionApi->version_docker: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DockerVersion**](DockerVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_get**
> bool, date, datetime, dict, float, int, list, str, none_type version_get()

APP/API version

Return app and API version

### Example


```python
import time
import moses_client
from moses_client.api import version_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = version_api.VersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # APP/API version
        api_response = api_instance.version_get()
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling VersionApi->version_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

