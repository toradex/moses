# TorizonRestAPI.Api.PlatformsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PlatformCompatibledevicesGet**](PlatformsApi.md#platformcompatibledevicesget) | **GET** /platforms/{platform_id}/compatibledevices | Get compatible devices
[**PlatformGet**](PlatformsApi.md#platformget) | **GET** /platforms/{platform_id} | Get detailed information about a platform
[**PlatformsGet**](PlatformsApi.md#platformsget) | **GET** /platforms | Get all platforms



## PlatformCompatibledevicesGet

> List&lt;TargetDevice&gt; PlatformCompatibledevicesGet (string platformId)

Get compatible devices

Return a list of devices that are compatible with the platform

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class PlatformCompatibledevicesGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new PlatformsApi(Configuration.Default);
            var platformId = platformId_example;  // string | Id of a platform formatted as name_version

            try
            {
                // Get compatible devices
                List<TargetDevice> result = apiInstance.PlatformCompatibledevicesGet(platformId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling PlatformsApi.PlatformCompatibledevicesGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platformId** | **string**| Id of a platform formatted as name_version | 

### Return type

[**List&lt;TargetDevice&gt;**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of devices |  -  |
| **404** | Platform not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PlatformGet

> Platform PlatformGet (string platformId)

Get detailed information about a platform

Return data about a specific platform

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class PlatformGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new PlatformsApi(Configuration.Default);
            var platformId = platformId_example;  // string | Id of a platform formatted as name_version

            try
            {
                // Get detailed information about a platform
                Platform result = apiInstance.PlatformGet(platformId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling PlatformsApi.PlatformGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platformId** | **string**| Id of a platform formatted as name_version | 

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
| **200** | Platform information |  -  |
| **404** | Platform not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PlatformsGet

> List&lt;Platform&gt; PlatformsGet (string runtime = null)

Get all platforms

Return all configured platforms

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class PlatformsGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new PlatformsApi(Configuration.Default);
            var runtime = runtime_example;  // string |  (optional) 

            try
            {
                // Get all platforms
                List<Platform> result = apiInstance.PlatformsGet(runtime);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling PlatformsApi.PlatformsGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime** | **string**|  | [optional] 

### Return type

[**List&lt;Platform&gt;**](Platform.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Platforms |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

