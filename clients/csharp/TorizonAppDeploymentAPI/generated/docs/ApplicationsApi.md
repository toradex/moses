# TorizonRestAPI.Api.ApplicationsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApplicationBuild**](ApplicationsApi.md#applicationbuild) | **GET** /applications/{application_id}/build | Builds container image
[**ApplicationDelete**](ApplicationsApi.md#applicationdelete) | **DELETE** /applications/{application_id} | Remove an application and all the associated data and containers
[**ApplicationDeploy**](ApplicationsApi.md#applicationdeploy) | **GET** /applications/{application_id}/deploy | Deploys container image
[**ApplicationGet**](ApplicationsApi.md#applicationget) | **GET** /applications/{application_id} | Get application
[**ApplicationGetcontainer**](ApplicationsApi.md#applicationgetcontainer) | **GET** /applications/{application_id}/container | Get container information
[**ApplicationGetcontainerLogs**](ApplicationsApi.md#applicationgetcontainerlogs) | **GET** /applications/{application_id}/container_logs | Get container log, chunk by chunk
[**ApplicationGetdockerCommandline**](ApplicationsApi.md#applicationgetdockercommandline) | **GET** /applications/{application_id}/docker_commandline | Get docker command line used to run the container
[**ApplicationGetdockerComposefile**](ApplicationsApi.md#applicationgetdockercomposefile) | **GET** /applications/{application_id}/docker_composefile | Get docker compose file
[**ApplicationGetprivatekey**](ApplicationsApi.md#applicationgetprivatekey) | **GET** /applications/{application_id}/privatekey | Retrieves the path of the RSA private key
[**ApplicationModify**](ApplicationsApi.md#applicationmodify) | **PUT** /applications/{application_id} | Change application properties
[**ApplicationReseal**](ApplicationsApi.md#applicationreseal) | **GET** /applications/{application_id}/reseal | Cleans id and keys for git repo uploading
[**ApplicationRun**](ApplicationsApi.md#applicationrun) | **GET** /applications/{application_id}/run | Runs container image
[**ApplicationRunsdk**](ApplicationsApi.md#applicationrunsdk) | **GET** /applications/{application_id}/sdk/run | Runs SDK containers
[**ApplicationSdkContainer**](ApplicationsApi.md#applicationsdkcontainer) | **GET** /applications/{application_id}/sdk/container | Get SDK container
[**ApplicationStop**](ApplicationsApi.md#applicationstop) | **GET** /applications/{application_id}/stop | Stops running container image
[**ApplicationSyncfolders**](ApplicationsApi.md#applicationsyncfolders) | **GET** /applications/{application_id}/syncfolders | synchronizes folders
[**ApplicationUpdated**](ApplicationsApi.md#applicationupdated) | **GET** /applications/{application_id}/updated | Builds container image
[**ApplicationUpdatesdk**](ApplicationsApi.md#applicationupdatesdk) | **GET** /applications/{application_id}/sdk/update | Update SDK container
[**ApplicationsCreate**](ApplicationsApi.md#applicationscreate) | **GET** /applications/create | Loads an application configuration
[**ApplicationsLoad**](ApplicationsApi.md#applicationsload) | **GET** /applications/load | Loads an application configuration



## ApplicationBuild

> void ApplicationBuild (string applicationId, string configuration, string progressId = null)

Builds container image

Builds application release or debug container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationBuildExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Builds container image
                apiInstance.ApplicationBuild(applicationId, configuration, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationBuild: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
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
| **200** | Successful build |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationDelete

> void ApplicationDelete (string applicationId)

Remove an application and all the associated data and containers

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationDeleteExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)

            try
            {
                // Remove an application and all the associated data and containers
                apiInstance.ApplicationDelete(applicationId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationDelete: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 

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
| **204** | Application was correctly deleted |  -  |
| **404** | Application no found |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationDeploy

> void ApplicationDeploy (string applicationId, string configuration, string deviceid, string progressId = null)

Deploys container image

Deploys application release or debug container to target

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationDeployExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Deploys container image
                apiInstance.ApplicationDeploy(applicationId, configuration, deviceid, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationDeploy: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 
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
| **200** | Successful build |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **525** | Remote docker exception. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGet

> Application ApplicationGet (string applicationId)

Get application

Returns a specified application, knowing its id

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)

            try
            {
                // Get application
                Application result = apiInstance.ApplicationGet(applicationId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGet: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 

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
| **200** | Returns application |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGetcontainer

> DockerContainer ApplicationGetcontainer (string applicationId, string configuration, string deviceid)

Get container information

Get informations about container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetcontainerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 

            try
            {
                // Get container information
                DockerContainer result = apiInstance.ApplicationGetcontainer(applicationId, configuration, deviceid);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGetcontainer: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 

### Return type

[**DockerContainer**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns application container |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **525** | Remote docker exception. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGetcontainerLogs

> string ApplicationGetcontainerLogs (string applicationId, string configuration, string deviceid, bool? restart = null)

Get container log, chunk by chunk

Return one chunk of log (one or more lines), blocking if no data is available

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetcontainerLogsExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 
            var restart = true;  // bool? | when true reads the lock back from beginning (optional)  (default to false)

            try
            {
                // Get container log, chunk by chunk
                string result = apiInstance.ApplicationGetcontainerLogs(applicationId, configuration, deviceid, restart);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGetcontainerLogs: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 
 **restart** | **bool?**| when true reads the lock back from beginning | [optional] [default to false]

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a chunk of logs |  -  |
| **204** | No content |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGetdockerCommandline

> string ApplicationGetdockerCommandline (string applicationId, string configuration)

Get docker command line used to run the container

returns full command line

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetdockerCommandlineExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 

            try
            {
                // Get docker command line used to run the container
                string result = apiInstance.ApplicationGetdockerCommandline(applicationId, configuration);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGetdockerCommandline: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns command line |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGetdockerComposefile

> string ApplicationGetdockerComposefile (string applicationId, string configuration)

Get docker compose file

returns docker compose file that can be used to run the container and its dependencies

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetdockerComposefileExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 

            try
            {
                // Get docker compose file
                string result = apiInstance.ApplicationGetdockerComposefile(applicationId, configuration);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGetdockerComposefile: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Docker-compose file as string with *nix line ending |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationGetprivatekey

> string ApplicationGetprivatekey (string applicationId)

Retrieves the path of the RSA private key

The application stores the public key inside the container if ssh is enabled, this key will allow passwordless connections to a running instance

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationGetprivatekeyExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)

            try
            {
                // Retrieves the path of the RSA private key
                string result = apiInstance.ApplicationGetprivatekey(applicationId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationGetprivatekey: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | key returned |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationModify

> Application ApplicationModify (string applicationId, Application application = null)

Change application properties

Changes specified properties on an applicaton

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationModifyExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var application = new Application(); // Application |  (optional) 

            try
            {
                // Change application properties
                Application result = apiInstance.ApplicationModify(applicationId, application);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationModify: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **application** | [**Application**](Application.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns application |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationReseal

> void ApplicationReseal (string applicationId)

Cleans id and keys for git repo uploading

This operation make the application no longer valid, but allow you to upload it to a git repo from where it can be cloned/forked re-generating new ids every time, avoiding that all clones share the same id/keys.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationResealExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)

            try
            {
                // Cleans id and keys for git repo uploading
                apiInstance.ApplicationReseal(applicationId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationReseal: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | key returned |  -  |
| **404** | Application not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationRun

> DockerContainer ApplicationRun (string applicationId, string configuration, string deviceid, string progressId = null)

Runs container image

Runs application release or debug container on target, if the application is already running, restarts it

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationRunExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Runs container image
                DockerContainer result = apiInstance.ApplicationRun(applicationId, configuration, deviceid, progressId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationRun: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 
 **progressId** | **string**| Id of a progress cookie (uuid) | [optional] 

### Return type

[**DockerContainer**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns application container |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **525** | Remote docker exception. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationRunsdk

> InlineResponse200 ApplicationRunsdk (string applicationId, string configuration, bool? build = null, string progressId = null)

Runs SDK containers

Runs SDK container and return its IP and SSH port

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationRunsdkExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var build = true;  // bool? |  (optional)  (default to true)
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Runs SDK containers
                InlineResponse200 result = apiInstance.ApplicationRunsdk(applicationId, configuration, build, progressId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationRunsdk: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **build** | **bool?**|  | [optional] [default to true]
 **progressId** | **string**| Id of a progress cookie (uuid) | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Container started |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationSdkContainer

> DockerContainer ApplicationSdkContainer (string applicationId, string configuration)

Get SDK container

Get SDK container for check if it is running

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationSdkContainerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 

            try
            {
                // Get SDK container
                DockerContainer result = apiInstance.ApplicationSdkContainer(applicationId, configuration);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationSdkContainer: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 

### Return type

[**DockerContainer**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns application container |  -  |
| **204** | No content |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationStop

> void ApplicationStop (string applicationId, string configuration, string deviceid)

Stops running container image

Stops application release or debug container currently running on target

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationStopExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 

            try
            {
                // Stops running container image
                apiInstance.ApplicationStop(applicationId, configuration, deviceid);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationStop: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 

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
| **200** | Application stopped (returned also if not running) |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationSyncfolders

> void ApplicationSyncfolders (string applicationId, string sourcefolder, string configuration, string deviceid, string destfolder, bool? sourceIsSdk = null, string progressId = null)

synchronizes folders

synchronizes folders between host/SDK container and application container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationSyncfoldersExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var sourcefolder = sourcefolder_example;  // string | 
            var configuration = configuration_example;  // string | 
            var deviceid = deviceid_example;  // string | 
            var destfolder = destfolder_example;  // string | 
            var sourceIsSdk = true;  // bool? |  (optional) 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // synchronizes folders
                apiInstance.ApplicationSyncfolders(applicationId, sourcefolder, configuration, deviceid, destfolder, sourceIsSdk, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationSyncfolders: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **sourcefolder** | **string**|  | 
 **configuration** | **string**|  | 
 **deviceid** | **string**|  | 
 **destfolder** | **string**|  | 
 **sourceIsSdk** | **bool?**|  | [optional] 
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
| **200** | Sysroot updated |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **523** | Container is not running. |  -  |
| **525** | Remote docker exception. |  -  |
| **529** | Remote command execution failed. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **541** | SDK container is not running. |  -  |
| **548** | Container does not support SSH |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationUpdated

> bool ApplicationUpdated (string applicationId, string configuration)

Builds container image

Builds application release or debug container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationUpdatedExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 

            try
            {
                // Builds container image
                bool result = apiInstance.ApplicationUpdated(applicationId, configuration);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationUpdated: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful build |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationUpdatesdk

> void ApplicationUpdatesdk (string applicationId, string configuration, string progressId = null)

Update SDK container

Updates/rebuilds the SDK container by adding new dev libraries or synchronizing sysroots

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationUpdatesdkExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Update SDK container
                apiInstance.ApplicationUpdatesdk(applicationId, configuration, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationUpdatesdk: " + e.Message );
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
 **applicationId** | **string**| Id of an application (uuid) | 
 **configuration** | **string**|  | 
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
| **200** | SDK updated |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationsCreate

> Application ApplicationsCreate (string platformId, string path, string username = null)

Loads an application configuration

Returns data about an application

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationsCreateExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var platformId = platformId_example;  // string | 
            var path = path_example;  // string | 
            var username = username_example;  // string |  (optional) 

            try
            {
                // Loads an application configuration
                Application result = apiInstance.ApplicationsCreate(platformId, path, username);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationsCreate: " + e.Message );
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
 **platformId** | **string**|  | 
 **path** | **string**|  | 
 **username** | **string**|  | [optional] 

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
| **404** | Platform not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **540** | Invalid path. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationsLoad

> Application ApplicationsLoad (string path)

Loads an application configuration

Returns data about an application

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationsLoadExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var path = path_example;  // string | 

            try
            {
                // Loads an application configuration
                Application result = apiInstance.ApplicationsLoad(path);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationsLoad: " + e.Message );
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
 **path** | **string**|  | 

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

