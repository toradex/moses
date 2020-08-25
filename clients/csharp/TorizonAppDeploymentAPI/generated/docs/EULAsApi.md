# TorizonRestAPI.Api.EULAsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**EulaModify**](EULAsApi.md#eulamodify) | **PUT** /eulas/{eula_id} | Change eula properties



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
            var apiInstance = new EULAsApi(Configuration.Default);
            var eulaId = eulaId_example;  // string | Id of an eula
            var e = new Eula(); // Eula |  (optional) 

            try
            {
                // Change eula properties
                Eula result = apiInstance.EulaModify(eulaId, e);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling EULAsApi.EulaModify: " + e.Message );
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
 **eulaId** | **string**| Id of an eula | 
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
| **200** | Returns eula |  -  |
| **404** | eula not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

