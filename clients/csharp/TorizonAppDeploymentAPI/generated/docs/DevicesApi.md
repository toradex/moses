# TorizonRestAPI.Api.DevicesApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ContainerGetlogs**](DevicesApi.md#containergetlogs) | **GET** /devices/{device_id}/containers/{container_id}/logs | Return text lines from the container logs
[**ContainerGetmemory**](DevicesApi.md#containergetmemory) | **GET** /devices/{device_id}/containers/{container_id}/memory | Return container memory information
[**ContainerGetmountpoints**](DevicesApi.md#containergetmountpoints) | **GET** /devices/{device_id}/containers/{container_id}/storage | Return information about storage
[**ContainerGetprocesses**](DevicesApi.md#containergetprocesses) | **GET** /devices/{device_id}/containers/{container_id}/processes | Get processes running in container
[**ContainerStart**](DevicesApi.md#containerstart) | **GET** /devices/{device_id}/containers/{container_id}/start | Starts container
[**ContainerStop**](DevicesApi.md#containerstop) | **GET** /devices/{device_id}/containers/{container_id}/stop | Stop container
[**ContainersDeletecontainer**](DevicesApi.md#containersdeletecontainer) | **DELETE** /devices/{device_id}/containers/{container_id} | Delete a container
[**ContainersGetcontainer**](DevicesApi.md#containersgetcontainer) | **GET** /devices/{device_id}/containers/{container_id} | Get information about a container
[**DeviceClosedocker**](DevicesApi.md#deviceclosedocker) | **GET** /devices/{device_id}/docker/close | Close SSH tunnel for docker API
[**DeviceClosessh**](DevicesApi.md#deviceclosessh) | **GET** /devices/{device_id}/ssh/close | Close SSH tunnel for shell
[**DeviceCurrentIp**](DevicesApi.md#devicecurrentip) | **GET** /devices/{device_id}/current_ip | Get current ip of the device
[**DeviceDelete**](DevicesApi.md#devicedelete) | **DELETE** /devices/{device_id} | Remove a device
[**DeviceGet**](DevicesApi.md#deviceget) | **GET** /devices/{device_id} | Get device
[**DeviceGetcontainers**](DevicesApi.md#devicegetcontainers) | **GET** /devices/{device_id}/containers | List containers
[**DeviceGetdockerport**](DevicesApi.md#devicegetdockerport) | **GET** /devices/{device_id}/docker/port | Get local port for remote docker tunnel
[**DeviceGetimages**](DevicesApi.md#devicegetimages) | **GET** /devices/{device_id}/images | List container images on the device
[**DeviceGetmemory**](DevicesApi.md#devicegetmemory) | **GET** /devices/{device_id}/memory | Get device memory information
[**DeviceGetmountpoints**](DevicesApi.md#devicegetmountpoints) | **GET** /devices/{device_id}/storage | Get storage information for a device
[**DeviceGetprivatekey**](DevicesApi.md#devicegetprivatekey) | **GET** /devices/{device_id}/privatekey | Return the path of the device private key
[**DeviceGetprocesses**](DevicesApi.md#devicegetprocesses) | **GET** /devices/{device_id}/processes | Get list of processes
[**DeviceGetsshport**](DevicesApi.md#devicegetsshport) | **GET** /devices/{device_id}/ssh/port | Get local port for shell
[**DeviceModify**](DevicesApi.md#devicemodify) | **PUT** /devices/{device_id} | Change device properties
[**DeviceOpendocker**](DevicesApi.md#deviceopendocker) | **GET** /devices/{device_id}/docker/open | Expose remote docker
[**DeviceOpenssh**](DevicesApi.md#deviceopenssh) | **GET** /devices/{device_id}/ssh/open | Expose shell via SSH
[**DeviceReboot**](DevicesApi.md#devicereboot) | **GET** /devices/{device_id}/reboot | Reboot the device
[**DeviceShutdown**](DevicesApi.md#deviceshutdown) | **GET** /devices/{device_id}/shutdown | Shutdown the device
[**DeviceSyncfolders**](DevicesApi.md#devicesyncfolders) | **GET** /devices/{device_id}/syncfolders | Synchronize folders
[**DeviceUpdate**](DevicesApi.md#deviceupdate) | **GET** /devices/{device_id}/update | Update device information
[**DevicesGet**](DevicesApi.md#devicesget) | **GET** /devices | Get all devices
[**DevicesNetworkdetect**](DevicesApi.md#devicesnetworkdetect) | **GET** /devices/network_detect | Detect a network device
[**DevicesSerialdetect**](DevicesApi.md#devicesserialdetect) | **GET** /devices/serial_detect | Detect a serial device
[**ImagesDeleteimage**](DevicesApi.md#imagesdeleteimage) | **DELETE** /devices/{device_id}/images/{image_id} | Delete a container image
[**ImagesGetimage**](DevicesApi.md#imagesgetimage) | **GET** /devices/{device_id}/images/{image_id} | Get information about an image



## ContainerGetlogs

> string ContainerGetlogs (string deviceId, string containerId, bool? restart = null)

Return text lines from the container logs

Return one or more lines from the log, waiting until it's available, this will allow clients to show logs in almost real time

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class ContainerGetlogsExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container
            var restart = false;  // bool? | when true reads the lock back from beginning (optional)  (default to false)

            try
            {
                // Return text lines from the container logs
                string result = apiInstance.ContainerGetlogs(deviceId, containerId, restart);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.ContainerGetlogs: " + e.Message );
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
| **200** | Text from the logs |  -  |
| **204** | No content, container is no longer running and log has ben fully read |  -  |
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerGetmemory

> MemInfo ContainerGetmemory (string deviceId, string containerId)

Return container memory information

Return total/free/available memory on a specific container running on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

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
| **200** | Memory information |  -  |
| **404** | Device or container not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ContainerGetmountpoints

> List&lt;MountPoint&gt; ContainerGetmountpoints (string deviceId, string containerId)

Return information about storage

Return a list of mount points available inside the container

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Return information about storage
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
| **200** | List of mount point information |  -  |
| **404** | Device or container not found |  -  |
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

Get processes running in container

Return a list of processes running in the specified container on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Get processes running in container
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
| **200** | List of processes |  -  |
| **404** | Device or container not found |  -  |
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

Starts container

Start a specified container on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Starts container
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
| **200** | Container information |  -  |
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

Stop container

Stop a specified container running on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Stop container
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

Delete a container

Stops and removes a container running on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Delete a container
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

Get information about a container

Get detailed information on a specific container running on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var containerId = "containerId_example";  // string | Id of a container

            try
            {
                // Get information about a container
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
| **200** | Container information |  -  |
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

Close SSH tunnel for docker API

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Close SSH tunnel for docker API
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

Close SSH tunnel for shell

Stop exposing remote shell port on localhost

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Close SSH tunnel for shell
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


## DeviceCurrentIp

> string DeviceCurrentIp (string deviceId)

Get current ip of the device

Return current ip of the device using local DNS and mDNS

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceCurrentIpExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get current ip of the device
                string result = apiInstance.DeviceCurrentIp(deviceId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceCurrentIp: " + e.Message );
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
| **200** | ip |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceDelete

> void DeviceDelete (string deviceId)

Remove a device

Permanently remove a device from the list of configured ones

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
            var deviceId = "deviceId_example";  // string | Target device serial number

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
| **204** | Device was correctly removed |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGet

> TargetDevice DeviceGet (string deviceId)

Get device

Return a specific configured device, knowing its id

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
            var deviceId = "deviceId_example";  // string | Target device serial number

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
| **200** | Device Information |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetcontainers

> List&lt;DockerContainer&gt; DeviceGetcontainers (string deviceId)

List containers

Get a list of the containers on a specific device

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // List containers
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
| **200** | List of containers |  -  |
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

Get local port for remote docker tunnel

Get local port where docker is tunneled via SSH

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get local port for remote docker tunnel
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
| **200** | Local port for docker interface |  -  |
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

List container images on the device

Get list of all container images available on a specified device

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // List container images on the device
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
| **200** | List of container images |  -  |
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

Get device memory information

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get device memory information
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
| **200** | Memory information |  -  |
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

Get storage information for a device

Return a list with information about every mountpoint

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get storage information for a device
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
| **200** | List of mount point information |  -  |
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

Return the path of the device private key

Returns the file containing the key that can be used to activate passowordless connections to the device

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Return the path of the device private key
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
| **200** | Path of the key file |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceGetprocesses

> List&lt;Process&gt; DeviceGetprocesses (string deviceId)

Get list of processes

Get list of processes running on a specified device

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get list of processes
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
| **200** | List of processes |  -  |
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

Get local port for shell

Get local port where remote shell is tunneled via SSH

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Get local port for shell
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
| **200** | Local port for SSH shell |  -  |
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

Changes specified properties on a configured device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
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
| **200** | Device information |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceOpendocker

> int DeviceOpendocker (string deviceId, int? port = null)

Expose remote docker

Expose remote docker port on localhost via SSH tunnel

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var port = 56;  // int? |  (optional) 

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
 **port** | **int?**|  | [optional] 

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
| **200** | Local port for docker interface |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceOpenssh

> int DeviceOpenssh (string deviceId, int? port = null)

Expose shell via SSH

Expose remote shell on local port via SSH

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var port = 56;  // int? |  (optional) 

            try
            {
                // Expose shell via SSH
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
 **port** | **int?**|  | [optional] 

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
| **200** | Local port for SSH shell |  -  |
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceReboot

> void DeviceReboot (string deviceId, string password)

Reboot the device

Perform a reboot on a specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceRebootExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = "deviceId_example";  // string | Target device serial number
            var password = "password_example";  // string | 

            try
            {
                // Reboot the device
                apiInstance.DeviceReboot(deviceId, password);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceReboot: " + e.Message );
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
 **password** | **string**|  | 

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
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceShutdown

> void DeviceShutdown (string deviceId, string password)

Shutdown the device

Perform a shutdown on a specified device

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TorizonRestAPI.Api;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace Example
{
    public class DeviceShutdownExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "http://localhost:5000/api";
            var apiInstance = new DevicesApi(Configuration.Default);
            var deviceId = "deviceId_example";  // string | Target device serial number
            var password = "password_example";  // string | 

            try
            {
                // Shutdown the device
                apiInstance.DeviceShutdown(deviceId, password);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling DevicesApi.DeviceShutdown: " + e.Message );
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
 **password** | **string**|  | 

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
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceSyncfolders

> void DeviceSyncfolders (string deviceId, string sourcefolder, string destfolder, string progressId = null)

Synchronize folders

Synchronize folders between host and target

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var sourcefolder = "sourcefolder_example";  // string | 
            var destfolder = "destfolder_example";  // string | 
            var progressId = "progressId_example";  // string | Id of a progress cookie (uuid) (optional) 

            try
            {
                // Synchronize folders
                apiInstance.DeviceSyncfolders(deviceId, sourcefolder, destfolder, progressId);
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
| **404** | Device not found |  -  |
| **500** | Unexpected exception. |  -  |
| **520** | Container image not found on local host. |  -  |
| **523** | Container is not running. |  -  |
| **533** | SSH error. |  -  |
| **544** | Local command execution failed. |  -  |
| **551** | Operation has been aborted |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeviceUpdate

> TargetDevice DeviceUpdate (string deviceId)

Update device information

Checks for updates on the remote device and return up-to-date information

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
            var deviceId = "deviceId_example";  // string | Target device serial number

            try
            {
                // Update device information
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
| **200** | Device information |  -  |
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
| **200** | Devices list |  -  |
| **500** | Unexpected exception. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DevicesNetworkdetect

> TargetDevice DevicesNetworkdetect (string hostname, string username, string password)

Detect a network device

Detect a device using its ip or hostname

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
            var hostname = "hostname_example";  // string | 
            var username = "username_example";  // string | 
            var password = "password_example";  // string | 

            try
            {
                // Detect a network device
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
| **200** | Device information |  -  |
| **500** | Unexpected exception. |  -  |
| **524** | User is not enable to execute commands as root. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **533** | SSH error. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |
| **546** | Device information is not valid. |  -  |
| **547** | Model id not recognized. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DevicesSerialdetect

> TargetDevice DevicesSerialdetect (string port, string username, string password)

Detect a serial device

Detect a device connected to a local serial port

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
            var port = "port_example";  // string | 
            var username = "username_example";  // string | 
            var password = "password_example";  // string | 

            try
            {
                // Detect a serial device
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
| **200** | Device information |  -  |
| **500** | Unexpected exception. |  -  |
| **524** | User is not enable to execute commands as root. |  -  |
| **531** | Object Does not have a valid id. |  -  |
| **532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
| **534** | OS error. |  -  |
| **535** | Invalid device id. |  -  |
| **536** | Serial port error. |  -  |
| **537** | Command timeout. |  -  |
| **538** | Login failed. |  -  |
| **546** | Device information is not valid. |  -  |
| **547** | Model id not recognized. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ImagesDeleteimage

> void ImagesDeleteimage (string deviceId, string imageId)

Delete a container image

Delete a specific container image from the device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var imageId = "imageId_example";  // string | Id of an image

            try
            {
                // Delete a container image
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

Get information about an image

Get detailed information on a specific container image stored on a device

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
            var deviceId = "deviceId_example";  // string | Target device serial number
            var imageId = "imageId_example";  // string | Id of an image

            try
            {
                // Get information about an image
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
| **200** | Container image information |  -  |
| **404** | Device or Image not found |  -  |
| **500** | Unexpected exception. |  -  |
| **525** | Remote docker exception. |  -  |
| **533** | SSH error. |  -  |
| **539** | SSH tunnel error. |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

