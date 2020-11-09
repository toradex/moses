/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.11
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = TorizonRestAPI.Client.OpenAPIDateConverter;

namespace TorizonRestAPI.Model
{
    /// <summary>
    /// A container&#39;s resources (cgroups config, ulimits, etc)
    /// </summary>
    [DataContract]
    public partial class DockerResources :  IEquatable<DockerResources>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerResources" /> class.
        /// </summary>
        /// <param name="cpuShares">An integer value representing this container&#39;s relative CPU weight versus other containers..</param>
        /// <param name="memory">Memory limit in bytes. (default to 0).</param>
        /// <param name="cgroupParent">Path to &#x60;cgroups&#x60; under which the container&#39;s &#x60;cgroup&#x60; is created. If the path is not absolute, the path is considered to be relative to the &#x60;cgroups&#x60; path of the init process. Cgroups are created if they do not already exist..</param>
        /// <param name="blkioWeight">Block IO weight (relative weight)..</param>
        /// <param name="blkioWeightDevice">Block IO weight (relative device weight) in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Weight\&quot;: weight}]&#x60;. .</param>
        /// <param name="blkioDeviceReadBps">Limit read rate (bytes per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. .</param>
        /// <param name="blkioDeviceWriteBps">Limit write rate (bytes per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. .</param>
        /// <param name="blkioDeviceReadIOps">Limit read rate (IO per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. .</param>
        /// <param name="blkioDeviceWriteIOps">Limit write rate (IO per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. .</param>
        /// <param name="cpuPeriod">The length of a CPU period in microseconds..</param>
        /// <param name="cpuQuota">Microseconds of CPU time that the container can get in a CPU period..</param>
        /// <param name="cpuRealtimePeriod">The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks..</param>
        /// <param name="cpuRealtimeRuntime">The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks..</param>
        /// <param name="cpusetCpus">CPUs in which to allow execution (e.g., &#x60;0-3&#x60;, &#x60;0,1&#x60;).</param>
        /// <param name="cpusetMems">Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems..</param>
        /// <param name="devices">A list of devices to add to the container..</param>
        /// <param name="deviceCgroupRules">a list of cgroup rules to apply to the container.</param>
        /// <param name="diskQuota">Disk limit (in bytes)..</param>
        /// <param name="kernelMemory">Kernel memory limit in bytes..</param>
        /// <param name="memoryReservation">Memory soft limit in bytes..</param>
        /// <param name="memorySwap">Total memory limit (memory + swap). Set as &#x60;-1&#x60; to enable unlimited swap..</param>
        /// <param name="memorySwappiness">Tune a container&#39;s memory swappiness behavior. Accepts an integer between 0 and 100..</param>
        /// <param name="nanoCPUs">CPU quota in units of 10&lt;sup&gt;-9&lt;/sup&gt; CPUs..</param>
        /// <param name="oomKillDisable">Disable OOM Killer for the container..</param>
        /// <param name="init">Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used..</param>
        /// <param name="pidsLimit">Tune a container&#39;s pids limit. Set -1 for unlimited..</param>
        /// <param name="ulimits">A list of resource limits to set in the container. For example: &#x60;{\&quot;Name\&quot;: \&quot;nofile\&quot;, \&quot;Soft\&quot;: 1024, \&quot;Hard\&quot;: 2048}&#x60;\&quot; .</param>
        /// <param name="cpuCount">The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. .</param>
        /// <param name="cpuPercent">The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. .</param>
        /// <param name="iOMaximumIOps">Maximum IOps for the container system drive (Windows only).</param>
        /// <param name="iOMaximumBandwidth">Maximum IO in bytes per second for the container system drive (Windows only).</param>
        public DockerResources(int cpuShares = default(int), long memory = 0, string cgroupParent = default(string), int blkioWeight = default(int), List<DockerResourcesBlkioWeightDevice> blkioWeightDevice = default(List<DockerResourcesBlkioWeightDevice>), List<DockerThrottleDevice> blkioDeviceReadBps = default(List<DockerThrottleDevice>), List<DockerThrottleDevice> blkioDeviceWriteBps = default(List<DockerThrottleDevice>), List<DockerThrottleDevice> blkioDeviceReadIOps = default(List<DockerThrottleDevice>), List<DockerThrottleDevice> blkioDeviceWriteIOps = default(List<DockerThrottleDevice>), long cpuPeriod = default(long), long cpuQuota = default(long), long cpuRealtimePeriod = default(long), long cpuRealtimeRuntime = default(long), string cpusetCpus = default(string), string cpusetMems = default(string), List<DockerDeviceMapping> devices = default(List<DockerDeviceMapping>), List<string> deviceCgroupRules = default(List<string>), long diskQuota = default(long), long kernelMemory = default(long), long memoryReservation = default(long), long memorySwap = default(long), long? memorySwappiness = default(long?), long nanoCPUs = default(long), bool oomKillDisable = default(bool), bool? init = default(bool?), long? pidsLimit = default(long?), List<DockerResourcesUlimits> ulimits = default(List<DockerResourcesUlimits>), long cpuCount = default(long), long cpuPercent = default(long), long iOMaximumIOps = default(long), long iOMaximumBandwidth = default(long))
        {
            this.MemorySwappiness = memorySwappiness;
            this.Init = init;
            this.PidsLimit = pidsLimit;
            this.CpuShares = cpuShares;
            // use default value if no "memory" provided
            if (memory == null)
            {
                this.Memory = 0;
            }
            else
            {
                this.Memory = memory;
            }
            this.CgroupParent = cgroupParent;
            this.BlkioWeight = blkioWeight;
            this.BlkioWeightDevice = blkioWeightDevice;
            this.BlkioDeviceReadBps = blkioDeviceReadBps;
            this.BlkioDeviceWriteBps = blkioDeviceWriteBps;
            this.BlkioDeviceReadIOps = blkioDeviceReadIOps;
            this.BlkioDeviceWriteIOps = blkioDeviceWriteIOps;
            this.CpuPeriod = cpuPeriod;
            this.CpuQuota = cpuQuota;
            this.CpuRealtimePeriod = cpuRealtimePeriod;
            this.CpuRealtimeRuntime = cpuRealtimeRuntime;
            this.CpusetCpus = cpusetCpus;
            this.CpusetMems = cpusetMems;
            this.Devices = devices;
            this.DeviceCgroupRules = deviceCgroupRules;
            this.DiskQuota = diskQuota;
            this.KernelMemory = kernelMemory;
            this.MemoryReservation = memoryReservation;
            this.MemorySwap = memorySwap;
            this.MemorySwappiness = memorySwappiness;
            this.NanoCPUs = nanoCPUs;
            this.OomKillDisable = oomKillDisable;
            this.Init = init;
            this.PidsLimit = pidsLimit;
            this.Ulimits = ulimits;
            this.CpuCount = cpuCount;
            this.CpuPercent = cpuPercent;
            this.IOMaximumIOps = iOMaximumIOps;
            this.IOMaximumBandwidth = iOMaximumBandwidth;
        }
        
