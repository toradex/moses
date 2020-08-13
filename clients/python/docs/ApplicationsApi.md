# moses_client.ApplicationsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_build**](ApplicationsApi.md#application_build) | **GET** /applications/{application_id}/build | Builds container image
[**application_delete**](ApplicationsApi.md#application_delete) | **DELETE** /applications/{application_id} | Remove an application and all the associated data and containers
[**application_deploy**](ApplicationsApi.md#application_deploy) | **GET** /applications/{application_id}/deploy | Deploys container image
[**application_get**](ApplicationsApi.md#application_get) | **GET** /applications/{application_id} | Get application
[**application_getcontainer**](ApplicationsApi.md#application_getcontainer) | **GET** /applications/{application_id}/container | Get container information
[**application_getcontainer_logs**](ApplicationsApi.md#application_getcontainer_logs) | **GET** /applications/{application_id}/container_logs | Get container log, chunk by chunk
[**application_getdocker_commandline**](ApplicationsApi.md#application_getdocker_commandline) | **GET** /applications/{application_id}/docker_commandline | Get docker command line used to run the container
[**application_getdocker_composefile**](ApplicationsApi.md#application_getdocker_composefile) | **GET** /applications/{application_id}/docker_composefile | Get docker compose file
[**application_getprivatekey**](ApplicationsApi.md#application_getprivatekey) | **GET** /applications/{application_id}/privatekey | Retrieves the path of the RSA private key
[**application_modify**](ApplicationsApi.md#application_modify) | **PUT** /applications/{application_id} | Change application properties
[**application_reseal**](ApplicationsApi.md#application_reseal) | **GET** /applications/{application_id}/reseal | Cleans id and keys for git repo uploading
[**application_run**](ApplicationsApi.md#application_run) | **GET** /applications/{application_id}/run | Runs container image
[**application_runsdk**](ApplicationsApi.md#application_runsdk) | **GET** /applications/{application_id}/sdk/run | Runs SDK containers
[**application_sdk_container**](ApplicationsApi.md#application_sdk_container) | **GET** /applications/{application_id}/sdk/container | Get SDK container
[**application_stop**](ApplicationsApi.md#application_stop) | **GET** /applications/{application_id}/stop | Stops running container image
[**application_syncfolders**](ApplicationsApi.md#application_syncfolders) | **GET** /applications/{application_id}/syncfolders | synchronizes folders
[**application_updated**](ApplicationsApi.md#application_updated) | **GET** /applications/{application_id}/updated | Builds container image
[**application_updatesdk**](ApplicationsApi.md#application_updatesdk) | **GET** /applications/{application_id}/sdk/update | Update SDK container
[**applications_create**](ApplicationsApi.md#applications_create) | **GET** /applications/create | Loads an application configuration
[**applications_load**](ApplicationsApi.md#applications_load) | **GET** /applications/load | Loads an application configuration


# **application_build**
> application_build(application_id, configuration, progress_id=progress_id)

Builds container image

Builds application release or debug container

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # Builds container image
        api_instance.application_build(application_id, configuration, progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
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
**200** | Successful build |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_delete**
> application_delete(application_id)

Remove an application and all the associated data and containers

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)

    try:
        # Remove an application and all the associated data and containers
        api_instance.application_delete(application_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 

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
**204** | Application was correctly deleted |  -  |
**404** | Application no found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_deploy**
> application_deploy(application_id, configuration, deviceid, progress_id=progress_id)

Deploys container image

Deploys application release or debug container to target

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # Deploys container image
        api_instance.application_deploy(application_id, configuration, deviceid, progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_deploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 
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
**200** | Successful build |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get**
> Application application_get(application_id)

Get application

Returns a specified application, knowing its id

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)

    try:
        # Get application
        api_response = api_instance.application_get(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 

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
**200** | Returns application |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getcontainer**
> DockerContainer application_getcontainer(application_id, configuration, deviceid)

Get container information

Get informations about container

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 

    try:
        # Get container information
        api_response = api_instance.application_getcontainer(application_id, configuration, deviceid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_getcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 

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
**200** | Returns application container |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getcontainer_logs**
> str application_getcontainer_logs(application_id, configuration, deviceid, restart=restart)

Get container log, chunk by chunk

Return one chunk of log (one or more lines), blocking if no data is available

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 
restart = False # bool | when true reads the lock back from beginning (optional) (default to False)

    try:
        # Get container log, chunk by chunk
        api_response = api_instance.application_getcontainer_logs(application_id, configuration, deviceid, restart=restart)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_getcontainer_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 
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
**200** | Returns a chunk of logs |  -  |
**204** | No content |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getdocker_commandline**
> str application_getdocker_commandline(application_id, configuration)

Get docker command line used to run the container

returns full command line

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 

    try:
        # Get docker command line used to run the container
        api_response = api_instance.application_getdocker_commandline(application_id, configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_getdocker_commandline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 

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
**200** | Returns command line |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getdocker_composefile**
> str application_getdocker_composefile(application_id, configuration)

Get docker compose file

returns docker compose file that can be used to run the container and its dependencies

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 

    try:
        # Get docker compose file
        api_response = api_instance.application_getdocker_composefile(application_id, configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_getdocker_composefile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 

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
**200** | Docker-compose file as string with *nix line ending |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getprivatekey**
> str application_getprivatekey(application_id)

Retrieves the path of the RSA private key

The application stores the public key inside the container if ssh is enabled, this key will allow passwordless connections to a running instance

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)

    try:
        # Retrieves the path of the RSA private key
        api_response = api_instance.application_getprivatekey(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_getprivatekey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 

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
**200** | key returned |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_modify**
> Application application_modify(application_id, application=application)

Change application properties

Changes specified properties on an applicaton

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
application = moses_client.Application() # Application |  (optional)

    try:
        # Change application properties
        api_response = api_instance.application_modify(application_id, application=application)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
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
**200** | Returns application |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_reseal**
> application_reseal(application_id)

Cleans id and keys for git repo uploading

This operation make the application no longer valid, but allow you to upload it to a git repo from where it can be cloned/forked re-generating new ids every time, avoiding that all clones share the same id/keys.

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)

    try:
        # Cleans id and keys for git repo uploading
        api_instance.application_reseal(application_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_reseal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 

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
**200** | key returned |  -  |
**404** | Application not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_run**
> DockerContainer application_run(application_id, configuration, deviceid, progress_id=progress_id)

Runs container image

Runs application release or debug container on target, if the application is already running, restarts it

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # Runs container image
        api_response = api_instance.application_run(application_id, configuration, deviceid, progress_id=progress_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 
 **progress_id** | **str**| Id of a progress cookie (uuid) | [optional] 

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
**200** | Returns application container |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_runsdk**
> InlineResponse200 application_runsdk(application_id, configuration, build=build, progress_id=progress_id)

Runs SDK containers

Runs SDK container and return its IP and SSH port

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
build = True # bool |  (optional) (default to True)
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # Runs SDK containers
        api_response = api_instance.application_runsdk(application_id, configuration, build=build, progress_id=progress_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_runsdk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **build** | **bool**|  | [optional] [default to True]
 **progress_id** | **str**| Id of a progress cookie (uuid) | [optional] 

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
**200** | Container started |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_sdk_container**
> DockerContainer application_sdk_container(application_id, configuration)

Get SDK container

Get SDK container for check if it is running

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 

    try:
        # Get SDK container
        api_response = api_instance.application_sdk_container(application_id, configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_sdk_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 

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
**200** | Returns application container |  -  |
**204** | No content |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_stop**
> application_stop(application_id, configuration, deviceid)

Stops running container image

Stops application release or debug container currently running on target

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 

    try:
        # Stops running container image
        api_instance.application_stop(application_id, configuration, deviceid)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 

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
**200** | Application stopped (returned also if not running) |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_syncfolders**
> application_syncfolders(application_id, sourcefolder, configuration, deviceid, destfolder, source_is_sdk=source_is_sdk, progress_id=progress_id)

synchronizes folders

synchronizes folders between host/SDK container and application container

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
sourcefolder = 'sourcefolder_example' # str | 
configuration = 'configuration_example' # str | 
deviceid = 'deviceid_example' # str | 
destfolder = 'destfolder_example' # str | 
source_is_sdk = True # bool |  (optional)
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # synchronizes folders
        api_instance.application_syncfolders(application_id, sourcefolder, configuration, deviceid, destfolder, source_is_sdk=source_is_sdk, progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_syncfolders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **sourcefolder** | **str**|  | 
 **configuration** | **str**|  | 
 **deviceid** | **str**|  | 
 **destfolder** | **str**|  | 
 **source_is_sdk** | **bool**|  | [optional] 
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
**200** | Sysroot updated |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**523** | Container is not running. |  -  |
**525** | Remote docker exception. |  -  |
**529** | Remote command execution failed. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**541** | SDK container is not running. |  -  |
**548** | Container does not support SSH |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_updated**
> bool application_updated(application_id, configuration)

Builds container image

Builds application release or debug container

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 

    try:
        # Builds container image
        api_response = api_instance.application_updated(application_id, configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_updated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 

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
**200** | Successful build |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_updatesdk**
> application_updatesdk(application_id, configuration, progress_id=progress_id)

Update SDK container

Updates/rebuilds the SDK container by adding new dev libraries or synchronizing sysroots

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
    api_instance = moses_client.ApplicationsApi(api_client)
    application_id = 'application_id_example' # str | Id of an application (uuid)
configuration = 'configuration_example' # str | 
progress_id = 'progress_id_example' # str | Id of a progress cookie (uuid) (optional)

    try:
        # Update SDK container
        api_instance.application_updatesdk(application_id, configuration, progress_id=progress_id)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->application_updatesdk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) | 
 **configuration** | **str**|  | 
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
**200** | SDK updated |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_create**
> Application applications_create(platform_id, path, username=username)

Loads an application configuration

Returns data about an application

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
    api_instance = moses_client.ApplicationsApi(api_client)
    platform_id = 'platform_id_example' # str | 
path = 'path_example' # str | 
username = 'username_example' # str |  (optional)

    try:
        # Loads an application configuration
        api_response = api_instance.applications_create(platform_id, path, username=username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**|  | 
 **path** | **str**|  | 
 **username** | **str**|  | [optional] 

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
**200** | Returns an application |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**540** | Invalid path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_load**
> Application applications_load(path)

Loads an application configuration

Returns data about an application

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
    api_instance = moses_client.ApplicationsApi(api_client)
    path = 'path_example' # str | 

    try:
        # Loads an application configuration
        api_response = api_instance.applications_load(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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
**200** | Returns an application |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**540** | Invalid path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

