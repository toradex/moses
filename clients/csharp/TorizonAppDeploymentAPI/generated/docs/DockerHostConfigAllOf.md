
# TorizonRestAPI.Model.DockerHostConfigAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Binds** | **List&lt;string&gt;** | A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - &#x60;host-src:container-dest&#x60; to bind-mount a host path into the container. Both &#x60;host-src&#x60;, and &#x60;container-dest&#x60; must be an _absolute_ path. - &#x60;host-src:container-dest:ro&#x60; to make the bind mount read-only inside the container. Both &#x60;host-src&#x60;, and &#x60;container-dest&#x60; must be an _absolute_ path. - &#x60;volume-name:container-dest&#x60; to bind-mount a volume managed by a volume driver into the container. &#x60;container-dest&#x60; must be an _absolute_ path. - &#x60;volume-name:container-dest:ro&#x60; to mount the volume read-only inside the container.  &#x60;container-dest&#x60; must be an _absolute_ path.  | [optional] 
**ContainerIDFile** | **string** | Path to a file where the container ID is written | [optional] 
**LogConfig** | [**DockerHostConfigAllOfLogConfig**](DockerHostConfigAllOfLogConfig.md) |  | [optional] 
**NetworkMode** | **string** | Network mode to use for this container. Supported standard values are: &#x60;bridge&#x60;, &#x60;host&#x60;, &#x60;none&#x60;, and &#x60;container:&lt;name|id&gt;&#x60;. Any other value is taken as a custom network&#39;s name to which this container should connect to. | [optional] 
**PortBindings** | **Dictionary&lt;string, List&lt;DockerPortBinding&gt;&gt;** | PortMap describes the mapping of container ports to host ports, using the container&#39;s port-number and protocol as key in the format &#x60;&lt;port&gt;/&lt;protocol&gt;&#x60;, for example, &#x60;80/udp&#x60;.  If a container&#39;s port is mapped for multiple protocols, separate entries are added to the mapping table.  | [optional] 
**RestartPolicy** | [**DockerRestartPolicy**](DockerRestartPolicy.md) |  | [optional] 
**AutoRemove** | **bool** | Automatically remove the container when the container&#39;s process exits. This has no effect if &#x60;RestartPolicy&#x60; is set. | [optional] 
**VolumeDriver** | **string** | Driver that this container uses to mount volumes. | [optional] 
**VolumesFrom** | **List&lt;string&gt;** | A list of volumes to inherit from another container, specified in the form &#x60;&lt;container name&gt;[:&lt;ro|rw&gt;]&#x60;. | [optional] 
**Mounts** | [**List&lt;DockerMount&gt;**](DockerMount.md) | Specification for mounts to be added to the container. | [optional] 
**CapAdd** | **List&lt;string&gt;** | A list of kernel capabilities to add to the container. | [optional] 
**CapDrop** | **List&lt;string&gt;** | A list of kernel capabilities to drop from the container. | [optional] 
**Dns** | **List&lt;string&gt;** | A list of DNS servers for the container to use. | [optional] 
**DnsOptions** | **List&lt;string&gt;** | A list of DNS options. | [optional] 
**DnsSearch** | **List&lt;string&gt;** | A list of DNS search domains. | [optional] 
**ExtraHosts** | **List&lt;string&gt;** | A list of hostnames/IP mappings to add to the container&#39;s &#x60;/etc/hosts&#x60; file. Specified in the form &#x60;[\&quot;hostname:IP\&quot;]&#x60;.  | [optional] 
**GroupAdd** | **List&lt;string&gt;** | A list of additional groups that the container process will run as. | [optional] 
**IpcMode** | **string** | IPC sharing mode for the container. Possible values are:  - &#x60;\&quot;none\&quot;&#x60;: own private IPC namespace, with /dev/shm not mounted - &#x60;\&quot;private\&quot;&#x60;: own private IPC namespace - &#x60;\&quot;shareable\&quot;&#x60;: own private IPC namespace, with a possibility to share it with other containers - &#x60;\&quot;container:&lt;name|id&gt;\&quot;&#x60;: join another (shareable) container&#39;s IPC namespace - &#x60;\&quot;host\&quot;&#x60;: use the host system&#39;s IPC namespace  If not specified, daemon default is used, which can either be &#x60;\&quot;private\&quot;&#x60; or &#x60;\&quot;shareable\&quot;&#x60;, depending on daemon version and configuration.  | [optional] 
**Cgroup** | **string** | Cgroup to use for the container. | [optional] 
**Links** | **List&lt;string&gt;** | A list of links for the container in the form &#x60;container_name:alias&#x60;. | [optional] 
**OomScoreAdj** | **int** | An integer value containing the score given to the container in order to tune OOM killer preferences. | [optional] 
**PidMode** | **string** | Set the PID (Process) Namespace mode for the container. It can be either:  - &#x60;\&quot;container:&lt;name|id&gt;\&quot;&#x60;: joins another container&#39;s PID namespace - &#x60;\&quot;host\&quot;&#x60;: use the host&#39;s PID namespace inside the container  | [optional] 
**Privileged** | **bool** | Gives the container full access to the host. | [optional] 
**PublishAllPorts** | **bool** | Allocates an ephemeral host port for all of a container&#39;s exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by &#x60;/proc/sys/net/ipv4/ip_local_port_range&#x60;.  | [optional] 
**ReadonlyRootfs** | **bool** | Mount the container&#39;s root filesystem as read only. | [optional] 
**SecurityOpt** | **List&lt;string&gt;** | A list of string values to customize labels for MLS systems, such as SELinux. | [optional] 
**StorageOpt** | **Dictionary&lt;string, string&gt;** | Storage driver options for this container, in the form &#x60;{\&quot;size\&quot;: \&quot;120G\&quot;}&#x60;.  | [optional] 
**Tmpfs** | **Dictionary&lt;string, string&gt;** | A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: &#x60;{ \&quot;/run\&quot;: \&quot;rw,noexec,nosuid,size&#x3D;65536k\&quot; }&#x60;.  | [optional] 
**UTSMode** | **string** | UTS namespace to use for the container. | [optional] 
**UsernsMode** | **string** | Sets the usernamespace mode for the container when usernamespace remapping option is enabled. | [optional] 
**ShmSize** | **int** | Size of &#x60;/dev/shm&#x60; in bytes. If omitted, the system uses 64MB. | [optional] 
**Sysctls** | **Dictionary&lt;string, string&gt;** | A list of kernel parameters (sysctls) to set in the container. For example: &#x60;{\&quot;net.ipv4.ip_forward\&quot;: \&quot;1\&quot;}&#x60;  | [optional] 
**Runtime** | **string** | Runtime to use with this container. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

