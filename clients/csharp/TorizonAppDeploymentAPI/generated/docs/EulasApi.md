# TorizonRestAPI.Api.EulasApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**EulaGet**](EulasApi.md#eulaget) | **GET** /eulas/{eula_id} | Get detail about an eula
[**EulaModify**](EulasApi.md#eulamodify) | **PUT** /eulas/{eula_id} | Change eula properties
[**EulasGet**](EulasApi.md#eulasget) | **GET** /eulas | Get all eulas



## EulaGet

> Eula EulaGet (string eulaId)

Get detail about an eula

Return detailed information about a specific eula

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class EulaGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new EulasApi(Configuration.Default);
            var eulaId = eulaId_example;  // string | Id of an Eula

            try
            {
                // Get detail about an eula
                Eula result = apiInstance.EulaGet(eulaId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling EulasApi.EulaGet: " + e.Message );
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
 **eulaId** | **string**| Id of an Eula | 

### Return type

[**Eula**](Eula.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Eula Information |  -  |
| **404** | Eula not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EulaModify

> Eula EulaModify (string eulaId, Eula e = null)

Change eula properties

Set eula as visualized and/or accepted

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class EulaModifyExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new EulasApi(Configuration.Default);
            var eulaId = eulaId_example;  // string | Id of an Eula
            var e = new Eula(); // Eula |  (optional) 

            try
            {
                // Change eula properties
                Eula result = apiInstance.EulaModify(eulaId, e);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling EulasApi.EulaModify: " + e.Message );
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
 **eulaId** | **string**| Id of an Eula | 
 **e** | [**Eula**](Eula.md)|  | [optional] 

### Return type

[**Eula**](Eula.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Eula information |  -  |
| **404** | Eula not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EulasGet

> List&lt;Eula&gt; EulasGet ()

Get all eulas

Returns information about all eulas required to run different platforms on the system

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class EulasGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new EulasApi(Configuration.Default);

            try
            {
                // Get all eulas
                List<Eula> result = apiInstance.EulasGet();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling EulasApi.EulasGet: " + e.Message );
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

[**List&lt;Eula&gt;**](Eula.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Eulas |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

