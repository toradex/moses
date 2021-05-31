# moses_client.PlatformsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_compatibledevices_get**](PlatformsApi.md#platform_compatibledevices_get) | **GET** /platforms/{platform_id}/compatibledevices | Get compatible devices
[**platform_get**](PlatformsApi.md#platform_get) | **GET** /platforms/{platform_id} | Get detailed information about a platform
[**platforms_get**](PlatformsApi.md#platforms_get) | **GET** /platforms | Get all platforms


# **platform_compatibledevices_get**
> [TargetDevice] platform_compatibledevices_get(platform_id)

Get compatible devices

Return a list of devices that are compatible with the platform

### Example

```python
import time
import moses_client
from moses_client.api import platforms_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = platforms_api.PlatformsApi(api_client)
    platform_id = "zA9LCSLv1C1ylmgd0.Y2TA_TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SpQR..OCvg" # str | Id of a platform formatted as name_version

    # example passing only required values which don't have defaults set
    try:
        # Get compatible devices
        api_response = api_instance.platform_compatibledevices_get(platform_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling PlatformsApi->platform_compatibledevices_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**| Id of a platform formatted as name_version |

### Return type

[**[TargetDevice]**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of devices |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get**
> Platform platform_get(platform_id)

Get detailed information about a platform

Return data about a specific platform

### Example

```python
import time
import moses_client
from moses_client.api import platforms_api
from moses_client.model.platform import Platform
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
    api_instance = platforms_api.PlatformsApi(api_client)
    platform_id = "zA9LCSLv1C1ylmgd0.Y2TA_TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SpQR..OCvg" # str | Id of a platform formatted as name_version

    # example passing only required values which don't have defaults set
    try:
        # Get detailed information about a platform
        api_response = api_instance.platform_get(platform_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling PlatformsApi->platform_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**| Id of a platform formatted as name_version |

### Return type

[**Platform**](Platform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Platform information |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_get**
> [Platform] platforms_get()

Get all platforms

Return all configured platforms

### Example

```python
import time
import moses_client
from moses_client.api import platforms_api
from moses_client.model.platform import Platform
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
    api_instance = platforms_api.PlatformsApi(api_client)
    runtime = "runtime_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all platforms
        api_response = api_instance.platforms_get(runtime=runtime)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling PlatformsApi->platforms_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime** | **str**|  | [optional]

### Return type

[**[Platform]**](Platform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Platforms |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

