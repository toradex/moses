# moses_client.ApplicationsApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_build**](ApplicationsApi.md#application_build) | **GET** /applications/{application_id}/build | Build container image
[**application_delete**](ApplicationsApi.md#application_delete) | **DELETE** /applications/{application_id} | Remove an application
[**application_deploy**](ApplicationsApi.md#application_deploy) | **GET** /applications/{application_id}/deploy | Deploy container image
[**application_get**](ApplicationsApi.md#application_get) | **GET** /applications/{application_id} | Get application
[**application_getcontainer**](ApplicationsApi.md#application_getcontainer) | **GET** /applications/{application_id}/container | Get container information
[**application_getcontainer_logs**](ApplicationsApi.md#application_getcontainer_logs) | **GET** /applications/{application_id}/container_logs | Get one of more lines from container logs
[**application_getdocker_commandline**](ApplicationsApi.md#application_getdocker_commandline) | **GET** /applications/{application_id}/docker_commandline | Get docker command line to run the application/json
[**application_getdocker_composefile**](ApplicationsApi.md#application_getdocker_composefile) | **GET** /applications/{application_id}/docker_composefile | Get docker compose file
[**application_getprivatekey**](ApplicationsApi.md#application_getprivatekey) | **GET** /applications/{application_id}/privatekey | Get the path of the RSA private key
[**application_modify**](ApplicationsApi.md#application_modify) | **PUT** /applications/{application_id} | Change application properties
[**application_publish**](ApplicationsApi.md#application_publish) | **GET** /applications/{application_id}/publish | Publish a new version of the application on Torizon OTA
[**application_push_to_registry**](ApplicationsApi.md#application_push_to_registry) | **GET** /applications/{application_id}/push_to_registry | Push application to docker registry
[**application_reseal**](ApplicationsApi.md#application_reseal) | **GET** /applications/{application_id}/reseal | Clean id and keys from application configuration
[**application_run**](ApplicationsApi.md#application_run) | **GET** /applications/{application_id}/run | Run container image
[**application_runsdk**](ApplicationsApi.md#application_runsdk) | **GET** /applications/{application_id}/sdk/run | Run SDK containers
[**application_sdk_container**](ApplicationsApi.md#application_sdk_container) | **GET** /applications/{application_id}/sdk/container | Get SDK container
[**application_stop**](ApplicationsApi.md#application_stop) | **GET** /applications/{application_id}/stop | Stop running container image
[**application_syncfolders**](ApplicationsApi.md#application_syncfolders) | **GET** /applications/{application_id}/syncfolders | Synchronize folders
[**application_tcb_build_yaml**](ApplicationsApi.md#application_tcb_build_yaml) | **GET** /applications/{application_id}/tcb_build_yaml | Build the TorizonCore tcbuild.yaml
[**application_tcb_deploy**](ApplicationsApi.md#application_tcb_deploy) | **GET** /applications/{application_id}/tcb_deploy | TorizonCore unpack command
[**application_tcb_dt_checkout**](ApplicationsApi.md#application_tcb_dt_checkout) | **GET** /applications/{application_id}/tcb_dt_checkout | TorizonCore Device Tree repo checkout
[**application_tcb_isolate**](ApplicationsApi.md#application_tcb_isolate) | **GET** /applications/{application_id}/tcb_isolate | TorizonCore isolate command
[**application_tcb_push**](ApplicationsApi.md#application_tcb_push) | **GET** /applications/{application_id}/tcb_push | TorizonCore Builder push command.
[**application_tcb_union**](ApplicationsApi.md#application_tcb_union) | **GET** /applications/{application_id}/tcb_union | TorizonCore Builder union command.
[**application_tcb_unpack**](ApplicationsApi.md#application_tcb_unpack) | **GET** /applications/{application_id}/tcb_unpack | TorizonCore unpack command
[**application_updated**](ApplicationsApi.md#application_updated) | **GET** /applications/{application_id}/updated | Check if container image is up to date
[**application_updatesdk**](ApplicationsApi.md#application_updatesdk) | **GET** /applications/{application_id}/sdk/update | Update SDK container
[**application_validate_array_item**](ApplicationsApi.md#application_validate_array_item) | **GET** /applications/{application_id}/validate_array_item | Validates a value for a parameter
[**application_validate_dictionary_entry**](ApplicationsApi.md#application_validate_dictionary_entry) | **GET** /applications/{application_id}/validate_dictionary_entry | Validates a value for a parameter
[**application_validate_parameter**](ApplicationsApi.md#application_validate_parameter) | **GET** /applications/{application_id}/validate_parameter | Validates a value for a parameter
[**applications_create**](ApplicationsApi.md#applications_create) | **GET** /applications/create | Create an application configuration
[**applications_load**](ApplicationsApi.md#applications_load) | **GET** /applications/load | Load an application configuration


# **application_build**
> application_build(application_id, configuration)

Build container image

Build application release or debug container

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Build container image
        api_instance.application_build(application_id, configuration)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_build: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Build container image
        api_instance.application_build(application_id, configuration, progress_id=progress_id)
    except moses_client.ApiException as e:
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
**200** | OK |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_delete**
> application_delete(application_id)

Remove an application

Remove an application and all the associated data and containers

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)

    # example passing only required values which don't have defaults set
    try:
        # Remove an application
        api_instance.application_delete(application_id)
    except moses_client.ApiException as e:
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
**204** | OK |  -  |
**404** | Application no found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_deploy**
> application_deploy(application_id, configuration, device_id)

Deploy container image

Deploy application container to target

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deploy container image
        api_instance.application_deploy(application_id, configuration, device_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_deploy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy container image
        api_instance.application_deploy(application_id, configuration, device_id, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_deploy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **device_id** | **str**| Target device serial number |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get**
> Application application_get(application_id)

Get application

Returns a specified application, knowing its id

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.application import Application
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)

    # example passing only required values which don't have defaults set
    try:
        # Get application
        api_response = api_instance.application_get(application_id)
        pprint(api_response)
    except moses_client.ApiException as e:
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
> DockerContainer application_getcontainer(application_id, configuration, device_id)

Get container information

Get detailed informations about container

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Get container information
        api_response = api_instance.application_getcontainer(application_id, configuration, device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_getcontainer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **device_id** | **str**| Target device serial number |

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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getcontainer_logs**
> str application_getcontainer_logs(application_id, configuration, device_id)

Get one of more lines from container logs

Return one chunk of log (one or more lines), blocking if no data is available

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    restart = False # bool | when true reads the lock back from beginning (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get one of more lines from container logs
        api_response = api_instance.application_getcontainer_logs(application_id, configuration, device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_getcontainer_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get one of more lines from container logs
        api_response = api_instance.application_getcontainer_logs(application_id, configuration, device_id, restart=restart)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_getcontainer_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **device_id** | **str**| Target device serial number |
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
**200** | Log entries as text |  -  |
**204** | No content |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getdocker_commandline**
> str application_getdocker_commandline(application_id, configuration)

Get docker command line to run the application/json

Return the full docker command line that can be used to run the application container

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get docker command line to run the application/json
        api_response = api_instance.application_getdocker_commandline(application_id, configuration)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Command line |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getdocker_composefile**
> str application_getdocker_composefile(application_id, configuration)

Get docker compose file

Return docker-compose file that can be used to run the application container and its dependencies

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get docker compose file
        api_response = api_instance.application_getdocker_composefile(application_id, configuration)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Docker-compose file (string with *nix line endings) |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_getprivatekey**
> str application_getprivatekey(application_id)

Get the path of the RSA private key

Retrieve the path of the private key that allows passwordless connection to the container. The application stores the public key inside the container if ssh is enabled (usually for debug builds only)

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)

    # example passing only required values which don't have defaults set
    try:
        # Get the path of the RSA private key
        api_response = api_instance.application_getprivatekey(application_id)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Key path |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_modify**
> Application application_modify(application_id)

Change application properties

Changes specified properties on an application

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.application import Application
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    application = Application(
        props={
            "key": {
                "key": "key_example",
            },
        },
        dockercomposefile={
            "key": "key_example",
        },
        startupscript={
            "key": "key_example",
        },
        shutdownscript={
            "key": "key_example",
        },
        ports={
            "key": {
                "key": "key_example",
            },
        },
        volumes={
            "key": {
                "key": "key_example",
            },
        },
        devices={
            "key": [
                "key_example",
            ],
        },
        networks={
            "key": [
                "key_example",
            ],
        },
        extraparms={
            "key": {
                "key": "key_example",
            },
        },
        username="username_example",
        images={
            "key": "key_example",
        },
        sdkimages={
            "key": "key_example",
        },
        imagetags={
            "key": "key_example",
        },
        sdkimagetags={
            "key": "key_example",
        },
        otapackagename="otapackagename_example",
        otapackageversion="otapackageversion_example",
    ) # Application |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change application properties
        api_response = api_instance.application_modify(application_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_modify: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change application properties
        api_response = api_instance.application_modify(application_id, application=application)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Application information |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_publish**
> application_publish(application_id, credentials, dockeruser, dockerpass)

Publish a new version of the application on Torizon OTA

Publishes a new package version for the application, if no credentials are provided, then only docker-compose file is generated.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    credentials = "credentials_example" # str | credentials file
    dockeruser = "dockeruser_example" # str | user for docker registry login
    dockerpass = "dockerpass_example" # str | password for docker registry login
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Publish a new version of the application on Torizon OTA
        api_instance.application_publish(application_id, credentials, dockeruser, dockerpass)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_publish: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Publish a new version of the application on Torizon OTA
        api_instance.application_publish(application_id, credentials, dockeruser, dockerpass, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **credentials** | **str**| credentials file |
 **dockeruser** | **str**| user for docker registry login |
 **dockerpass** | **str**| password for docker registry login |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**552** | Invalid or missing parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_push_to_registry**
> application_push_to_registry(application_id, configuration, username, password)

Push application to docker registry

Push application's container to a docker registry, using authentication

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    username = "username_example" # str | 
    password = "password_example" # str | 
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Push application to docker registry
        api_instance.application_push_to_registry(application_id, configuration, username, password)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_push_to_registry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Push application to docker registry
        api_instance.application_push_to_registry(application_id, configuration, username, password, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_push_to_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **username** | **str**|  |
 **password** | **str**|  |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_reseal**
> application_reseal(application_id)

Clean id and keys from application configuration

This operation make the application no longer valid, but allow you to upload it to a git repo from where it can be cloned/forked. Id and keys will be re-generated on next re-opening of the application, leading to different names for the images etc.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)

    # example passing only required values which don't have defaults set
    try:
        # Clean id and keys from application configuration
        api_instance.application_reseal(application_id)
    except moses_client.ApiException as e:
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
**200** | OK |  -  |
**404** | Application not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_run**
> DockerContainer application_run(application_id, configuration, device_id)

Run container image

Run the application release or debug container on target, if the application is already running, restarts it

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Run container image
        api_response = api_instance.application_run(application_id, configuration, device_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run container image
        api_response = api_instance.application_run(application_id, configuration, device_id, progress_id=progress_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **device_id** | **str**| Target device serial number |
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
**200** | Container information |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**525** | Remote docker exception. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_runsdk**
> InlineResponse200 application_runsdk(application_id, configuration)

Run SDK containers

Run SDK container and return its IP and SSH port

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from moses_client.model.inline_response200 import InlineResponse200
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    build = True # bool |  (optional) if omitted the server will use the default value of True
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Run SDK containers
        api_response = api_instance.application_runsdk(application_id, configuration)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_runsdk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run SDK containers
        api_response = api_instance.application_runsdk(application_id, configuration, build=build, progress_id=progress_id)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_runsdk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **build** | **bool**|  | [optional] if omitted the server will use the default value of True
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
**200** | IP and port of the SSH port exposed by container (if any) |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_sdk_container**
> DockerContainer application_sdk_container(application_id, configuration)

Get SDK container

Get SDK container information (can be used to check if it's running)

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get SDK container
        api_response = api_instance.application_sdk_container(application_id, configuration)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Container information |  -  |
**204** | No content |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_stop**
> application_stop(application_id, configuration, device_id)

Stop running container image

Stop application release or debug container currently running on target, operation succeeds even if the container is not running

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number

    # example passing only required values which don't have defaults set
    try:
        # Stop running container image
        api_instance.application_stop(application_id, configuration, device_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
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
**500** | Unexpected exception. |  -  |
**525** | Remote docker exception. |  -  |
**533** | SSH error. |  -  |
**539** | SSH tunnel error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_syncfolders**
> application_syncfolders(application_id, sourcefolder, configuration, device_id, destfolder)

Synchronize folders

Synchronizes folders between host/SDK container and the application container

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    sourcefolder = "sourcefolder_example" # str | 
    configuration = "release" # str | 
    device_id = "zA9LCSLv1C1ylmgd0.Y2TA" # str | Target device serial number
    destfolder = "destfolder_example" # str | 
    source_is_sdk = True # bool |  (optional)
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Synchronize folders
        api_instance.application_syncfolders(application_id, sourcefolder, configuration, device_id, destfolder)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_syncfolders: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Synchronize folders
        api_instance.application_syncfolders(application_id, sourcefolder, configuration, device_id, destfolder, source_is_sdk=source_is_sdk, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_syncfolders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **sourcefolder** | **str**|  |
 **configuration** | **str**|  |
 **device_id** | **str**| Target device serial number |
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
**200** | OK |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**523** | Container is not running. |  -  |
**525** | Remote docker exception. |  -  |
**529** | Remote command execution failed. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**541** | SDK container is not running. |  -  |
**549** | Container does not support SSH |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_build_yaml**
> application_tcb_build_yaml(application_id, yamlfilepath)

Build the TorizonCore tcbuild.yaml

Build the TorizonCore tcbuild.yaml using TorizonCore Builder Docker image.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    yamlfilepath = "yamlfilepath_example" # str | the yaml file name from workspace path
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Build the TorizonCore tcbuild.yaml
        api_instance.application_tcb_build_yaml(application_id, yamlfilepath)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_build_yaml: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Build the TorizonCore tcbuild.yaml
        api_instance.application_tcb_build_yaml(application_id, yamlfilepath, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_build_yaml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **yamlfilepath** | **str**| the yaml file name from workspace path |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_deploy**
> application_tcb_deploy(application_id, host, username, password)

TorizonCore unpack command

Unpack the output using TorizonCore Builder Docker image.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    host = "host_example" # str | the hostname or ip address of the device to be deployed
    username = "username_example" # str | the Torizon username of the device to be deployed
    password = "password_example" # str | the Torizon password of the device to be deployed
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore unpack command
        api_instance.application_tcb_deploy(application_id, host, username, password)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_deploy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore unpack command
        api_instance.application_tcb_deploy(application_id, host, username, password, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_deploy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **host** | **str**| the hostname or ip address of the device to be deployed |
 **username** | **str**| the Torizon username of the device to be deployed |
 **password** | **str**| the Torizon password of the device to be deployed |
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
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_dt_checkout**
> application_tcb_dt_checkout(application_id)

TorizonCore Device Tree repo checkout

Checkout the device tree and overlays repository at https://github.com/toradex/device-trees

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore Device Tree repo checkout
        api_instance.application_tcb_dt_checkout(application_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_dt_checkout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore Device Tree repo checkout
        api_instance.application_tcb_dt_checkout(application_id, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_dt_checkout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_isolate**
> application_tcb_isolate(application_id, host, username, password, output_dir)

TorizonCore isolate command

Get configuration changes from the target board.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    host = "host_example" # str | the hostname or ip address of the device to be deployed
    username = "username_example" # str | the Torizon username of the device to be deployed
    password = "password_example" # str | the Torizon password of the device to be deployed
    output_dir = "output_dir_example" # str | the direcotry path that the changes will be save
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore isolate command
        api_instance.application_tcb_isolate(application_id, host, username, password, output_dir)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_isolate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore isolate command
        api_instance.application_tcb_isolate(application_id, host, username, password, output_dir, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_isolate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **host** | **str**| the hostname or ip address of the device to be deployed |
 **username** | **str**| the Torizon username of the device to be deployed |
 **password** | **str**| the Torizon password of the device to be deployed |
 **output_dir** | **str**| the direcotry path that the changes will be save |
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
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_push**
> application_tcb_push(application_id, branch, credentials)

TorizonCore Builder push command.

The command push from TorizonCore Builder can be used to push a new TorizonCore image to Torizon OTA.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    branch = "branch_example" # str | union branch string
    credentials = "credentials_example" # str | credentials file path
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore Builder push command.
        api_instance.application_tcb_push(application_id, branch, credentials)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_push: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore Builder push command.
        api_instance.application_tcb_push(application_id, branch, credentials, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_push: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **branch** | **str**| union branch string |
 **credentials** | **str**| credentials file path |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_union**
> application_tcb_union(application_id, branch)

TorizonCore Builder union command.

union makes an OSTree branch (containing the commit for changes) for all changes provided by the user to be made in OSTree rootfs of unpacked base Torizon image.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    branch = "branch_example" # str | union branch string
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore Builder union command.
        api_instance.application_tcb_union(application_id, branch)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_union: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore Builder union command.
        api_instance.application_tcb_union(application_id, branch, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_union: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **branch** | **str**| union branch string |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_tcb_unpack**
> application_tcb_unpack(application_id, outputpath)

TorizonCore unpack command

Unpack the output using TorizonCore Builder Docker image.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    outputpath = "outputpath_example" # str | the output directory created by TorizonCore builder from workspace path
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # TorizonCore unpack command
        api_instance.application_tcb_unpack(application_id, outputpath)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_unpack: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # TorizonCore unpack command
        api_instance.application_tcb_unpack(application_id, outputpath, progress_id=progress_id)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_tcb_unpack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **outputpath** | **str**| the output directory created by TorizonCore builder from workspace path |
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
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**550** | No tag has been set for the image |  -  |
**551** | Operation has been aborted |  -  |
**553** | TorizonCore Builder error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_updated**
> bool application_updated(application_id, configuration)

Check if container image is up to date

Check if some properties have been changed after the last build of the configuration-specific container image

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check if container image is up to date
        api_response = api_instance.application_updated(application_id, configuration)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | true if container image is up to date |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**530** | Local docker exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_updatesdk**
> application_updatesdk(application_id, configuration)

Update SDK container

Update the SDK container by adding new dev libraries or synchronizing sysroots

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "release" # str | 
    progress_id = "55914d4d-6Ea1-8e3e-53E0-3fEE4Bc7d,,c" # str | Id of a progress cookie (uuid) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update SDK container
        api_instance.application_updatesdk(application_id, configuration)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_updatesdk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update SDK container
        api_instance.application_updatesdk(application_id, configuration, progress_id=progress_id)
    except moses_client.ApiException as e:
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
**200** | OK |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |
**520** | Container image not found on local host. |  -  |
**530** | Local docker exception. |  -  |
**533** | SSH error. |  -  |
**551** | Operation has been aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_validate_array_item**
> ValidationResult application_validate_array_item(application_id, configuration, parameter, value, index)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "common" # str | 
    parameter = "parameter_example" # str | 
    value = "value_example" # str | 
    index = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Validates a value for a parameter
        api_response = api_instance.application_validate_array_item(application_id, configuration, parameter, value, index)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_validate_array_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **parameter** | **str**|  |
 **value** | **str**|  |
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
**200** | Validation results |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_validate_dictionary_entry**
> ValidationResult application_validate_dictionary_entry(application_id, configuration, parameter, key, value, newitem)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "common" # str | 
    parameter = "parameter_example" # str | 
    key = "key_example" # str | 
    value = "value_example" # str | 
    newitem = True # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Validates a value for a parameter
        api_response = api_instance.application_validate_dictionary_entry(application_id, configuration, parameter, key, value, newitem)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_validate_dictionary_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
 **parameter** | **str**|  |
 **key** | **str**|  |
 **value** | **str**|  |
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
**200** | Validation results |  -  |
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_validate_parameter**
> ValidationResult application_validate_parameter(application_id, configuration, parameter, value)

Validates a value for a parameter

Validates a parameter, allowing UI to report problems before applying it.

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "555914d4-d6Ea-18e3-e53E-03fEE4Bc7d,," # str | Id of an application (uuid)
    configuration = "common" # str | 
    parameter = "parameter_example" # str | 
    value = "value_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Validates a value for a parameter
        api_response = api_instance.application_validate_parameter(application_id, configuration, parameter, value)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->application_validate_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Id of an application (uuid) |
 **configuration** | **str**|  |
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
**404** | Application not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_create**
> Application applications_create(platform_id, path)

Create an application configuration

Create a new application configuration

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.application import Application
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    platform_id = "platform_id_example" # str | 
    path = "path_example" # str | 
    username = "username_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an application configuration
        api_response = api_instance.applications_create(platform_id, path)
        pprint(api_response)
    except moses_client.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an application configuration
        api_response = api_instance.applications_create(platform_id, path, username=username)
        pprint(api_response)
    except moses_client.ApiException as e:
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
**200** | Application information |  -  |
**404** | Platform not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |
**540** | Invalid path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_load**
> Application applications_load(path)

Load an application configuration

Load an application configuration from the local filesystem

### Example


```python
import time
import moses_client
from moses_client.api import applications_api
from moses_client.model.error_info import ErrorInfo
from moses_client.model.application import Application
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = moses_client.Configuration(
    host = "http://localhost:5000/api"
)


# Enter a context with an instance of the API client
with moses_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    path = "path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Load an application configuration
        api_response = api_instance.applications_load(path)
        pprint(api_response)
    except moses_client.ApiException as e:
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

