# TorizonRestAPI.Api.ProgressApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ProgressCreate**](ProgressApi.md#progresscreate) | **GET** /progress/create | Create a progress cookie
[**ProgressDelete**](ProgressApi.md#progressdelete) | **GET** /progress/delete | Releases a progress cookie
[**ProgressStatus**](ProgressApi.md#progressstatus) | **GET** /progress/status | Retrieves progress status of an operation



## ProgressCreate

> Progress ProgressCreate ()

Create a progress cookie

Creates a progress object that could be used to monitor and abort operations. A progress cookie must be used only for one operation and deleted when the operation is completed/terminated. Passing cookies to different operations may lead to unpredictable results.

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
                // Create a progress cookie
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
| **200** | Progress Cookie Information |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProgressDelete

> void ProgressDelete (string progressId = null)

Releases a progress cookie

Delete the cookie. If the operation is pending this will cause an abort. Abort may not be immediate. After the delete operation is called the progress cookie id is no longer valid and further calls to progress_status will fail.

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
            var progressId = "progressId_example";  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Releases a progress cookie
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

Retrieves progress status of an operation

Return the operation status, progress and messages, it's blocking until status changes or the operation is completed/terminated. Not all operations can return detailed progress information (it may not be possible to estimate it before starting the actual operation), it's anyway granted that an operation will report its completition/failure.

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
            var progressId = "progressId_example";  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Retrieves progress status of an operation
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
| **200** | Progress Cookie Information |  -  |
| **404** | Object not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

