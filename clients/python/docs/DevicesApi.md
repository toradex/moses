# moses_client.DevicesApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**container_getlogs**](DevicesApi.md#container_getlogs) | **GET** /devices/{device_id}/containers/{container_id}/logs | Return text lines from the container logs
[**container_getmemory**](DevicesApi.md#container_getmemory) | **GET** /devices/{device_id}/containers/{container_id}/memory | Return container memory information
[**container_getmountpoints**](DevicesApi.md#container_getmountpoints) | **GET** /devices/{device_id}/containers/{container_id}/storage | Return information about storage
[**container_getprocesses**](DevicesApi.md#container_getprocesses) | **GET** /devices/{device_id}/containers/{container_id}/processes | Get processes running in container
[**container_start**](DevicesApi.md#container_start) | **GET** /devices/{device_id}/containers/{container_id}/start | Starts container
[**container_stop**](DevicesApi.md#container_stop) | **GET** /devices/{device_id}/containers/{container_id}/stop | Stop container
[**containers_deletecontainer**](DevicesApi.md#containers_deletecontainer) | **DELETE** /devices/{device_id}/containers/{container_id} | Delete a container
[**containers_getcontainer**](DevicesApi.md#containers_getcontainer) | **GET** /devices/{device_id}/containers/{container_id} | Get information about a container
[**device_closedocker**](DevicesApi.md#device_closedocker) | **GET** /devices/{device_id}/docker/close | Close SSH tunnel for docker API
[**device_closessh**](DevicesApi.md#device_closessh) | **GET** /devices/{device_id}/ssh/close | Close SSH tunnel for shell
[**device_current_ip**](DevicesApi.md#device_current_ip) | **GET** /devices/{device_id}/current_ip | Get current ip of the device
[**device_delete**](DevicesApi.md#device_delete) | **DELETE** /devices/{device_id} | Remove a device
[**device_get**](DevicesApi.md#device_get) | **GET** /devices/{device_id} | Get device
[**device_getcontainers**](DevicesApi.md#device_getcontainers) | **GET** /devices/{device_id}/containers | List containers
[**device_getdockerport**](DevicesApi.md#device_getdockerport) | **GET** /devices/{device_id}/docker/port | Get local port for remote docker tunnel
[**device_getimages**](DevicesApi.md#device_getimages) | **GET** /devices/{device_id}/images | List container images on the device
[**device_getmemory**](DevicesApi.md#device_getmemory) | **GET** /devices/{device_id}/memory | Get device memory information
[**device_getmountpoints**](DevicesApi.md#device_getmountpoints) | **GET** /devices/{device_id}/storage | Get storage information for a device
[**device_getprivatekey**](DevicesApi.md#device_getprivatekey) | **GET** /devices/{device_id}/privatekey | Return the path of the device private key
[**device_getprocesses**](DevicesApi.md#device_getprocesses) | **GET** /devices/{device_id}/processes | Get list of processes
[**device_getsshport**](DevicesApi.md#device_getsshport) | **GET** /devices/{device_id}/ssh/port | Get local port for shell
[**device_modify**](DevicesApi.md#device_modify) | **PUT** /devices/{device_id} | Change device properties
[**device_opendocker**](DevicesApi.md#device_opendocker) | **GET** /devices/{device_id}/docker/open | Expose remote docker
[**device_openssh**](DevicesApi.md#device_openssh) | **GET** /devices/{device_id}/ssh/open | Expose shell via SSH
[**device_reboot**](DevicesApi.md#device_reboot) | **GET** /devices/{device_id}/reboot | Reboot the device
[**device_shutdown**](DevicesApi.md#device_shutdown) | **GET** /devices/{device_id}/shutdown | Shutdown the device
[**device_syncfolders**](DevicesApi.md#device_syncfolders) | **GET** /devices/{device_id}/syncfolders | Synchronize folders
[**device_update**](DevicesApi.md#device_update) | **GET** /devices/{device_id}/update | Update device information
[**device_validate_parameter**](DevicesApi.md#device_validate_parameter) | **GET** /devices/{device_id}/validate_parameter | Validates a value for a parameter
[**devices_get**](DevicesApi.md#devices_get) | **GET** /devices | Get all devices
[**devices_networkdetect**](DevicesApi.md#devices_networkdetect) | **GET** /devices/network_detect | Detect a network device
[**devices_serialdetect**](DevicesApi.md#devices_serialdetect) | **GET** /devices/serial_detect | Detect a serial device
[**images_deleteimage**](DevicesApi.md#images_deleteimage) | **DELETE** /devices/{device_id}/images/{image_id} | Delete a container image
[**images_getimage**](DevicesApi.md#images_getimage) | **GET** /devices/{device_id}/images/{image_id} | Get information about an image


# **container_getlogs**
> str container_getlogs(device_id, container_id)

Return text lines from the container logs

Return one or more lines from the log, waiting until it's available, this will allow clients to show logs in almost real time

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container
    restart = False # bool | when true reads the lock back from beginning (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Return text lines from the container logs
        api_response = api_instance.container_getlogs(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_getlogs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return text lines from the container logs
        api_response = api_instance.container_getlogs(device_id, container_id, restart=restart)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_getlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |
 **restart** | **bool**| when true reads the lock back from beginning | [optional] if omitted the server will use the default value of False

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Text from the logs |  -  |
**204** | No content, container is no longer running and log has ben fully read |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_getmemory**
> MemInfo container_getmemory(device_id, container_id)

Return container memory information

Return total/free/available memory on a specific container running on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.mem_info import MemInfo
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Return container memory information
        api_response = api_instance.container_getmemory(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_getmemory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

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
**200** | Memory information |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_getmountpoints**
> [MountPoint] container_getmountpoints(device_id, container_id)

Return information about storage

Return a list of mount points available inside the container

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.mount_point import MountPoint
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Return information about storage
        api_response = api_instance.container_getmountpoints(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_getmountpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

### Return type

[**[MountPoint]**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of mount point information |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_getprocesses**
> [Process] container_getprocesses(device_id, container_id)

Get processes running in container

Return a list of processes running in the specified container on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.process import Process
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Get processes running in container
        api_response = api_instance.container_getprocesses(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_getprocesses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

### Return type

[**[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of processes |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_start**
> DockerContainer container_start(device_id, container_id)

Starts container

Start a specified container on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.docker_container import DockerContainer
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Starts container
        api_response = api_instance.container_start(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

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
**200** | Container information |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_stop**
> DockerContainer container_stop(device_id, container_id)

Stop container

Stop a specified container running on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.docker_container import DockerContainer
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Stop container
        api_response = api_instance.container_stop(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->container_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

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
**200** | Returns container |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **containers_deletecontainer**
> containers_deletecontainer(device_id, container_id)

Delete a container

Stops and removes a container running on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Delete a container
        api_instance.containers_deletecontainer(device_id, container_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->containers_deletecontainer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

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
**204** | OK |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **containers_getcontainer**
> DockerContainer containers_getcontainer(device_id, container_id)

Get information about a container

Get detailed information on a specific container running on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.docker_container import DockerContainer
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    container_id = "555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of a container

    # example passing only required values which don't have defaults set
    try:
        # Get information about a container
        api_response = api_instance.containers_getcontainer(device_id, container_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->containers_getcontainer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **container_id** | **str**| Id of a container |

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
**200** | Container information |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_closedocker**
> device_closedocker(device_id)

Close SSH tunnel for docker API

Stop exposing remote docker port on localhost

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Close SSH tunnel for docker API
        api_instance.device_closedocker(device_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_closedocker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | OK |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_closessh**
> device_closessh(device_id)

Close SSH tunnel for shell

Stop exposing remote shell port on localhost

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Close SSH tunnel for shell
        api_instance.device_closessh(device_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_closessh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | OK |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_current_ip**
> str device_current_ip(device_id)

Get current ip of the device

Return current ip of the device using local DNS and mDNS

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get current ip of the device
        api_response = api_instance.device_current_ip(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_current_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ip |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**534** | OS error. |  -  |
**535** | Invalid device id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete**
> device_delete(device_id)

Remove a device

Permanently remove a device from the list of configured ones

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Remove a device
        api_instance.device_delete(device_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**204** | Device was correctly removed |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get**
> TargetDevice device_get(device_id)

Get device

Return a specific configured device, knowing its id

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get device
        api_response = api_instance.device_get(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | Device Information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getcontainers**
> [DockerContainer] device_getcontainers(device_id)

List containers

Get a list of the containers on a specific device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.docker_container import DockerContainer
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # List containers
        api_response = api_instance.device_getcontainers(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getcontainers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

[**[DockerContainer]**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of containers |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getdockerport**
> int device_getdockerport(device_id)

Get local port for remote docker tunnel

Get local port where docker is tunneled via SSH

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get local port for remote docker tunnel
        api_response = api_instance.device_getdockerport(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getdockerport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | Local port for docker interface |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getimages**
> [DockerImage] device_getimages(device_id)

List container images on the device

Get list of all container images available on a specified device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.docker_image import DockerImage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # List container images on the device
        api_response = api_instance.device_getimages(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getimages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

[**[DockerImage]**](DockerImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of container images |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getmemory**
> MemInfo device_getmemory(device_id)

Get device memory information

Return total/free/available memory on the device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.mem_info import MemInfo
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get device memory information
        api_response = api_instance.device_getmemory(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getmemory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | Memory information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getmountpoints**
> [MountPoint] device_getmountpoints(device_id)

Get storage information for a device

Return a list with information about every mountpoint

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.mount_point import MountPoint
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get storage information for a device
        api_response = api_instance.device_getmountpoints(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getmountpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

[**[MountPoint]**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of mount point information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getprivatekey**
> str device_getprivatekey(device_id)

Return the path of the device private key

Returns the file containing the key that can be used to activate passowordless connections to the device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Return the path of the device private key
        api_response = api_instance.device_getprivatekey(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getprivatekey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Path of the key file |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getprocesses**
> [Process] device_getprocesses(device_id)

Get list of processes

Get list of processes running on a specified device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.process import Process
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get list of processes
        api_response = api_instance.device_getprocesses(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getprocesses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

### Return type

[**[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of processes |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getsshport**
> int device_getsshport(device_id)

Get local port for shell

Get local port where remote shell is tunneled via SSH

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get local port for shell
        api_response = api_instance.device_getsshport(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_getsshport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | Local port for SSH shell |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_modify**
> TargetDevice device_modify(device_id)

Change device properties

Changes specified properties on a configured device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    device = TargetDevice(
        name="Colibri imx7 EVB",
        hostname="verdin-imx8mm-06632494",
        username="torizon",
        homefolder="/home/torizon",
    ) # TargetDevice |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change device properties
        api_response = api_instance.device_modify(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_modify: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change device properties
        api_response = api_instance.device_modify(device_id, device=device)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_modify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
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
**200** | Device information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_opendocker**
> int device_opendocker(device_id)

Expose remote docker

Expose remote docker port on localhost via SSH tunnel

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    port = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Expose remote docker
        api_response = api_instance.device_opendocker(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_opendocker: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Expose remote docker
        api_response = api_instance.device_opendocker(device_id, port=port)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_opendocker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
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
**200** | Local port for docker interface |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_openssh**
> int device_openssh(device_id)

Expose shell via SSH

Expose remote shell on local port via SSH

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    port = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Expose shell via SSH
        api_response = api_instance.device_openssh(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_openssh: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Expose shell via SSH
        api_response = api_instance.device_openssh(device_id, port=port)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_openssh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
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
**200** | Local port for SSH shell |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_reboot**
> device_reboot(device_id, password)

Reboot the device

Perform a reboot on a specified device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    password = "password_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reboot the device
        api_instance.device_reboot(device_id, password)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_reboot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **password** | **str**|  |

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
**200** | OK |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_shutdown**
> device_shutdown(device_id, password)

Shutdown the device

Perform a shutdown on a specified device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    password = "password_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Shutdown the device
        api_instance.device_shutdown(device_id, password)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_shutdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **password** | **str**|  |

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
**200** | OK |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_syncfolders**
> device_syncfolders(device_id, sourcefolder, destfolder)

Synchronize folders

Synchronize folders between host and target

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    sourcefolder = "sourcefolder_example" # str | 
    destfolder = "destfolder_example" # str | 
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Synchronize folders
        api_instance.device_syncfolders(device_id, sourcefolder, destfolder)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_syncfolders: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Synchronize folders
        api_instance.device_syncfolders(device_id, sourcefolder, destfolder, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_syncfolders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **sourcefolder** | **str**|  |
 **destfolder** | **str**|  |
 **progress_id** | **str**| Id of a progress cookie (uuid) | [optional]

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
**200** | OK |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**523** | Container is not running. |  -  |
**533** | SSH error. |  -  |
**544** | Local command execution failed. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> TargetDevice device_update(device_id)

Update device information

Checks for updates on the remote device and return up-to-date information

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Update device information
        api_response = api_instance.device_update(device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |

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
**200** | Device information |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**533** | SSH error. |  -  |
**534** | OS error. |  -  |
**535** | Invalid device id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_validate_parameter**
> ValidationResult device_validate_parameter(device_id, parameter, value)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.validation_result import ValidationResult
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    parameter = "parameter_example" # str | 
    value = "value_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Validates a value for a parameter
        api_response = api_instance.device_validate_parameter(device_id, parameter, value)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->device_validate_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **parameter** | **str**|  |
 **value** | **str**|  |

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
**200** | Validation results |  -  |
**500** | Unexpected exception. |  -  |
**535** | Invalid device id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> [TargetDevice] devices_get()

Get all devices

Returns all configured devices

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all devices
        api_response = api_instance.devices_get()
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->devices_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TargetDevice]**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Devices list |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_networkdetect**
> TargetDevice devices_networkdetect(hostname, username, password)

Detect a network device

Detect a device using its ip or hostname

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    hostname = "hostname_example" # str | 
    username = "username_example" # str | 
    password = "password_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Detect a network device
        api_response = api_instance.devices_networkdetect(hostname, username, password)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->devices_networkdetect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  |
 **username** | **str**|  |
 **password** | **str**|  |

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
**200** | Device information |  -  |
**500** | Unexpected exception. |  -  |
**524** | User is not enable to execute commands as root. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**533** | SSH error. |  -  |
**534** | OS error. |  -  |
**535** | Invalid device id. |  -  |
**546** | Device information is not valid. |  -  |
**547** | Model id not recognized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_serialdetect**
> TargetDevice devices_serialdetect(port, username, password)

Detect a serial device

Detect a device connected to a local serial port

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.target_device import TargetDevice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    port = "port_example" # str | 
    username = "username_example" # str | 
    password = "password_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Detect a serial device
        api_response = api_instance.devices_serialdetect(port, username, password)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->devices_serialdetect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**|  |
 **username** | **str**|  |
 **password** | **str**|  |

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
**200** | Device information |  -  |
**500** | Unexpected exception. |  -  |
**524** | User is not enable to execute commands as root. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**534** | OS error. |  -  |
**535** | Invalid device id. |  -  |
**536** | Serial port error. |  -  |
**537** | Command timeout. |  -  |
**538** | Login failed. |  -  |
**546** | Device information is not valid. |  -  |
**547** | Model id not recognized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_deleteimage**
> images_deleteimage(device_id, image_id)

Delete a container image

Delete a specific container image from the device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    image_id = "sha256:555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of an image

    # example passing only required values which don't have defaults set
    try:
        # Delete a container image
        api_instance.images_deleteimage(device_id, image_id)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->images_deleteimage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **image_id** | **str**| Id of an image |

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
**204** | OK |  -  |
**404** | Device or image not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_getimage**
> DockerImage images_getimage(device_id, image_id)

Get information about an image

Get detailed information on a specific container image stored on a device

### Example


```python
import time
import moses_client
from moses_client.api import devices_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.docker_image import DockerImage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = devices_api.DevicesApi(api_client)
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    image_id = "sha256:555914d4d6Ea18e3e53E03fEE4Bc7d,,c0d281Fb40cDe1Fd7eaf49b6d348c6Fc" # str | Id of an image

    # example passing only required values which don't have defaults set
    try:
        # Get information about an image
        api_response = api_instance.images_getimage(device_id, image_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling DevicesApi->images_getimage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number |
 **image_id** | **str**| Id of an image |

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
**200** | Container image information |  -  |
**404** | Device or Image not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