        /// <summary>
        /// An integer value representing this container&#39;s relative CPU weight versus other containers.
        /// </summary>
        /// <value>An integer value representing this container&#39;s relative CPU weight versus other containers.</value>
        [DataMember(Name="CpuShares", EmitDefaultValue=false)]
        public int CpuShares { get; set; }

        /// <summary>
        /// Memory limit in bytes.
        /// </summary>
        /// <value>Memory limit in bytes.</value>
        [DataMember(Name="Memory", EmitDefaultValue=false)]
        public long Memory { get; set; }

        /// <summary>
        /// Path to &#x60;cgroups&#x60; under which the container&#39;s &#x60;cgroup&#x60; is created. If the path is not absolute, the path is considered to be relative to the &#x60;cgroups&#x60; path of the init process. Cgroups are created if they do not already exist.
        /// </summary>
        /// <value>Path to &#x60;cgroups&#x60; under which the container&#39;s &#x60;cgroup&#x60; is created. If the path is not absolute, the path is considered to be relative to the &#x60;cgroups&#x60; path of the init process. Cgroups are created if they do not already exist.</value>
        [DataMember(Name="CgroupParent", EmitDefaultValue=false)]
        public string CgroupParent { get; set; }

        /// <summary>
        /// Block IO weight (relative weight).
        /// </summary>
        /// <value>Block IO weight (relative weight).</value>
        [DataMember(Name="BlkioWeight", EmitDefaultValue=false)]
        public int BlkioWeight { get; set; }

