# TorizonRestAPI.Api.ApplicationsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApplicationBuild**](ApplicationsApi.md#applicationbuild) | **GET** /applications/{application_id}/build | Build container image
[**ApplicationDelete**](ApplicationsApi.md#applicationdelete) | **DELETE** /applications/{application_id} | Remove an application
[**ApplicationDeploy**](ApplicationsApi.md#applicationdeploy) | **GET** /applications/{application_id}/deploy | Deploy container image
[**ApplicationGet**](ApplicationsApi.md#applicationget) | **GET** /applications/{application_id} | Get application
[**ApplicationGetcontainer**](ApplicationsApi.md#applicationgetcontainer) | **GET** /applications/{application_id}/container | Get container information
[**ApplicationGetcontainerLogs**](ApplicationsApi.md#applicationgetcontainerlogs) | **GET** /applications/{application_id}/container_logs | Get one of more lines from container logs
[**ApplicationGetdockerCommandline**](ApplicationsApi.md#applicationgetdockercommandline) | **GET** /applications/{application_id}/docker_commandline | Get docker command line to run the application/json
[**ApplicationGetdockerComposefile**](ApplicationsApi.md#applicationgetdockercomposefile) | **GET** /applications/{application_id}/docker_composefile | Get docker compose file
[**ApplicationGetprivatekey**](ApplicationsApi.md#applicationgetprivatekey) | **GET** /applications/{application_id}/privatekey | Get the path of the RSA private key
[**ApplicationModify**](ApplicationsApi.md#applicationmodify) | **PUT** /applications/{application_id} | Change application properties
[**ApplicationPublish**](ApplicationsApi.md#applicationpublish) | **GET** /applications/{application_id}/publish | Publish a new version of the application on Torizon OTA
[**ApplicationPushToRegistry**](ApplicationsApi.md#applicationpushtoregistry) | **GET** /applications/{application_id}/push_to_registry | Push application to docker registry
[**ApplicationReseal**](ApplicationsApi.md#applicationreseal) | **GET** /applications/{application_id}/reseal | Clean id and keys from application configuration
[**ApplicationRun**](ApplicationsApi.md#applicationrun) | **GET** /applications/{application_id}/run | Run container image
[**ApplicationRunsdk**](ApplicationsApi.md#applicationrunsdk) | **GET** /applications/{application_id}/sdk/run | Run SDK containers
[**ApplicationSdkContainer**](ApplicationsApi.md#applicationsdkcontainer) | **GET** /applications/{application_id}/sdk/container | Get SDK container
[**ApplicationStop**](ApplicationsApi.md#applicationstop) | **GET** /applications/{application_id}/stop | Stop running container image
[**ApplicationSyncfolders**](ApplicationsApi.md#applicationsyncfolders) | **GET** /applications/{application_id}/syncfolders | Synchronize folders
[**ApplicationTcbBuildYaml**](ApplicationsApi.md#applicationtcbbuildyaml) | **GET** /applications/{application_id}/tcb_build_yaml | Build the TorizonCore tcbuild.yaml
[**ApplicationTcbDeploy**](ApplicationsApi.md#applicationtcbdeploy) | **GET** /applications/{application_id}/tcb_deploy | TorizonCore unpack command
[**ApplicationTcbDtCheckout**](ApplicationsApi.md#applicationtcbdtcheckout) | **GET** /applications/{application_id}/tcb_dt_checkout | TorizonCore Device Tree repo checkout
[**ApplicationTcbIsolate**](ApplicationsApi.md#applicationtcbisolate) | **GET** /applications/{application_id}/tcb_isolate | TorizonCore isolate command
[**ApplicationTcbPush**](ApplicationsApi.md#applicationtcbpush) | **GET** /applications/{application_id}/tcb_push | TorizonCore Builder push command.
[**ApplicationTcbUnion**](ApplicationsApi.md#applicationtcbunion) | **GET** /applications/{application_id}/tcb_union | TorizonCore Builder union command.
[**ApplicationTcbUnpack**](ApplicationsApi.md#applicationtcbunpack) | **GET** /applications/{application_id}/tcb_unpack | TorizonCore unpack command
[**ApplicationUpdated**](ApplicationsApi.md#applicationupdated) | **GET** /applications/{application_id}/updated | Check if container image is up to date
[**ApplicationUpdatesdk**](ApplicationsApi.md#applicationupdatesdk) | **GET** /applications/{application_id}/sdk/update | Update SDK container
[**ApplicationValidateArrayItem**](ApplicationsApi.md#applicationvalidatearrayitem) | **GET** /applications/{application_id}/validate_array_item | Validates a value for a parameter
[**ApplicationValidateDictionaryEntry**](ApplicationsApi.md#applicationvalidatedictionaryentry) | **GET** /applications/{application_id}/validate_dictionary_entry | Validates a value for a parameter
[**ApplicationValidateParameter**](ApplicationsApi.md#applicationvalidateparameter) | **GET** /applications/{application_id}/validate_parameter | Validates a value for a parameter
[**ApplicationsCreate**](ApplicationsApi.md#applicationscreate) | **GET** /applications/create | Create an application configuration
[**ApplicationsLoad**](ApplicationsApi.md#applicationsload) | **GET** /applications/load | Load an application configuration



## ApplicationBuild

> void ApplicationBuild (string applicationId, string configuration, string progressId = null)

Build container image

Build application release or debug container

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
                // Build container image
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
| **200** | OK |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationDelete

> void ApplicationDelete (string applicationId)

Remove an application

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
                // Remove an application
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
| **204** | OK |  -  |
| **404** | Application no found |  -  |
| **500** | Unexpected exception. |  -  |
| **530** | Local docker exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationDeploy

> void ApplicationDeploy (string applicationId, string configuration, string deviceId, string progressId = null)

Deploy container image

Deploy application container to target

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
            var deviceId = deviceId_example;  // string | Target device serial number
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Deploy container image
                apiInstance.ApplicationDeploy(applicationId, configuration, deviceId, progressId);
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
 **deviceId** | **string**| Target device serial number | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **525** | Remote docker exception. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |
| **551** | Operation has been aborted |  -  |

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

> DockerContainer ApplicationGetcontainer (string applicationId, string configuration, string deviceId)

Get container information

Get detailed informations about container

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
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Get container information
                DockerContainer result = apiInstance.ApplicationGetcontainer(applicationId, configuration, deviceId);
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
 **deviceId** | **string**| Target device serial number | 

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
| **200** | Container information |  -  |
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

> string ApplicationGetcontainerLogs (string applicationId, string configuration, string deviceId, bool? restart = null)

Get one of more lines from container logs

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
            var deviceId = deviceId_example;  // string | Target device serial number
            var restart = true;  // bool? | when true reads the lock back from beginning (optional)  (default to false)

            try
            {
                // Get one of more lines from container logs
                string result = apiInstance.ApplicationGetcontainerLogs(applicationId, configuration, deviceId, restart);
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
 **deviceId** | **string**| Target device serial number | 
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
| **200** | Log entries as text |  -  |
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

Get docker command line to run the application/json

Return the full docker command line that can be used to run the application container

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
                // Get docker command line to run the application/json
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
| **200** | Command line |  -  |
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

Return docker-compose file that can be used to run the application container and its dependencies

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
| **200** | Docker-compose file (string with *nix line endings) |  -  |
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

Get the path of the RSA private key

Retrieve the path of the private key that allows passwordless connection to the container. The application stores the public key inside the container if ssh is enabled (usually for debug builds only)

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
                // Get the path of the RSA private key
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
| **200** | Key path |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationModify

> Application ApplicationModify (string applicationId, Application application = null)

Change application properties

Changes specified properties on an application

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
| **200** | Application information |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationPublish

> void ApplicationPublish (string applicationId, string credentials, string dockeruser, string dockerpass, string progressId = null)

Publish a new version of the application on Torizon OTA

Publishes a new package version for the application, if no credentials are provided, then only docker-compose file is generated.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationPublishExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var credentials = credentials_example;  // string | credentials file
            var dockeruser = dockeruser_example;  // string | user for docker registry login
            var dockerpass = dockerpass_example;  // string | password for docker registry login
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Publish a new version of the application on Torizon OTA
                apiInstance.ApplicationPublish(applicationId, credentials, dockeruser, dockerpass, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationPublish: " + e.Message );
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
 **credentials** | **string**| credentials file | 
 **dockeruser** | **string**| user for docker registry login | 
 **dockerpass** | **string**| password for docker registry login | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **552** | Invalid or missing parameter |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationPushToRegistry

> void ApplicationPushToRegistry (string applicationId, string configuration, string username, string password, string progressId = null)

Push application to docker registry

Push application's container to a docker registry, using authentication

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationPushToRegistryExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var username = username_example;  // string | 
            var password = password_example;  // string | 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Push application to docker registry
                apiInstance.ApplicationPushToRegistry(applicationId, configuration, username, password, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationPushToRegistry: " + e.Message );
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
 **username** | **string**|  | 
 **password** | **string**|  | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationReseal

> void ApplicationReseal (string applicationId)

Clean id and keys from application configuration

This operation make the application no longer valid, but allow you to upload it to a git repo from where it can be cloned/forked. Id and keys will be re-generated on next re-opening of the application, leading to different names for the images etc.

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
                // Clean id and keys from application configuration
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
| **200** | OK |  -  |
| **404** | Application not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationRun

> DockerContainer ApplicationRun (string applicationId, string configuration, string deviceId, string progressId = null)

Run container image

Run the application release or debug container on target, if the application is already running, restarts it

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
            var deviceId = deviceId_example;  // string | Target device serial number
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Run container image
                DockerContainer result = apiInstance.ApplicationRun(applicationId, configuration, deviceId, progressId);
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
 **deviceId** | **string**| Target device serial number | 
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
| **200** | Container information |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **525** | Remote docker exception. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationRunsdk

> InlineResponse200 ApplicationRunsdk (string applicationId, string configuration, bool? build = null, string progressId = null)

Run SDK containers

Run SDK container and return its IP and SSH port

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
                // Run SDK containers
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
| **200** | IP and port of the SSH port exposed by container (if any) |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationSdkContainer

> DockerContainer ApplicationSdkContainer (string applicationId, string configuration)

Get SDK container

Get SDK container information (can be used to check if it's running)

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
| **200** | Container information |  -  |
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

> void ApplicationStop (string applicationId, string configuration, string deviceId)

Stop running container image

Stop application release or debug container currently running on target, operation succeeds even if the container is not running

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
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Stop running container image
                apiInstance.ApplicationStop(applicationId, configuration, deviceId);
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
 **deviceId** | **string**| Target device serial number | 

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
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationSyncfolders

> void ApplicationSyncfolders (string applicationId, string sourcefolder, string configuration, string deviceId, string destfolder, bool? sourceIsSdk = null, string progressId = null)

Synchronize folders

Synchronizes folders between host/SDK container and the application container

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
            var deviceId = deviceId_example;  // string | Target device serial number
            var destfolder = destfolder_example;  // string | 
            var sourceIsSdk = true;  // bool? |  (optional) 
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Synchronize folders
                apiInstance.ApplicationSyncfolders(applicationId, sourcefolder, configuration, deviceId, destfolder, sourceIsSdk, progressId);
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
 **deviceId** | **string**| Target device serial number | 
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
| **200** | OK |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **523** | Container is not running. |  -  |
| **525** | Remote docker exception. |  -  |
| **529** | Remote command execution failed. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **541** | SDK container is not running. |  -  |
| **549** | Container does not support SSH |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbBuildYaml

> void ApplicationTcbBuildYaml (string applicationId, string yamlfilepath, string progressId = null)

Build the TorizonCore tcbuild.yaml

Build the TorizonCore tcbuild.yaml using TorizonCore Builder Docker image.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbBuildYamlExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var yamlfilepath = yamlfilepath_example;  // string | the yaml file name from workspace path
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Build the TorizonCore tcbuild.yaml
                apiInstance.ApplicationTcbBuildYaml(applicationId, yamlfilepath, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbBuildYaml: " + e.Message );
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
 **yamlfilepath** | **string**| the yaml file name from workspace path | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbDeploy

> void ApplicationTcbDeploy (string applicationId, string host, string username, string password, string progressId = null)

TorizonCore unpack command

Unpack the output using TorizonCore Builder Docker image.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbDeployExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var host = host_example;  // string | the hostname or ip address of the device to be deployed
            var username = username_example;  // string | the Torizon username of the device to be deployed
            var password = password_example;  // string | the Torizon password of the device to be deployed
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore unpack command
                apiInstance.ApplicationTcbDeploy(applicationId, host, username, password, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbDeploy: " + e.Message );
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
 **host** | **string**| the hostname or ip address of the device to be deployed | 
 **username** | **string**| the Torizon username of the device to be deployed | 
 **password** | **string**| the Torizon password of the device to be deployed | 
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
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbDtCheckout

> void ApplicationTcbDtCheckout (string applicationId, string progressId = null)

TorizonCore Device Tree repo checkout

Checkout the device tree and overlays repository at https://github.com/toradex/device-trees

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbDtCheckoutExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore Device Tree repo checkout
                apiInstance.ApplicationTcbDtCheckout(applicationId, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbDtCheckout: " + e.Message );
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbIsolate

> void ApplicationTcbIsolate (string applicationId, string host, string username, string password, string outputDir, string progressId = null)

TorizonCore isolate command

Get configuration changes from the target board.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbIsolateExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var host = host_example;  // string | the hostname or ip address of the device to be deployed
            var username = username_example;  // string | the Torizon username of the device to be deployed
            var password = password_example;  // string | the Torizon password of the device to be deployed
            var outputDir = outputDir_example;  // string | the direcotry path that the changes will be save
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore isolate command
                apiInstance.ApplicationTcbIsolate(applicationId, host, username, password, outputDir, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbIsolate: " + e.Message );
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
 **host** | **string**| the hostname or ip address of the device to be deployed | 
 **username** | **string**| the Torizon username of the device to be deployed | 
 **password** | **string**| the Torizon password of the device to be deployed | 
 **outputDir** | **string**| the direcotry path that the changes will be save | 
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
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbPush

> void ApplicationTcbPush (string applicationId, string branch, string credentials, string progressId = null)

TorizonCore Builder push command.

The command push from TorizonCore Builder can be used to push a new TorizonCore image to Torizon OTA.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbPushExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var branch = branch_example;  // string | union branch string
            var credentials = credentials_example;  // string | credentials file path
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore Builder push command.
                apiInstance.ApplicationTcbPush(applicationId, branch, credentials, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbPush: " + e.Message );
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
 **branch** | **string**| union branch string | 
 **credentials** | **string**| credentials file path | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbUnion

> void ApplicationTcbUnion (string applicationId, string branch, string progressId = null)

TorizonCore Builder union command.

union makes an OSTree branch (containing the commit for changes) for all changes provided by the user to be made in OSTree rootfs of unpacked base Torizon image.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbUnionExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var branch = branch_example;  // string | union branch string
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore Builder union command.
                apiInstance.ApplicationTcbUnion(applicationId, branch, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbUnion: " + e.Message );
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
 **branch** | **string**| union branch string | 
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
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationTcbUnpack

> void ApplicationTcbUnpack (string applicationId, string outputpath, string progressId = null)

TorizonCore unpack command

Unpack the output using TorizonCore Builder Docker image.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationTcbUnpackExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var outputpath = outputpath_example;  // string | the output directory created by TorizonCore builder from workspace path
            var progressId = progressId_example;  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // TorizonCore unpack command
                apiInstance.ApplicationTcbUnpack(applicationId, outputpath, progressId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationTcbUnpack: " + e.Message );
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
 **outputpath** | **string**| the output directory created by TorizonCore builder from workspace path | 
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
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **550** | No tag has been set for the image |  -  |
| **551** | Operation has been aborted |  -  |
| **553** | TorizonCore Builder error |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationUpdated

> bool ApplicationUpdated (string applicationId, string configuration)

Check if container image is up to date

Check if some properties have been changed after the last build of the configuration-specific container image

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
                // Check if container image is up to date
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
| **200** | true if container image is up to date |  -  |
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

Update the SDK container by adding new dev libraries or synchronizing sysroots

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
| **200** | OK |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **530** | Local docker exception. |  -  |
| **533** | SSH error. |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationValidateArrayItem

> ValidationResult ApplicationValidateArrayItem (string applicationId, string configuration, string _parameter, string value, int index)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationValidateArrayItemExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var _parameter = _parameter_example;  // string | 
            var value = value_example;  // string | 
            var index = 56;  // int | 

            try
            {
                // Validates a value for a parameter
                ValidationResult result = apiInstance.ApplicationValidateArrayItem(applicationId, configuration, _parameter, value, index);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationValidateArrayItem: " + e.Message );
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
 **_parameter** | **string**|  | 
 **value** | **string**|  | 
 **index** | **int**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation results |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationValidateDictionaryEntry

> ValidationResult ApplicationValidateDictionaryEntry (string applicationId, string configuration, string _parameter, string key, string value, bool newitem)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationValidateDictionaryEntryExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var _parameter = _parameter_example;  // string | 
            var key = key_example;  // string | 
            var value = value_example;  // string | 
            var newitem = true;  // bool | 

            try
            {
                // Validates a value for a parameter
                ValidationResult result = apiInstance.ApplicationValidateDictionaryEntry(applicationId, configuration, _parameter, key, value, newitem);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationValidateDictionaryEntry: " + e.Message );
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
 **_parameter** | **string**|  | 
 **key** | **string**|  | 
 **value** | **string**|  | 
 **newitem** | **bool**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation results |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationValidateParameter

> ValidationResult ApplicationValidateParameter (string applicationId, string configuration, string _parameter, string value)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ApplicationValidateParameterExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new ApplicationsApi(Configuration.Default);
            var applicationId = applicationId_example;  // string | Id of an application (uuid)
            var configuration = configuration_example;  // string | 
            var _parameter = _parameter_example;  // string | 
            var value = value_example;  // string | 

            try
            {
                // Validates a value for a parameter
                ValidationResult result = apiInstance.ApplicationValidateParameter(applicationId, configuration, _parameter, value);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ApplicationsApi.ApplicationValidateParameter: " + e.Message );
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
 **_parameter** | **string**|  | 
 **value** | **string**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation results |  -  |
| **404** | Application not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApplicationsCreate

> Application ApplicationsCreate (string platformId, string path, string username = null)

Create an application configuration

Create a new application configuration

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
                // Create an application configuration
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
| **200** | Application information |  -  |
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

Load an application configuration

Load an application configuration from the local filesystem

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
                // Load an application configuration
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

