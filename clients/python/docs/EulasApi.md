# moses_client.EulasApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eula_get**](EulasApi.md#eula_get) | **GET** /eulas/{eula_id} | Get detail about an eula
[**eula_modify**](EulasApi.md#eula_modify) | **PUT** /eulas/{eula_id} | Change eula properties
[**eulas_get**](EulasApi.md#eulas_get) | **GET** /eulas | Get all eulas


# **eula_get**
> Eula eula_get(eula_id)

Get detail about an eula

Return detailed information about a specific eula

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
    api_instance = moses_client.EulasApi(api_client)
    eula_id = 'eula_id_example' # str | Id of an Eula

    try:
        # Get detail about an eula
        api_response = api_instance.eula_get(eula_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EulasApi->eula_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eula_id** | **str**| Id of an Eula | 

### Return type

[**Eula**](Eula.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eula Information |  -  |
**404** | Eula not found |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eula_modify**
> Eula eula_modify(eula_id, e=e)

Change eula properties

Set eula as visualized and/or accepted

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
    api_instance = moses_client.EulasApi(api_client)
    eula_id = 'eula_id_example' # str | Id of an Eula
e = moses_client.Eula() # Eula |  (optional)

    try:
        # Change eula properties
        api_response = api_instance.eula_modify(eula_id, e=e)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EulasApi->eula_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eula_id** | **str**| Id of an Eula | 
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
**200** | Eula information |  -  |
**404** | Eula not found |  -  |
**500** | Unexpected exception. |  -  |
**531** | Object Does not have a valid id. |  -  |
**532** | Object cannot be saved because it&#39;s in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eulas_get**
> list[Eula] eulas_get()

Get all eulas

Returns information about all eulas required to run different platforms on the system

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
    api_instance = moses_client.EulasApi(api_client)
    
    try:
        # Get all eulas
        api_response = api_instance.eulas_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EulasApi->eulas_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Eula]**](Eula.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Eulas |  -  |
**500** | Unexpected exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

