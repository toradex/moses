# TorizonRestAPI.Api.DevicesApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ContainerGetmemory**](DevicesApi.md#containergetmemory) | **GET** /devices/{device_id}/containers/{container_id}/memory | Return container memory information
[**ContainerGetmountpoints**](DevicesApi.md#containergetmountpoints) | **GET** /devices/{device_id}/containers/{container_id}/storage | return information about storage
[**ContainerGetprocesses**](DevicesApi.md#containergetprocesses) | **GET** /devices/{device_id}/containers/{container_id}/processes | return processes running in container
[**ContainerStart**](DevicesApi.md#containerstart) | **GET** /devices/{device_id}/containers/{container_id}/start | starts container
[**ContainerStop**](DevicesApi.md#containerstop) | **GET** /devices/{device_id}/containers/{container_id}/stop | stops container
[**ContainersDeletecontainer**](DevicesApi.md#containersdeletecontainer) | **DELETE** /devices/{device_id}/containers/{container_id} | delete a container
[**ContainersGetcontainer**](DevicesApi.md#containersgetcontainer) | **GET** /devices/{device_id}/containers/{container_id} | get container details
[**DeviceClosedocker**](DevicesApi.md#deviceclosedocker) | **GET** /devices/{device_id}/docker/close | Disables remote docker
[**DeviceClosessh**](DevicesApi.md#deviceclosessh) | **GET** /devices/{device_id}/ssh/close | Disables ssh tunneling
[**DeviceDelete**](DevicesApi.md#devicedelete) | **DELETE** /devices/{device_id} | Remove a device
[**DeviceGet**](DevicesApi.md#deviceget) | **GET** /devices/{device_id} | Get device
[**DeviceGetcontainers**](DevicesApi.md#devicegetcontainers) | **GET** /devices/{device_id}/containers | list containers
[**DeviceGetdockerport**](DevicesApi.md#devicegetdockerport) | **GET** /devices/{device_id}/docker/port | remote docker local port
[**DeviceGetimages**](DevicesApi.md#devicegetimages) | **GET** /devices/{device_id}/images | list images
[**DeviceGetmemory**](DevicesApi.md#devicegetmemory) | **GET** /devices/{device_id}/memory | Return memory information
[**DeviceGetmountpoints**](DevicesApi.md#devicegetmountpoints) | **GET** /devices/{device_id}/storage | return storage information for a device
[**DeviceGetprivatekey**](DevicesApi.md#devicegetprivatekey) | **GET** /devices/{device_id}/privatekey | return the path of the device private key
[**DeviceGetprocesses**](DevicesApi.md#devicegetprocesses) | **GET** /devices/{device_id}/processes | list running processes on a device
[**DeviceGetsshport**](DevicesApi.md#devicegetsshport) | **GET** /devices/{device_id}/ssh/port | remote ssh local port
[**DeviceModify**](DevicesApi.md#devicemodify) | **PUT** /devices/{device_id} | Change device properties
[**DeviceOpendocker**](DevicesApi.md#deviceopendocker) | **GET** /devices/{device_id}/docker/open | Expose remote docker
[**DeviceOpenssh**](DevicesApi.md#deviceopenssh) | **GET** /devices/{device_id}/ssh/open | Expose remote ssh
[**DeviceSyncfolders**](DevicesApi.md#devicesyncfolders) | **GET** /devices/{device_id}/syncfolders | synchronizes folders
[**DeviceUpdate**](DevicesApi.md#deviceupdate) | **GET** /devices/{device_id}/update | update information for a specific device
[**DevicesGet**](DevicesApi.md#devicesget) | **GET** /devices | Get all devices
[**DevicesNetworkdetect**](DevicesApi.md#devicesnetworkdetect) | **GET** /devices/network_detect | Finds a network device
[**DevicesSerialdetect**](DevicesApi.md#devicesserialdetect) | **GET** /devices/serial_detect | Finds a device connected to serial port
[**ImagesDeleteimage**](DevicesApi.md#imagesdeleteimage) | **DELETE** /devices/{device_id}/images/{image_id} | delete an image
[**ImagesGetimage**](DevicesApi.md#imagesgetimage) | **GET** /devices/{device_id}/images/{image_id} | get image details



## ContainerGetmemory

> MemInfo ContainerGetmemory (string deviceId, string containerId)

Return container memory information

Return total/free/available memory on a specific container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerGetmemoryExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // Return container memory information
                MemInfo result = apiInstance.ContainerGetmemory(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerGetmemory: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

### Return type

[**MemInfo**](MemInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns memory information |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerGetmountpoints

> List&lt;MountPoint&gt; ContainerGetmountpoints (string deviceId, string containerId)

return information about storage

returns a list of storages available inside the container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerGetmountpointsExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // return information about storage
                List<MountPoint> result = apiInstance.ContainerGetmountpoints(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerGetmountpoints: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

### Return type

[**List&lt;MountPoint&gt;**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of storage informations |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerGetprocesses

> List&lt;Process&gt; ContainerGetprocesses (string deviceId, string containerId)

return processes running in container

returns a list of processes running in the specified container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerGetprocessesExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // return processes running in container
                List<Process> result = apiInstance.ContainerGetprocesses(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerGetprocesses: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

### Return type

[**List&lt;Process&gt;**](Process.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of processes |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerStart

> DockerContainer ContainerStart (string deviceId, string containerId)

starts container

Start specified container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerStartExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // starts container
                DockerContainer result = apiInstance.ContainerStart(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerStart: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

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
| **200** | Returns container |  -  |
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerStop

> DockerContainer ContainerStop (string deviceId, string containerId)

stops container

Stops specified container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerStopExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // stops container
                DockerContainer result = apiInstance.ContainerStop(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerStop: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

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
| **200** | Returns container |  -  |
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainersDeletecontainer

> void ContainersDeletecontainer (string deviceId, string containerId)

delete a container

Executes rm command on container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainersDeletecontainerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // delete a container
                apiInstance.ContainersDeletecontainer(deviceId, containerId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainersDeletecontainer: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

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
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainersGetcontainer

> DockerContainer ContainersGetcontainer (string deviceId, string containerId)

get container details

Get detailed information on a specific container

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainersGetcontainerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var containerId = containerId_example;  // string | Id of a container

            try
            {
                // get container details
                DockerContainer result = apiInstance.ContainersGetcontainer(deviceId, containerId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainersGetcontainer: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **containerId** | **string**| Id of a container | 

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
| **200** | Returns container |  -  |
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceClosedocker

> void DeviceClosedocker (string deviceId)

Disables remote docker

Stop exposing remote docker port on localhost

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceClosedockerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Disables remote docker
                apiInstance.DeviceClosedocker(deviceId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceClosedocker: " + e.Message );
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
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceClosessh

> void DeviceClosessh (string deviceId)

Disables ssh tunneling

Stop exposing remote ssh port on localhost

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceClosesshExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Disables ssh tunneling
                apiInstance.DeviceClosessh(deviceId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceClosessh: " + e.Message );
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
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceDelete

> void DeviceDelete (string deviceId)

Remove a device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceDeleteExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Remove a device
                apiInstance.DeviceDelete(deviceId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceDelete: " + e.Message );
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
| **204** | Device was correctly deleted |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGet

> TargetDevice DeviceGet (string deviceId)

Get device

Returns a specified device, knowing its id

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Get device
                TargetDevice result = apiInstance.DeviceGet(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGet: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**TargetDevice**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns device |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetcontainers

> List&lt;DockerContainer&gt; DeviceGetcontainers (string deviceId)

list containers

Get containers running on a specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetcontainersExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // list containers
                List<DockerContainer> result = apiInstance.DeviceGetcontainers(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetcontainers: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**List&lt;DockerContainer&gt;**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of containers |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetdockerport

> int DeviceGetdockerport (string deviceId)

remote docker local port

Get local port where docker is tunneled

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetdockerportExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // remote docker local port
                int result = apiInstance.DeviceGetdockerport(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetdockerport: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns port |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetimages

> List&lt;DockerImage&gt; DeviceGetimages (string deviceId)

list images

Get images available on a specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetimagesExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // list images
                List<DockerImage> result = apiInstance.DeviceGetimages(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetimages: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**List&lt;DockerImage&gt;**](DockerImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of images |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetmemory

> MemInfo DeviceGetmemory (string deviceId)

Return memory information

Return total/free/available memory on the device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetmemoryExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // Return memory information
                MemInfo result = apiInstance.DeviceGetmemory(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetmemory: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**MemInfo**](MemInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns memory information |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetmountpoints

> List&lt;MountPoint&gt; DeviceGetmountpoints (string deviceId)

return storage information for a device

Get a list of storages for the specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetmountpointsExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // return storage information for a device
                List<MountPoint> result = apiInstance.DeviceGetmountpoints(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetmountpoints: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**List&lt;MountPoint&gt;**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of storage information |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetprivatekey

> string DeviceGetprivatekey (string deviceId)

return the path of the device private key

returns the key that can be used to activate passowordless connections to the device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetprivatekeyExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // return the path of the device private key
                string result = apiInstance.DeviceGetprivatekey(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetprivatekey: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

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
| **200** | Path of the private key file |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetprocesses

> List&lt;Process&gt; DeviceGetprocesses (string deviceId)

list running processes on a device

Get processes running on a specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetprocessesExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // list running processes on a device
                List<Process> result = apiInstance.DeviceGetprocesses(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetprocesses: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**List&lt;Process&gt;**](Process.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of processes |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetsshport

> int DeviceGetsshport (string deviceId)

remote ssh local port

Get local port where ssh is tunneled

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceGetsshportExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // remote ssh local port
                int result = apiInstance.DeviceGetsshport(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceGetsshport: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns port |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceModify

> TargetDevice DeviceModify (string deviceId, TargetDevice device = null)

Change device properties

Changes specified properties on a device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceModifyExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var device = new TargetDevice(); // TargetDevice |  (optional) 

            try
            {
                // Change device properties
                TargetDevice result = apiInstance.DeviceModify(deviceId, device);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceModify: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **device** | [**TargetDevice**](TargetDevice.md)|  | [optional] 

### Return type

[**TargetDevice**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns device |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceOpendocker

> int DeviceOpendocker (string deviceId, int port = null)

Expose remote docker

Expose remote docker port on localhost

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceOpendockerExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var port = 56;  // int |  (optional) 

            try
            {
                // Expose remote docker
                int result = apiInstance.DeviceOpendocker(deviceId, port);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceOpendocker: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **port** | **int**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns port |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceOpenssh

> int DeviceOpenssh (string deviceId, int port = null)

Expose remote ssh

Expose remote ssh port on localhost

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceOpensshExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var port = 56;  // int |  (optional) 

            try
            {
                // Expose remote ssh
                int result = apiInstance.DeviceOpenssh(deviceId, port);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceOpenssh: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **port** | **int**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns port |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceSyncfolders

> void DeviceSyncfolders (string deviceId, string sourcefolder, string destfolder)

synchronizes folders

synchronizes folders between host and target

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceSyncfoldersExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var sourcefolder = sourcefolder_example;  // string | 
            var destfolder = destfolder_example;  // string | 

            try
            {
                // synchronizes folders
                apiInstance.DeviceSyncfolders(deviceId, sourcefolder, destfolder);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceSyncfolders: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **sourcefolder** | **string**|  | 
 **destfolder** | **string**|  | 

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
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **523** | Container is not running. |  -  |
| **533** | SSH error. |  -  |
| **544** | Local command execution failed. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceUpdate

> TargetDevice DeviceUpdate (string deviceId)

update information for a specific device

Returns a specified device, with updated info if available

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceUpdateExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number

            try
            {
                // update information for a specific device
                TargetDevice result = apiInstance.DeviceUpdate(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceUpdate: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 

### Return type

[**TargetDevice**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns device |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **533** | SSH error. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DevicesGet

> List&lt;TargetDevice&gt; DevicesGet ()

Get all devices

Returns all configured devices

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DevicesGetExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);

            try
            {
                // Get all devices
                List<TargetDevice> result = apiInstance.DevicesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DevicesGet: " + e.Message );
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

[**List&lt;TargetDevice&gt;**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DevicesNetworkdetect

> TargetDevice DevicesNetworkdetect (string hostname, string username, string password)

Finds a network device

Returns a new device detected from network

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DevicesNetworkdetectExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var hostname = hostname_example;  // string | 
            var username = username_example;  // string | 
            var password = password_example;  // string | 

            try
            {
                // Finds a network device
                TargetDevice result = apiInstance.DevicesNetworkdetect(hostname, username, password);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DevicesNetworkdetect: " + e.Message );
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
 **hostname** | **string**|  | 
 **username** | **string**|  | 
 **password** | **string**|  | 

### Return type

[**TargetDevice**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns device |  -  |
| **500** | Unexpected exception. |  -  |
| **524** | User is not enable to execute commands as root. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **533** | SSH error. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DevicesSerialdetect

> TargetDevice DevicesSerialdetect (string port, string username, string password)

Finds a device connected to serial port

Returns a new device detected from serial port

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DevicesSerialdetectExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var port = port_example;  // string | 
            var username = username_example;  // string | 
            var password = password_example;  // string | 

            try
            {
                // Finds a device connected to serial port
                TargetDevice result = apiInstance.DevicesSerialdetect(port, username, password);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DevicesSerialdetect: " + e.Message );
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
 **port** | **string**|  | 
 **username** | **string**|  | 
 **password** | **string**|  | 

### Return type

[**TargetDevice**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns device |  -  |
| **500** | Unexpected exception. |  -  |
| **524** | User is not enable to execute commands as root. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |
| **536** | Serial port error. |  -  |
| **537** | Command timeout. |  -  |
| **538** | Login failed. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ImagesDeleteimage

> void ImagesDeleteimage (string deviceId, string imageId)

delete an image

Executes rmi command on and image

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ImagesDeleteimageExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var imageId = imageId_example;  // string | Id of an image

            try
            {
                // delete an image
                apiInstance.ImagesDeleteimage(deviceId, imageId);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ImagesDeleteimage: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **imageId** | **string**| Id of an image | 

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
| **404** | Device or image not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ImagesGetimage

> DockerImage ImagesGetimage (string deviceId, string imageId)

get image details

Get detailed information on an image

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ImagesGetimageExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = deviceId_example;  // string | Target device serial number
            var imageId = imageId_example;  // string | Id of an image

            try
            {
                // get image details
                DockerImage result = apiInstance.ImagesGetimage(deviceId, imageId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ImagesGetimage: " + e.Message );
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
 **deviceId** | **string**| Target device serial number | 
 **imageId** | **string**| Id of an image | 

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns image |  -  |
| **404** | Device or Image not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