        /// <summary>
        /// Block IO weight (relative device weight) in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Weight\&quot;: weight}]&#x60;. 
        /// </summary>
        /// <value>Block IO weight (relative device weight) in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Weight\&quot;: weight}]&#x60;. </value>
        [DataMember(Name="BlkioWeightDevice", EmitDefaultValue=false)]
        public List<DockerResourcesBlkioWeightDevice> BlkioWeightDevice { get; set; }

        /// <summary>
        /// Limit read rate (bytes per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. 
        /// </summary>
        /// <value>Limit read rate (bytes per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. </value>
        [DataMember(Name="BlkioDeviceReadBps", EmitDefaultValue=false)]
        public List<DockerThrottleDevice> BlkioDeviceReadBps { get; set; }

        /// <summary>
        /// Limit write rate (bytes per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. 
        /// </summary>
        /// <value>Limit write rate (bytes per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. </value>
        [DataMember(Name="BlkioDeviceWriteBps", EmitDefaultValue=false)]
        public List<DockerThrottleDevice> BlkioDeviceWriteBps { get; set; }

        /// <summary>
        /// Limit read rate (IO per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. 
        /// </summary>
        /// <value>Limit read rate (IO per second) from a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. </value>
        [DataMember(Name="BlkioDeviceReadIOps", EmitDefaultValue=false)]
        public List<DockerThrottleDevice> BlkioDeviceReadIOps { get; set; }

        /// <summary>
        /// Limit write rate (IO per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. 
        /// </summary>
        /// <value>Limit write rate (IO per second) to a device, in the form &#x60;[{\&quot;Path\&quot;: \&quot;device_path\&quot;, \&quot;Rate\&quot;: rate}]&#x60;. </value>
        [DataMember(Name="BlkioDeviceWriteIOps", EmitDefaultValue=false)]
        public List<DockerThrottleDevice> BlkioDeviceWriteIOps { get; set; }

        /// <summary>
        /// The length of a CPU period in microseconds.
        /// </summary>
        /// <value>The length of a CPU period in microseconds.</value>
        [DataMember(Name="CpuPeriod", EmitDefaultValue=false)]
        public long CpuPeriod { get; set; }

        /// <summary>
        /// Microseconds of CPU time that the container can get in a CPU period.
        /// </summary>
        /// <value>Microseconds of CPU time that the container can get in a CPU period.</value>
        [DataMember(Name="CpuQuota", EmitDefaultValue=false)]
        public long CpuQuota { get; set; }

        /// <summary>
        /// The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks.
        /// </summary>
        /// <value>The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks.</value>
        [DataMember(Name="CpuRealtimePeriod", EmitDefaultValue=false)]
        public long CpuRealtimePeriod { get; set; }

        /// <summary>
        /// The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks.
        /// </summary>
        /// <value>The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks.</value>
        [DataMember(Name="CpuRealtimeRuntime", EmitDefaultValue=false)]
        public long CpuRealtimeRuntime { get; set; }

        /// <summary>
        /// CPUs in which to allow execution (e.g., &#x60;0-3&#x60;, &#x60;0,1&#x60;)
        /// </summary>
        /// <value>CPUs in which to allow execution (e.g., &#x60;0-3&#x60;, &#x60;0,1&#x60;)</value>
        [DataMember(Name="CpusetCpus", EmitDefaultValue=false)]
        public string CpusetCpus { get; set; }

