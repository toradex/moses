# TorizonRestAPI.Api.ProjectApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ProjectBuild**](ProjectApi.md#projectbuild) | **GET** /project/build | Builds a project using torizoncore-builder



## ProjectBuild

> Application ProjectBuild (string projectPath, bool cleanBuild, bool generateInstallerImage, bool generateOtaUpdate, string outputDir = null)

Builds a project using torizoncore-builder

This operation can be used to build a project. The IDE backend will take care of running torizoncore-builder container.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ProjectBuildExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ProjectApi(Configuration.Default);
            var projectPath = projectPath_example;  // string | 
            var cleanBuild = true;  // bool | 
            var generateInstallerImage = true;  // bool | 
            var generateOtaUpdate = true;  // bool | 
            var outputDir = outputDir_example;  // string |  (optional) 

            try
            {
                // Builds a project using torizoncore-builder
                Application result = apiInstance.ProjectBuild(projectPath, cleanBuild, generateInstallerImage, generateOtaUpdate, outputDir);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ProjectApi.ProjectBuild: " + e.Message );
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
 **projectPath** | **string**|  | 
 **cleanBuild** | **bool**|  | 
 **generateInstallerImage** | **bool**|  | 
 **generateOtaUpdate** | **bool**|  | 
 **outputDir** | **string**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an application |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **540** | Invalid path. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

