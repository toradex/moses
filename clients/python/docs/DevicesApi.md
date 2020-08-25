# moses_client.DevicesApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**container_getlogs**](DevicesApi.md#container_getlogs) | **GET** /devices/{device_id}/containers/{container_id}/logs | return container logs one chunk a time
[**container_getmemory**](DevicesApi.md#container_getmemory) | **GET** /devices/{device_id}/containers/{container_id}/memory | Return container memory information
[**container_getmountpoints**](DevicesApi.md#container_getmountpoints) | **GET** /devices/{device_id}/containers/{container_id}/storage | return information about storage
[**container_getprocesses**](DevicesApi.md#container_getprocesses) | **GET** /devices/{device_id}/containers/{container_id}/processes | return processes running in container
[**container_start**](DevicesApi.md#container_start) | **GET** /devices/{device_id}/containers/{container_id}/start | starts container
[**container_stop**](DevicesApi.md#container_stop) | **GET** /devices/{device_id}/containers/{container_id}/stop | stops container
[**containers_deletecontainer**](DevicesApi.md#containers_deletecontainer) | **DELETE** /devices/{device_id}/containers/{container_id} | delete a container
[**containers_getcontainer**](DevicesApi.md#containers_getcontainer) | **GET** /devices/{device_id}/containers/{container_id} | get container details
[**device_closedocker**](DevicesApi.md#device_closedocker) | **GET** /devices/{device_id}/docker/close | Disables remote docker
[**device_closessh**](DevicesApi.md#device_closessh) | **GET** /devices/{device_id}/ssh/close | Disables ssh tunneling
[**device_current_ip**](DevicesApi.md#device_current_ip) | **GET** /devices/{device_id}/current_ip | returns current ip of the device
[**device_delete**](DevicesApi.md#device_delete) | **DELETE** /devices/{device_id} | Remove a device
[**device_get**](DevicesApi.md#device_get) | **GET** /devices/{device_id} | Get device
[**device_getcontainers**](DevicesApi.md#device_getcontainers) | **GET** /devices/{device_id}/containers | list containers
[**device_getdockerport**](DevicesApi.md#device_getdockerport) | **GET** /devices/{device_id}/docker/port | remote docker local port
[**device_getimages**](DevicesApi.md#device_getimages) | **GET** /devices/{device_id}/images | list images
[**device_getmemory**](DevicesApi.md#device_getmemory) | **GET** /devices/{device_id}/memory | Return memory information
[**device_getmountpoints**](DevicesApi.md#device_getmountpoints) | **GET** /devices/{device_id}/storage | return storage information for a device
[**device_getprivatekey**](DevicesApi.md#device_getprivatekey) | **GET** /devices/{device_id}/privatekey | return the path of the device private key
[**device_getprocesses**](DevicesApi.md#device_getprocesses) | **GET** /devices/{device_id}/processes | list running processes on a device
[**device_getsshport**](DevicesApi.md#device_getsshport) | **GET** /devices/{device_id}/ssh/port | remote ssh local port
[**device_modify**](DevicesApi.md#device_modify) | **PUT** /devices/{device_id} | Change device properties
[**device_opendocker**](DevicesApi.md#device_opendocker) | **GET** /devices/{device_id}/docker/open | Expose remote docker
[**device_openssh**](DevicesApi.md#device_openssh) | **GET** /devices/{device_id}/ssh/open | Expose remote ssh
[**device_syncfolders**](DevicesApi.md#device_syncfolders) | **GET** /devices/{device_id}/syncfolders | synchronizes folders
[**device_update**](DevicesApi.md#device_update) | **GET** /devices/{device_id}/update | update information for a specific device
[**devices_get**](DevicesApi.md#devices_get) | **GET** /devices | Get all devices
[**devices_networkdetect**](DevicesApi.md#devices_networkdetect) | **GET** /devices/network_detect | Finds a network device
[**devices_serialdetect**](DevicesApi.md#devices_serialdetect) | **GET** /devices/serial_detect | Finds a device connected to serial port
[**images_deleteimage**](DevicesApi.md#images_deleteimage) | **DELETE** /devices/{device_id}/images/{image_id} | delete an image
[**images_getimage**](DevicesApi.md#images_getimage) | **GET** /devices/{device_id}/images/{image_id} | get image details


# **container_getlogs**
> str container_getlogs(device_id, container_id, restart=restart)

return container logs one chunk a time

return one or more lines of the log, waiting until it's available, this will allow clients to show logs in almost real time

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container
restart = False # bool | when true reads the lock back from beginning (optional) (default to False)

    try:
        # return container logs one chunk a time
        api_response = api_instance.container_getlogs(device_id, container_id, restart=restart)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->container_getlogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 
 **container_id** | **str**| Id of a container | 
 **restart** | **bool**| when true reads the lock back from beginning | [optional] [default to False]

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
**200** | Returns list of storage informations |  -  |
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

Return total/free/available memory on a specific container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # Return container memory information
        api_response = api_instance.container_getmemory(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns memory information |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_getmountpoints**
> list[MountPoint] container_getmountpoints(device_id, container_id)

return information about storage

returns a list of storages available inside the container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # return information about storage
        api_response = api_instance.container_getmountpoints(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->container_getmountpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 
 **container_id** | **str**| Id of a container | 

### Return type

[**list[MountPoint]**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of storage informations |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_getprocesses**
> list[Process] container_getprocesses(device_id, container_id)

return processes running in container

returns a list of processes running in the specified container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # return processes running in container
        api_response = api_instance.container_getprocesses(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->container_getprocesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 
 **container_id** | **str**| Id of a container | 

### Return type

[**list[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of processes |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_start**
> DockerContainer container_start(device_id, container_id)

starts container

Start specified container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # starts container
        api_response = api_instance.container_start(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns container |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_stop**
> DockerContainer container_stop(device_id, container_id)

stops container

Stops specified container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # stops container
        api_response = api_instance.container_stop(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
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

delete a container

Executes rm command on container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # delete a container
        api_instance.containers_deletecontainer(device_id, container_id)
    except ApiException as e:
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

get container details

Get detailed information on a specific container

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
container_id = 'container_id_example' # str | Id of a container

    try:
        # get container details
        api_response = api_instance.containers_getcontainer(device_id, container_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns container |  -  |
**404** | Device or container not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_closedocker**
> device_closedocker(device_id)

Disables remote docker

Stop exposing remote docker port on localhost

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # Disables remote docker
        api_instance.device_closedocker(device_id)
    except ApiException as e:
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

Disables ssh tunneling

Stop exposing remote ssh port on localhost

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # Disables ssh tunneling
        api_instance.device_closessh(device_id)
    except ApiException as e:
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

returns current ip of the device

Returns current ip of the device using local DNS and mDNS

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # returns current ip of the device
        api_response = api_instance.device_current_ip(device_id)
        pprint(api_response)
    except ApiException as e:
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

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # Remove a device
        api_instance.device_delete(device_id)
    except ApiException as e:
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
**204** | Device was correctly deleted |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get**
> TargetDevice device_get(device_id)

Get device

Returns a specified device, knowing its id

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # Get device
        api_response = api_instance.device_get(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns device |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getcontainers**
> list[DockerContainer] device_getcontainers(device_id)

list containers

Get containers running on a specified device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # list containers
        api_response = api_instance.device_getcontainers(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_getcontainers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 

### Return type

[**list[DockerContainer]**](DockerContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of containers |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getdockerport**
> int device_getdockerport(device_id)

remote docker local port

Get local port where docker is tunneled

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # remote docker local port
        api_response = api_instance.device_getdockerport(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns port |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getimages**
> list[DockerImage] device_getimages(device_id)

list images

Get images available on a specified device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # list images
        api_response = api_instance.device_getimages(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_getimages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 

### Return type

[**list[DockerImage]**](DockerImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of images |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getmemory**
> MemInfo device_getmemory(device_id)

Return memory information

Return total/free/available memory on the device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # Return memory information
        api_response = api_instance.device_getmemory(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns memory information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getmountpoints**
> list[MountPoint] device_getmountpoints(device_id)

return storage information for a device

Get a list of storages for the specified device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # return storage information for a device
        api_response = api_instance.device_getmountpoints(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_getmountpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 

### Return type

[**list[MountPoint]**](MountPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of storage information |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getprivatekey**
> str device_getprivatekey(device_id)

return the path of the device private key

returns the key that can be used to activate passowordless connections to the device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # return the path of the device private key
        api_response = api_instance.device_getprivatekey(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Path of the private key file |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getprocesses**
> list[Process] device_getprocesses(device_id)

list running processes on a device

Get processes running on a specified device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # list running processes on a device
        api_response = api_instance.device_getprocesses(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_getprocesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 

### Return type

[**list[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of processes |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_getsshport**
> int device_getsshport(device_id)

remote ssh local port

Get local port where ssh is tunneled

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # remote ssh local port
        api_response = api_instance.device_getsshport(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns port |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_modify**
> TargetDevice device_modify(device_id, device=device)

Change device properties

Changes specified properties on a device

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
device = moses_client.TargetDevice() # TargetDevice |  (optional)

    try:
        # Change device properties
        api_response = api_instance.device_modify(device_id, device=device)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns device |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_opendocker**
> int device_opendocker(device_id, port=port)

Expose remote docker

Expose remote docker port on localhost

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
port = 56 # int |  (optional)

    try:
        # Expose remote docker
        api_response = api_instance.device_opendocker(device_id, port=port)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns port |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_openssh**
> int device_openssh(device_id, port=port)

Expose remote ssh

Expose remote ssh port on localhost

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
port = 56 # int |  (optional)

    try:
        # Expose remote ssh
        api_response = api_instance.device_openssh(device_id, port=port)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns port |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_syncfolders**
> device_syncfolders(device_id, sourcefolder, destfolder)

synchronizes folders

synchronizes folders between host and target

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
sourcefolder = 'sourcefolder_example' # str | 
destfolder = 'destfolder_example' # str | 

    try:
        # synchronizes folders
        api_instance.device_syncfolders(device_id, sourcefolder, destfolder)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_syncfolders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device serial number | 
 **sourcefolder** | **str**|  | 
 **destfolder** | **str**|  | 

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
**200** | Sysroot updated |  -  |
**404** | Device not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**523** | Container is not running. |  -  |
**533** | SSH error. |  -  |
**544** | Local command execution failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> TargetDevice device_update(device_id)

update information for a specific device

Returns a specified device, with updated info if available

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number

    try:
        # update information for a specific device
        api_response = api_instance.device_update(device_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns device |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**533** | SSH error. |  -  |
**534** | OS error. |  -  |
**535** | Invalid device id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> list[TargetDevice] devices_get()

Get all devices

Returns all configured devices

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    
    try:
        # Get all devices
        api_response = api_instance.devices_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TargetDevice]**](TargetDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_networkdetect**
> TargetDevice devices_networkdetect(hostname, username, password)

Finds a network device

Returns a new device detected from network

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    hostname = 'hostname_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

    try:
        # Finds a network device
        api_response = api_instance.devices_networkdetect(hostname, username, password)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns device |  -  |
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

Finds a device connected to serial port

Returns a new device detected from serial port

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    port = 'port_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

    try:
        # Finds a device connected to serial port
        api_response = api_instance.devices_serialdetect(port, username, password)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns device |  -  |
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

delete an image

Executes rmi command on and image

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
image_id = 'image_id_example' # str | Id of an image

    try:
        # delete an image
        api_instance.images_deleteimage(device_id, image_id)
    except ApiException as e:
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

get image details

Get detailed information on an image

### Example

```python
from __future__ import print_function
import time
import moses_client
from moses_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moses_client.DevicesApi(api_client)
    device_id = 'device_id_example' # str | Target device serial number
image_id = 'image_id_example' # str | Id of an image

    try:
        # get image details
        api_response = api_instance.images_getimage(device_id, image_id)
        pprint(api_response)
    except ApiException as e:
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
**200** | Returns image |  -  |
**404** | Device or Image not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

