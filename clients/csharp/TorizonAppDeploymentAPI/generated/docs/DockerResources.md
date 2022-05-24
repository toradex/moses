
# TorizonRestAPI.Model.DockerResources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CpuShares** | **int** | An integer value representing this container&#39;s relative CPU weight versus other containers. | [optional] 
**Memory** | **long** | Memory limit in bytes. | [optional] [default to 0]
**CgroupParent** | **string** | Path to &#x60;cgroups&#x60; under which the container&#39;s &#x60;cgroup&#x60; is created. If the path is not absolute, the path is considered to be relative to the &#x60;cgroups&#x60; path of the init process. Cgroups are created if they do not already exist. | [optional] 
**BlkioWeight** | **int** | Block IO weight (relative weight). | [optional] 
**BlkioWeightDevice** | [**List&lt;DockerResourcesBlkioWeightDeviceInner&gt;**](DockerResourcesBlkioWeightDeviceInner.md) | Block IO weight (relative device weight) in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Weight\&quot;: weight}]&#x60;.  | [optional] 
**BlkioDeviceReadBps** | [**List&lt;DockerThrottleDevice&gt;**](DockerThrottleDevice.md) | Limit read rate (bytes per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;.  | [optional] 
**BlkioDeviceWriteBps** | [**List&lt;DockerThrottleDevice&gt;**](DockerThrottleDevice.md) | Limit write rate (bytes per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;.  | [optional] 
**BlkioDeviceReadIOps** | [**List&lt;DockerThrottleDevice&gt;**](DockerThrottleDevice.md) | Limit read rate (IO per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;.  | [optional] 
**BlkioDeviceWriteIOps** | [**List&lt;DockerThrottleDevice&gt;**](DockerThrottleDevice.md) | Limit write rate (IO per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;.  | [optional] 
**CpuPeriod** | **long** | The length of a CPU period in microseconds. | [optional] 
**CpuQuota** | **long** | Microseconds of CPU time that the container can get in a CPU period. | [optional] 
**CpuRealtimePeriod** | **long** | The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks. | [optional] 
**CpuRealtimeRuntime** | **long** | The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks. | [optional] 
**CpusetCpus** | **string** | CPUs in which to allow execution (e.g., &#x60;0-3&#x60;, &#x60;0,1&#x60;) | [optional] 
**CpusetMems** | **string** | Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems. | [optional] 
**Devices** | [**List&lt;DockerDeviceMapping&gt;**](DockerDeviceMapping.md) | A list of devices to add to the container. | [optional] 
**DeviceCgroupRules** | **List&lt;string&gt;** | a list of cgroup rules to apply to the container | [optional] 
**DiskQuota** | **long** | Disk limit (in bytes). | [optional] 
**KernelMemory** | **long** | Kernel memory limit in bytes. | [optional] 
**MemoryReservation** | **long** | Memory soft limit in bytes. | [optional] 
**MemorySwap** | **long** | Total memory limit (memory + swap). Set as &#x60;-1&#x60; to enable unlimited swap. | [optional] 
**MemorySwappiness** | **long?** | Tune a container&#39;s memory swappiness behavior. Accepts an integer between 0 and 100. | [optional] 
**NanoCPUs** | **long** | CPU quota in units of 10&lt;sup&gt;-9&lt;/sup&gt; CPUs. | [optional] 
**OomKillDisable** | **bool** | Disable OOM Killer for the container. | [optional] 
**Init** | **bool?** | Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used. | [optional] 
**PidsLimit** | **long?** | Tune a container&#39;s pids limit. Set -1 for unlimited. | [optional] 
**Ulimits** | [**List&lt;DockerResourcesUlimitsInner&gt;**](DockerResourcesUlimitsInner.md) | A list of resource limits to set in the container. For example: &#x60;{\&quot;Name\&quot;: \&quot;nofile\&quot;, \&quot;Soft\&quot;: 1024, \&quot;Hard\&quot;: 2048}&#x60;\&quot;  | [optional] 
**CpuCount** | **long** | The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last.  | [optional] 
**CpuPercent** | **long** | The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last.  | [optional] 
**IOMaximumIOps** | **long** | Maximum IOps for the container system drive (Windows only) | [optional] 
**IOMaximumBandwidth** | **long** | Maximum IO in bytes per second for the container system drive (Windows only) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to README]](../README.md)