        /// <summary>
        /// Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.
        /// </summary>
        /// <value>Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.</value>
        [DataMember(Name="CpusetMems", EmitDefaultValue=false)]
        public string CpusetMems { get; set; }

        /// <summary>
        /// A list of devices to add to the container.
        /// </summary>
        /// <value>A list of devices to add to the container.</value>
        [DataMember(Name="Devices", EmitDefaultValue=false)]
        public List<DockerDeviceMapping> Devices { get; set; }

        /// <summary>
        /// a list of cgroup rules to apply to the container
        /// </summary>
        /// <value>a list of cgroup rules to apply to the container</value>
        [DataMember(Name="DeviceCgroupRules", EmitDefaultValue=false)]
        public List<string> DeviceCgroupRules { get; set; }

        /// <summary>
        /// Disk limit (in bytes).
        /// </summary>
        /// <value>Disk limit (in bytes).</value>
        [DataMember(Name="DiskQuota", EmitDefaultValue=false)]
        public long DiskQuota { get; set; }

        /// <summary>
        /// Kernel memory limit in bytes.
        /// </summary>
        /// <value>Kernel memory limit in bytes.</value>
        [DataMember(Name="KernelMemory", EmitDefaultValue=false)]
        public long KernelMemory { get; set; }

        /// <summary>
        /// Memory soft limit in bytes.
        /// </summary>
        /// <value>Memory soft limit in bytes.</value>
        [DataMember(Name="MemoryReservation", EmitDefaultValue=false)]
        public long MemoryReservation { get; set; }

        /// <summary>
        /// Total memory limit (memory + swap). Set as &#x60;-1&#x60; to enable unlimited swap.
        /// </summary>
        /// <value>Total memory limit (memory + swap). Set as &#x60;-1&#x60; to enable unlimited swap.</value>
        [DataMember(Name="MemorySwap", EmitDefaultValue=false)]
        public long MemorySwap { get; set; }

        /// <summary>
        /// Tune a container&#39;s memory swappiness behavior. Accepts an integer between 0 and 100.
        /// </summary>
        /// <value>Tune a container&#39;s memory swappiness behavior. Accepts an integer between 0 and 100.</value>
        [DataMember(Name="MemorySwappiness", EmitDefaultValue=true)]
        public long? MemorySwappiness { get; set; }

        /// <summary>
        /// CPU quota in units of 10&lt;sup&gt;-9&lt;/sup&gt; CPUs.
        /// </summary>
        /// <value>CPU quota in units of 10&lt;sup&gt;-9&lt;/sup&gt; CPUs.</value>
        [DataMember(Name="NanoCPUs", EmitDefaultValue=false)]
        public long NanoCPUs { get; set; }

        /// <summary>
        /// Disable OOM Killer for the container.
        /// </summary>
        /// <value>Disable OOM Killer for the container.</value>
        [DataMember(Name="OomKillDisable", EmitDefaultValue=false)]
        public bool OomKillDisable { get; set; }

        /// <summary>
        /// Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used.
        /// </summary>
        /// <value>Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used.</value>
        [DataMember(Name="Init", EmitDefaultValue=true)]
        public bool? Init { get; set; }

        /// <summary>
        /// Tune a container&#39;s pids limit. Set -1 for unlimited.
        /// </summary>
        /// <value>Tune a container&#39;s pids limit. Set -1 for unlimited.</value>
        [DataMember(Name="PidsLimit", EmitDefaultValue=true)]
        public long? PidsLimit { get; set; }

        /// <summary>
        /// A list of resource limits to set in the container. For example: &#x60;{\&quot;Name\&quot;: \&quot;nofile\&quot;, \&quot;Soft\&quot;: 1024, \&quot;Hard\&quot;: 2048}&#x60;\&quot; 
        /// </summary>
        /// <value>A list of resource limits to set in the container. For example: &#x60;{\&quot;Name\&quot;: \&quot;nofile\&quot;, \&quot;Soft\&quot;: 1024, \&quot;Hard\&quot;: 2048}&#x60;\&quot; </value>
        [DataMember(Name="Ulimits", EmitDefaultValue=false)]
        public List<DockerResourcesUlimits> Ulimits { get; set; }

