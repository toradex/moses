# moses_client.PlatformsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_compatibledevices_get**](PlatformsApi.md#platform_compatibledevices_get) | **GET** /platforms/{platform_id}/compatibledevices | get compatible devices
[**platform_get**](PlatformsApi.md#platform_get) | **GET** /platforms/{platform_id} | Get a platform
[**platforms_get**](PlatformsApi.md#platforms_get) | **GET** /platforms | Get all platforms


# **platform_compatibledevices_get**
> list[TargetDevice] platform_compatibledevices_get(platform_id)

get compatible devices

Returns a list of devices that are compatible with the platform

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = moses_client.PlatformsApi()
platform_id = 'platform_id_example' # str | Id of a platform formatted as name_version

try:
    # get compatible devices
    api_response = api_instance.platform_compatibledevices_get(platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformsApi->platform_compatibledevices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**| Id of a platform formatted as name_version | 

### Return type

[**list[TargetDevice]**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of devices |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get**
> Platform platform_get(platform_id)

Get a platform

Returns data about a specific platform

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = moses_client.PlatformsApi()
platform_id = 'platform_id_example' # str | Id of a platform formatted as name_version

try:
    # Get a platform
    api_response = api_instance.platform_get(platform_id)
    pprint(api_response)
except ApiException as e:
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
**200** | Returns a platform |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_get**
> list[Platform] platforms_get(runtime=runtime)

Get all platforms

Returns all configured platforms

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = moses_client.PlatformsApi()
runtime = 'runtime_example' # str |  (optional)

try:
    # Get all platforms
    api_response = api_instance.platforms_get(runtime=runtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformsApi->platforms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime** | **str**|  | [optional] 

### Return type

[**list[Platform]**](Platform.md)

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

