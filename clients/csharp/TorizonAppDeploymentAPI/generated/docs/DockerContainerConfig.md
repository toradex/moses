
# TorizonRestAPI.Model.DockerContainerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Hostname** | **string** | The hostname to use for the container, as a valid RFC 1123 hostname. | [optional] 
**Domainname** | **string** | The domain name to use for the container. | [optional] 
**User** | **string** | The user that commands are run as inside the container. | [optional] 
**AttachStdin** | **bool** | Whether to attach to &#x60;stdin&#x60;. | [optional] [default to false]
**AttachStdout** | **bool** | Whether to attach to &#x60;stdout&#x60;. | [optional] [default to true]
**AttachStderr** | **bool** | Whether to attach to &#x60;stderr&#x60;. | [optional] [default to true]
**ExposedPorts** | **Dictionary&lt;string, Object&gt;** | An object mapping ports to an empty object in the form:  &#x60;{\&quot;&lt;port&gt;/&lt;tcp|udp|sctp&gt;\&quot;: {}}&#x60;  | [optional] 
**Tty** | **bool** | Attach standard streams to a TTY, including &#x60;stdin&#x60; if it is not closed. | [optional] [default to false]
**OpenStdin** | **bool** | Open &#x60;stdin&#x60; | [optional] [default to false]
**StdinOnce** | **bool** | Close &#x60;stdin&#x60; after one attached client disconnects | [optional] [default to false]
**Env** | **List&lt;string&gt;** | A list of environment variables to set inside the container in the form &#x60;[\&quot;VAR&#x3D;value\&quot;, ...]&#x60;. A variable without &#x60;&#x3D;&#x60; is removed from the environment, rather than to have an empty value.  | [optional] 
**Cmd** | **List&lt;string&gt;** | Command to run specified as a string or an array of strings. | [optional] 
**Healthcheck** | [**DockerHealthConfig**](DockerHealthConfig.md) |  | [optional] 
**ArgsEscaped** | **bool** | Command is already escaped (Windows only) | [optional] 
**Image** | **string** | The name of the image to use when creating the container | [optional] 
**Volumes** | **Dictionary&lt;string, Object&gt;** | An object mapping mount point paths inside the container to empty objects. | [optional] 
**WorkingDir** | **string** | The working directory for commands to run in. | [optional] 
**Entrypoint** | **List&lt;string&gt;** | The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (&#x60;[\&quot;\&quot;]&#x60;) then the entry point is reset to system default (i.e., the entry point used by docker when there is no &#x60;ENTRYPOINT&#x60; instruction in the &#x60;Dockerfile&#x60;).  | [optional] 
**NetworkDisabled** | **bool** | Disable networking for the container. | [optional] 
**MacAddress** | **string** | MAC address of the container. | [optional] 
**OnBuild** | **List&lt;string&gt;** | &#x60;ONBUILD&#x60; metadata that were defined in the image&#39;s &#x60;Dockerfile&#x60;. | [optional] 
**Labels** | **Dictionary&lt;string, string&gt;** | User-defined key/value metadata. | [optional] 
**StopSignal** | **string** | Signal to stop a container as a string or unsigned integer. | [optional] [default to "SIGTERM"]
**StopTimeout** | **int** | Timeout to stop a container in seconds. | [optional] 
**Shell** | **List&lt;string&gt;** | Shell for when &#x60;RUN&#x60;, &#x60;CMD&#x60;, and &#x60;ENTRYPOINT&#x60; uses a shell. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