        /// <summary>
        /// The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. 
        /// </summary>
        /// <value>The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. </value>
        [DataMember(Name="CpuCount", EmitDefaultValue=false)]
        public long CpuCount { get; set; }

        /// <summary>
        /// The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. 
        /// </summary>
        /// <value>The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is &#x60;CPUCount&#x60; first, then &#x60;CPUShares&#x60;, and &#x60;CPUPercent&#x60; last. </value>
        [DataMember(Name="CpuPercent", EmitDefaultValue=false)]
        public long CpuPercent { get; set; }

        /// <summary>
        /// Maximum IOps for the container system drive (Windows only)
        /// </summary>
        /// <value>Maximum IOps for the container system drive (Windows only)</value>
        [DataMember(Name="IOMaximumIOps", EmitDefaultValue=false)]
        public long IOMaximumIOps { get; set; }

        /// <summary>
        /// Maximum IO in bytes per second for the container system drive (Windows only)
        /// </summary>
        /// <value>Maximum IO in bytes per second for the container system drive (Windows only)</value>
        [DataMember(Name="IOMaximumBandwidth", EmitDefaultValue=false)]
        public long IOMaximumBandwidth { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerResources {\n");
            sb.Append("  CpuShares: ").Append(CpuShares).Append("\n");
            sb.Append("  Memory: ").Append(Memory).Append("\n");
            sb.Append("  CgroupParent: ").Append(CgroupParent).Append("\n");
            sb.Append("  BlkioWeight: ").Append(BlkioWeight).Append("\n");
            sb.Append("  BlkioWeightDevice: ").Append(BlkioWeightDevice).Append("\n");
            sb.Append("  BlkioDeviceReadBps: ").Append(BlkioDeviceReadBps).Append("\n");
            sb.Append("  BlkioDeviceWriteBps: ").Append(BlkioDeviceWriteBps).Append("\n");
            sb.Append("  BlkioDeviceReadIOps: ").Append(BlkioDeviceReadIOps).Append("\n");
            sb.Append("  BlkioDeviceWriteIOps: ").Append(BlkioDeviceWriteIOps).Append("\n");
            sb.Append("  CpuPeriod: ").Append(CpuPeriod).Append("\n");
            sb.Append("  CpuQuota: ").Append(CpuQuota).Append("\n");
            sb.Append("  CpuRealtimePeriod: ").Append(CpuRealtimePeriod).Append("\n");
            sb.Append("  CpuRealtimeRuntime: ").Append(CpuRealtimeRuntime).Append("\n");
            sb.Append("  CpusetCpus: ").Append(CpusetCpus).Append("\n");
            sb.Append("  CpusetMems: ").Append(CpusetMems).Append("\n");
            sb.Append("  Devices: ").Append(Devices).Append("\n");
            sb.Append("  DeviceCgroupRules: ").Append(DeviceCgroupRules).Append("\n");
            sb.Append("  DiskQuota: ").Append(DiskQuota).Append("\n");
            sb.Append("  KernelMemory: ").Append(KernelMemory).Append("\n");
            sb.Append("  MemoryReservation: ").Append(MemoryReservation).Append("\n");
            sb.Append("  MemorySwap: ").Append(MemorySwap).Append("\n");
            sb.Append("  MemorySwappiness: ").Append(MemorySwappiness).Append("\n");
            sb.Append("  NanoCPUs: ").Append(NanoCPUs).Append("\n");
            sb.Append("  OomKillDisable: ").Append(OomKillDisable).Append("\n");
            sb.Append("  Init: ").Append(Init).Append("\n");
            sb.Append("  PidsLimit: ").Append(PidsLimit).Append("\n");
            sb.Append("  Ulimits: ").Append(Ulimits).Append("\n");
            sb.Append("  CpuCount: ").Append(CpuCount).Append("\n");
            sb.Append("  CpuPercent: ").Append(CpuPercent).Append("\n");
            sb.Append("  IOMaximumIOps: ").Append(IOMaximumIOps).Append("\n");
            sb.Append("  IOMaximumBandwidth: ").Append(IOMaximumBandwidth).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as DockerResources);
        }

