# moses-client
Toradex API to build and deploy applications running as containers on Torizon

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.14
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import moses_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import moses_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with moses_client.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationsApi* | [**application_build**](docs/ApplicationsApi.md#application_build) | **GET** /applications/{application_id}/build | Builds container image
*ApplicationsApi* | [**application_delete**](docs/ApplicationsApi.md#application_delete) | **DELETE** /applications/{application_id} | Remove an application and all the associated data and containers
*ApplicationsApi* | [**application_deploy**](docs/ApplicationsApi.md#application_deploy) | **GET** /applications/{application_id}/deploy | Deploys container image
*ApplicationsApi* | [**application_get**](docs/ApplicationsApi.md#application_get) | **GET** /applications/{application_id} | Get application
*ApplicationsApi* | [**application_getcontainer**](docs/ApplicationsApi.md#application_getcontainer) | **GET** /applications/{application_id}/container | Get container information
*ApplicationsApi* | [**application_getcontainer_logs**](docs/ApplicationsApi.md#application_getcontainer_logs) | **GET** /applications/{application_id}/container_logs | Get container log, chunk by chunk
*ApplicationsApi* | [**application_getdocker_commandline**](docs/ApplicationsApi.md#application_getdocker_commandline) | **GET** /applications/{application_id}/docker_commandline | Get docker command line used to run the container
*ApplicationsApi* | [**application_getdocker_composefile**](docs/ApplicationsApi.md#application_getdocker_composefile) | **GET** /applications/{application_id}/docker_composefile | Get docker compose file
*ApplicationsApi* | [**application_getprivatekey**](docs/ApplicationsApi.md#application_getprivatekey) | **GET** /applications/{application_id}/privatekey | Retrieves the path of the RSA private key
*ApplicationsApi* | [**application_modify**](docs/ApplicationsApi.md#application_modify) | **PUT** /applications/{application_id} | Change application properties
*ApplicationsApi* | [**application_push_to_registry**](docs/ApplicationsApi.md#application_push_to_registry) | **GET** /applications/{application_id}/push_to_registry | Push application to docker registry
*ApplicationsApi* | [**application_reseal**](docs/ApplicationsApi.md#application_reseal) | **GET** /applications/{application_id}/reseal | Cleans id and keys for git repo uploading
*ApplicationsApi* | [**application_run**](docs/ApplicationsApi.md#application_run) | **GET** /applications/{application_id}/run | Runs container image
*ApplicationsApi* | [**application_runsdk**](docs/ApplicationsApi.md#application_runsdk) | **GET** /applications/{application_id}/sdk/run | Runs SDK containers
*ApplicationsApi* | [**application_sdk_container**](docs/ApplicationsApi.md#application_sdk_container) | **GET** /applications/{application_id}/sdk/container | Get SDK container
*ApplicationsApi* | [**application_stop**](docs/ApplicationsApi.md#application_stop) | **GET** /applications/{application_id}/stop | Stops running container image
*ApplicationsApi* | [**application_syncfolders**](docs/ApplicationsApi.md#application_syncfolders) | **GET** /applications/{application_id}/syncfolders | synchronizes folders
*ApplicationsApi* | [**application_updated**](docs/ApplicationsApi.md#application_updated) | **GET** /applications/{application_id}/updated | Builds container image
*ApplicationsApi* | [**application_updatesdk**](docs/ApplicationsApi.md#application_updatesdk) | **GET** /applications/{application_id}/sdk/update | Update SDK container
*ApplicationsApi* | [**applications_create**](docs/ApplicationsApi.md#applications_create) | **GET** /applications/create | Loads an application configuration
*ApplicationsApi* | [**applications_load**](docs/ApplicationsApi.md#applications_load) | **GET** /applications/load | Loads an application configuration
*DevicesApi* | [**container_getlogs**](docs/DevicesApi.md#container_getlogs) | **GET** /devices/{device_id}/containers/{container_id}/logs | return container logs one chunk a time
*DevicesApi* | [**container_getmemory**](docs/DevicesApi.md#container_getmemory) | **GET** /devices/{device_id}/containers/{container_id}/memory | Return container memory information
*DevicesApi* | [**container_getmountpoints**](docs/DevicesApi.md#container_getmountpoints) | **GET** /devices/{device_id}/containers/{container_id}/storage | return information about storage
*DevicesApi* | [**container_getprocesses**](docs/DevicesApi.md#container_getprocesses) | **GET** /devices/{device_id}/containers/{container_id}/processes | return processes running in container
*DevicesApi* | [**container_start**](docs/DevicesApi.md#container_start) | **GET** /devices/{device_id}/containers/{container_id}/start | starts container
*DevicesApi* | [**container_stop**](docs/DevicesApi.md#container_stop) | **GET** /devices/{device_id}/containers/{container_id}/stop | stops container
*DevicesApi* | [**containers_deletecontainer**](docs/DevicesApi.md#containers_deletecontainer) | **DELETE** /devices/{device_id}/containers/{container_id} | delete a container
*DevicesApi* | [**containers_getcontainer**](docs/DevicesApi.md#containers_getcontainer) | **GET** /devices/{device_id}/containers/{container_id} | get container details
*DevicesApi* | [**device_closedocker**](docs/DevicesApi.md#device_closedocker) | **GET** /devices/{device_id}/docker/close | Disables remote docker
*DevicesApi* | [**device_closessh**](docs/DevicesApi.md#device_closessh) | **GET** /devices/{device_id}/ssh/close | Disables ssh tunneling
*DevicesApi* | [**device_current_ip**](docs/DevicesApi.md#device_current_ip) | **GET** /devices/{device_id}/current_ip | returns current ip of the device
*DevicesApi* | [**device_delete**](docs/DevicesApi.md#device_delete) | **DELETE** /devices/{device_id} | Remove a device
*DevicesApi* | [**device_get**](docs/DevicesApi.md#device_get) | **GET** /devices/{device_id} | Get device
*DevicesApi* | [**device_getcontainers**](docs/DevicesApi.md#device_getcontainers) | **GET** /devices/{device_id}/containers | list containers
*DevicesApi* | [**device_getdockerport**](docs/DevicesApi.md#device_getdockerport) | **GET** /devices/{device_id}/docker/port | remote docker local port
*DevicesApi* | [**device_getimages**](docs/DevicesApi.md#device_getimages) | **GET** /devices/{device_id}/images | list images
*DevicesApi* | [**device_getmemory**](docs/DevicesApi.md#device_getmemory) | **GET** /devices/{device_id}/memory | Return memory information
*DevicesApi* | [**device_getmountpoints**](docs/DevicesApi.md#device_getmountpoints) | **GET** /devices/{device_id}/storage | return storage information for a device
*DevicesApi* | [**device_getprivatekey**](docs/DevicesApi.md#device_getprivatekey) | **GET** /devices/{device_id}/privatekey | return the path of the device private key
*DevicesApi* | [**device_getprocesses**](docs/DevicesApi.md#device_getprocesses) | **GET** /devices/{device_id}/processes | list running processes on a device
*DevicesApi* | [**device_getsshport**](docs/DevicesApi.md#device_getsshport) | **GET** /devices/{device_id}/ssh/port | remote ssh local port
*DevicesApi* | [**device_modify**](docs/DevicesApi.md#device_modify) | **PUT** /devices/{device_id} | Change device properties
*DevicesApi* | [**device_opendocker**](docs/DevicesApi.md#device_opendocker) | **GET** /devices/{device_id}/docker/open | Expose remote docker
*DevicesApi* | [**device_openssh**](docs/DevicesApi.md#device_openssh) | **GET** /devices/{device_id}/ssh/open | Expose remote ssh
*DevicesApi* | [**device_syncfolders**](docs/DevicesApi.md#device_syncfolders) | **GET** /devices/{device_id}/syncfolders | synchronizes folders
*DevicesApi* | [**device_update**](docs/DevicesApi.md#device_update) | **GET** /devices/{device_id}/update | update information for a specific device
*DevicesApi* | [**devices_get**](docs/DevicesApi.md#devices_get) | **GET** /devices | Get all devices
*DevicesApi* | [**devices_networkdetect**](docs/DevicesApi.md#devices_networkdetect) | **GET** /devices/network_detect | Finds a network device
*DevicesApi* | [**devices_serialdetect**](docs/DevicesApi.md#devices_serialdetect) | **GET** /devices/serial_detect | Finds a device connected to serial port
*DevicesApi* | [**images_deleteimage**](docs/DevicesApi.md#images_deleteimage) | **DELETE** /devices/{device_id}/images/{image_id} | delete an image
*DevicesApi* | [**images_getimage**](docs/DevicesApi.md#images_getimage) | **GET** /devices/{device_id}/images/{image_id} | get image details
*EulasApi* | [**eula_get**](docs/EulasApi.md#eula_get) | **GET** /eulas/{eula_id} | Get an eula
*EulasApi* | [**eula_modify**](docs/EulasApi.md#eula_modify) | **PUT** /eulas/{eula_id} | Change eula properties
*EulasApi* | [**eulas_get**](docs/EulasApi.md#eulas_get) | **GET** /eulas | Get all eulas
*PlatformsApi* | [**platform_compatibledevices_get**](docs/PlatformsApi.md#platform_compatibledevices_get) | **GET** /platforms/{platform_id}/compatibledevices | get compatible devices
*PlatformsApi* | [**platform_get**](docs/PlatformsApi.md#platform_get) | **GET** /platforms/{platform_id} | Get a platform
*PlatformsApi* | [**platforms_get**](docs/PlatformsApi.md#platforms_get) | **GET** /platforms | Get all platforms
*ProgressApi* | [**progress_create**](docs/ProgressApi.md#progress_create) | **GET** /progress/create | create a progress ID
*ProgressApi* | [**progress_delete**](docs/ProgressApi.md#progress_delete) | **GET** /progress/delete | releases progress ID
*ProgressApi* | [**progress_status**](docs/ProgressApi.md#progress_status) | **GET** /progress/status | retrieves status of an operation
*SetupApi* | [**setup_enableemulation**](docs/SetupApi.md#setup_enableemulation) | **GET** /setup/enableemulation | enables ARM emulation using qemu
*SetupApi* | [**setup_pullcontainers**](docs/SetupApi.md#setup_pullcontainers) | **GET** /setup/pullcontainers | pulls containers from docker repo
*VersionApi* | [**version_docker**](docs/VersionApi.md#version_docker) | **GET** /version/docker | Docker version info
*VersionApi* | [**version_get**](docs/VersionApi.md#version_get) | **GET** /version | APP/API version


## Documentation For Models

 - [Application](docs/Application.md)
 - [DockerAddress](docs/DockerAddress.md)
 - [DockerContainer](docs/DockerContainer.md)
 - [DockerContainerConfig](docs/DockerContainerConfig.md)
 - [DockerContainerState](docs/DockerContainerState.md)
 - [DockerDeviceMapping](docs/DockerDeviceMapping.md)
 - [DockerEndpointIPAMConfig](docs/DockerEndpointIPAMConfig.md)
 - [DockerEndpointSettings](docs/DockerEndpointSettings.md)
 - [DockerGraphDriverData](docs/DockerGraphDriverData.md)
 - [DockerHealthConfig](docs/DockerHealthConfig.md)
 - [DockerHostConfig](docs/DockerHostConfig.md)
 - [DockerHostConfigAllOf](docs/DockerHostConfigAllOf.md)
 - [DockerHostConfigAllOfLogConfig](docs/DockerHostConfigAllOfLogConfig.md)
 - [DockerImage](docs/DockerImage.md)
 - [DockerImageMetadata](docs/DockerImageMetadata.md)
 - [DockerImageRootFS](docs/DockerImageRootFS.md)
 - [DockerMount](docs/DockerMount.md)
 - [DockerMountBindOptions](docs/DockerMountBindOptions.md)
 - [DockerMountPoint](docs/DockerMountPoint.md)
 - [DockerMountTmpfsOptions](docs/DockerMountTmpfsOptions.md)
 - [DockerMountVolumeOptions](docs/DockerMountVolumeOptions.md)
 - [DockerMountVolumeOptionsDriverConfig](docs/DockerMountVolumeOptionsDriverConfig.md)
 - [DockerNetworkSettings](docs/DockerNetworkSettings.md)
 - [DockerPortBinding](docs/DockerPortBinding.md)
 - [DockerResources](docs/DockerResources.md)
 - [DockerResourcesBlkioWeightDevice](docs/DockerResourcesBlkioWeightDevice.md)
 - [DockerResourcesUlimits](docs/DockerResourcesUlimits.md)
 - [DockerRestartPolicy](docs/DockerRestartPolicy.md)
 - [DockerThrottleDevice](docs/DockerThrottleDevice.md)
 - [DockerVersion](docs/DockerVersion.md)
 - [DockerVersionComponents](docs/DockerVersionComponents.md)
 - [DockerVersionPlatform](docs/DockerVersionPlatform.md)
 - [ErrorInfo](docs/ErrorInfo.md)
 - [Eula](docs/Eula.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [MemInfo](docs/MemInfo.md)
 - [MountPoint](docs/MountPoint.md)
 - [Platform](docs/Platform.md)
 - [Process](docs/Process.md)
 - [Progress](docs/Progress.md)
 - [TargetDevice](docs/TargetDevice.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




