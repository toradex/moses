# TorizonRestAPI.Api.ProgressApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ProgressCreate**](ProgressApi.md#progresscreate) | **GET** /progress/create | 
[**ProgressDelete**](ProgressApi.md#progressdelete) | **GET** /progress/delete | 
[**ProgressStatus**](ProgressApi.md#progressstatus) | **GET** /progress/status | 



## ProgressCreate

> Progress ProgressCreate ()



### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ProgressCreateExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ProgressApi(Configuration.Default);

            try
            {
                Progress result = apiInstance.ProgressCreate();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ProgressApi.ProgressCreate: " + e.Message );
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

[**Progress**](Progress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns new empty object |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProgressDelete

> void ProgressDelete (string progressId = null)



### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ProgressDeleteExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ProgressApi(Configuration.Default);
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                apiInstance.ProgressDelete(progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ProgressApi.ProgressDelete: " + e.Message );
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
 **progressId** | **string**| Id of a progress cookie (uuid) | [optional] 

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
| **200** | OK |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProgressStatus

> Progress ProgressStatus (string progressId = null)



### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ProgressStatusExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ProgressApi(Configuration.Default);
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                Progress result = apiInstance.ProgressStatus(progressId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ProgressApi.ProgressStatus: " + e.Message );
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
 **progressId** | **string**| Id of a progress cookie (uuid) | [optional] 

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
| **200** | return object with up to date information |  -  |
| **404** | Object not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

