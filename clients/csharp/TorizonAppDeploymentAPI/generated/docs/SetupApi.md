# TorizonRestAPI.Api.SetupApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SetupPullcontainers**](SetupApi.md#setuppullcontainers) | **GET** /setup/pullcontainers | pulls containers from docker repo



## SetupPullcontainers

> void SetupPullcontainers ()

pulls containers from docker repo

installs base and sdk containers for supported platforms

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class SetupPullcontainersExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new SetupApi(Configuration.Default);

            try
            {
                // pulls containers from docker repo
                apiInstance.SetupPullcontainers();
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling SetupApi.SetupPullcontainers: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
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
| **200** | Sysroot updated |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |
| **542** | Error pulling images from docker registry. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