        /// <summary>
        /// Returns true if DockerResources instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerResources to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerResources input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.CpuShares == input.CpuShares ||
                    (this.CpuShares != null &&
                    this.CpuShares.Equals(input.CpuShares))
                ) && 
                (
                    this.Memory == input.Memory ||
                    (this.Memory != null &&
                    this.Memory.Equals(input.Memory))
                ) && 
                (
                    this.CgroupParent == input.CgroupParent ||
                    (this.CgroupParent != null &&
                    this.CgroupParent.Equals(input.CgroupParent))
                ) && 
                (
                    this.BlkioWeight == input.BlkioWeight ||
                    (this.BlkioWeight != null &&
                    this.BlkioWeight.Equals(input.BlkioWeight))
                ) && 
                (
                    this.BlkioWeightDevice == input.BlkioWeightDevice ||
                    this.BlkioWeightDevice != null &&
                    input.BlkioWeightDevice != null &&
                    this.BlkioWeightDevice.SequenceEqual(input.BlkioWeightDevice)
                ) && 
                (
                    this.BlkioDeviceReadBps == input.BlkioDeviceReadBps ||
                    this.BlkioDeviceReadBps != null &&
                    input.BlkioDeviceReadBps != null &&
                    this.BlkioDeviceReadBps.SequenceEqual(input.BlkioDeviceReadBps)
                ) && 
                (
                    this.BlkioDeviceWriteBps == input.BlkioDeviceWriteBps ||
                    this.BlkioDeviceWriteBps != null &&
                    input.BlkioDeviceWriteBps != null &&
                    this.BlkioDeviceWriteBps.SequenceEqual(input.BlkioDeviceWriteBps)
                ) && 
                (
                    this.BlkioDeviceReadIOps == input.BlkioDeviceReadIOps ||
                    this.BlkioDeviceReadIOps != null &&
                    input.BlkioDeviceReadIOps != null &&
                    this.BlkioDeviceReadIOps.SequenceEqual(input.BlkioDeviceReadIOps)
                ) && 
                (
                    this.BlkioDeviceWriteIOps == input.BlkioDeviceWriteIOps ||
                    this.BlkioDeviceWriteIOps != null &&
                    input.BlkioDeviceWriteIOps != null &&
                    this.BlkioDeviceWriteIOps.SequenceEqual(input.BlkioDeviceWriteIOps)
                ) && 
                (
                    this.CpuPeriod == input.CpuPeriod ||
                    (this.CpuPeriod != null &&
                    this.CpuPeriod.Equals(input.CpuPeriod))
                ) && 
                (
                    this.CpuQuota == input.CpuQuota ||
                    (this.CpuQuota != null &&
                    this.CpuQuota.Equals(input.CpuQuota))
                ) && 
                (
                    this.CpuRealtimePeriod == input.CpuRealtimePeriod ||
                    (this.CpuRealtimePeriod != null &&
                    this.CpuRealtimePeriod.Equals(input.CpuRealtimePeriod))
                ) && 
                (
                    this.CpuRealtimeRuntime == input.CpuRealtimeRuntime ||
                    (this.CpuRealtimeRuntime != null &&
                    this.CpuRealtimeRuntime.Equals(input.CpuRealtimeRuntime))
                ) && 
                (
                    this.CpusetCpus == input.CpusetCpus ||
                    (this.CpusetCpus != null &&
                    this.CpusetCpus.Equals(input.CpusetCpus))
                ) && 
                (
                    this.CpusetMems == input.CpusetMems ||
                    (this.CpusetMems != null &&
                    this.CpusetMems.Equals(input.CpusetMems))
                ) && 
                (
                    this.Devices == input.Devices ||
                    this.Devices != null &&
                    input.Devices != null &&
                    this.Devices.SequenceEqual(input.Devices)
                ) && 
                (
                    this.DeviceCgroupRules == input.DeviceCgroupRules ||
                    this.DeviceCgroupRules != null &&
                    input.DeviceCgroupRules != null &&
                    this.DeviceCgroupRules.SequenceEqual(input.DeviceCgroupRules)
                ) && 
                (
                    this.DiskQuota == input.DiskQuota ||
                    (this.DiskQuota != null &&
                    this.DiskQuota.Equals(input.DiskQuota))
                ) && 
                (
                    this.KernelMemory == input.KernelMemory ||
                    (this.KernelMemory != null &&
                    this.KernelMemory.Equals(input.KernelMemory))
                ) && 
                (
                    this.MemoryReservation == input.MemoryReservation ||
                    (this.MemoryReservation != null &&
                    this.MemoryReservation.Equals(input.MemoryReservation))
                ) && 
                (
                    this.MemorySwap == input.MemorySwap ||
                    (this.MemorySwap != null &&
                    this.MemorySwap.Equals(input.MemorySwap))
                ) && 
                (
                    this.MemorySwappiness == input.MemorySwappiness ||
                    (this.MemorySwappiness != null &&
                    this.MemorySwappiness.Equals(input.MemorySwappiness))
                ) && 
                (
                    this.NanoCPUs == input.NanoCPUs ||
                    (this.NanoCPUs != null &&
                    this.NanoCPUs.Equals(input.NanoCPUs))
                ) && 
                (
                    this.OomKillDisable == input.OomKillDisable ||
                    (this.OomKillDisable != null &&
                    this.OomKillDisable.Equals(input.OomKillDisable))
                ) && 
                (
                    this.Init == input.Init ||
                    (this.Init != null &&
                    this.Init.Equals(input.Init))
                ) && 
                (
                    this.PidsLimit == input.PidsLimit ||
                    (this.PidsLimit != null &&
                    this.PidsLimit.Equals(input.PidsLimit))
                ) && 
                (
                    this.Ulimits == input.Ulimits ||
                    this.Ulimits != null &&
                    input.Ulimits != null &&
                    this.Ulimits.SequenceEqual(input.Ulimits)
                ) && 
                (
                    this.CpuCount == input.CpuCount ||
                    (this.CpuCount != null &&
                    this.CpuCount.Equals(input.CpuCount))
                ) && 
                (
                    this.CpuPercent == input.CpuPercent ||
                    (this.CpuPercent != null &&
                    this.CpuPercent.Equals(input.CpuPercent))
                ) && 
                (
                    this.IOMaximumIOps == input.IOMaximumIOps ||
                    (this.IOMaximumIOps != null &&
                    this.IOMaximumIOps.Equals(input.IOMaximumIOps))
                ) && 
                (
                    this.IOMaximumBandwidth == input.IOMaximumBandwidth ||
                    (this.IOMaximumBandwidth != null &&
                    this.IOMaximumBandwidth.Equals(input.IOMaximumBandwidth))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.CpuShares != null)
                    hashCode = hashCode * 59 + this.CpuShares.GetHashCode();
                if (this.Memory != null)
                    hashCode = hashCode * 59 + this.Memory.GetHashCode();
                if (this.CgroupParent != null)
                    hashCode = hashCode * 59 + this.CgroupParent.GetHashCode();
                if (this.BlkioWeight != null)
                    hashCode = hashCode * 59 + this.BlkioWeight.GetHashCode();
                if (this.BlkioWeightDevice != null)
                    hashCode = hashCode * 59 + this.BlkioWeightDevice.GetHashCode();
                if (this.BlkioDeviceReadBps != null)
                    hashCode = hashCode * 59 + this.BlkioDeviceReadBps.GetHashCode();
                if (this.BlkioDeviceWriteBps != null)
                    hashCode = hashCode * 59 + this.BlkioDeviceWriteBps.GetHashCode();
                if (this.BlkioDeviceReadIOps != null)
                    hashCode = hashCode * 59 + this.BlkioDeviceReadIOps.GetHashCode();
                if (this.BlkioDeviceWriteIOps != null)
                    hashCode = hashCode * 59 + this.BlkioDeviceWriteIOps.GetHashCode();
                if (this.CpuPeriod != null)
                    hashCode = hashCode * 59 + this.CpuPeriod.GetHashCode();
                if (this.CpuQuota != null)
                    hashCode = hashCode * 59 + this.CpuQuota.GetHashCode();
                if (this.CpuRealtimePeriod != null)
                    hashCode = hashCode * 59 + this.CpuRealtimePeriod.GetHashCode();
                if (this.CpuRealtimeRuntime != null)
                    hashCode = hashCode * 59 + this.CpuRealtimeRuntime.GetHashCode();
                if (this.CpusetCpus != null)
                    hashCode = hashCode * 59 + this.CpusetCpus.GetHashCode();
                if (this.CpusetMems != null)
                    hashCode = hashCode * 59 + this.CpusetMems.GetHashCode();
                if (this.Devices != null)
                    hashCode = hashCode * 59 + this.Devices.GetHashCode();
                if (this.DeviceCgroupRules != null)
                    hashCode = hashCode * 59 + this.DeviceCgroupRules.GetHashCode();
                if (this.DiskQuota != null)
                    hashCode = hashCode * 59 + this.DiskQuota.GetHashCode();
                if (this.KernelMemory != null)
                    hashCode = hashCode * 59 + this.KernelMemory.GetHashCode();
                if (this.MemoryReservation != null)
                    hashCode = hashCode * 59 + this.MemoryReservation.GetHashCode();
                if (this.MemorySwap != null)
                    hashCode = hashCode * 59 + this.MemorySwap.GetHashCode();
                if (this.MemorySwappiness != null)
                    hashCode = hashCode * 59 + this.MemorySwappiness.GetHashCode();
                if (this.NanoCPUs != null)
                    hashCode = hashCode * 59 + this.NanoCPUs.GetHashCode();
                if (this.OomKillDisable != null)
                    hashCode = hashCode * 59 + this.OomKillDisable.GetHashCode();
                if (this.Init != null)
                    hashCode = hashCode * 59 + this.Init.GetHashCode();
                if (this.PidsLimit != null)
                    hashCode = hashCode * 59 + this.PidsLimit.GetHashCode();
                if (this.Ulimits != null)
                    hashCode = hashCode * 59 + this.Ulimits.GetHashCode();
                if (this.CpuCount != null)
                    hashCode = hashCode * 59 + this.CpuCount.GetHashCode();
                if (this.CpuPercent != null)
                    hashCode = hashCode * 59 + this.CpuPercent.GetHashCode();
                if (this.IOMaximumIOps != null)
                    hashCode = hashCode * 59 + this.IOMaximumIOps.GetHashCode();
                if (this.IOMaximumBandwidth != null)
                    hashCode = hashCode * 59 + this.IOMaximumBandwidth.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {

            
            // BlkioWeight (int) maximum
            if(this.BlkioWeight > (int)1000)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for BlkioWeight, must be a value less than or equal to 1000.", new [] { "BlkioWeight" });
            }

            // BlkioWeight (int) minimum
            if(this.BlkioWeight < (int)0)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for BlkioWeight, must be a value greater than or equal to 0.", new [] { "BlkioWeight" });
            }


            
            // MemorySwappiness (long?) maximum
            if(this.MemorySwappiness > (long?)100)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for MemorySwappiness, must be a value less than or equal to 100.", new [] { "MemorySwappiness" });
            }

            // MemorySwappiness (long?) minimum
            if(this.MemorySwappiness < (long?)0)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for MemorySwappiness, must be a value greater than or equal to 0.", new [] { "MemorySwappiness" });
            }

            yield break;
        }
    }

}
