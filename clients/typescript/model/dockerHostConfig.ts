/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { DockerDeviceMapping } from './dockerDeviceMapping';
import { DockerHostConfigAllOf } from './dockerHostConfigAllOf';
import { DockerHostConfigAllOfLogConfig } from './dockerHostConfigAllOfLogConfig';
import { DockerMount } from './dockerMount';
import { DockerPortBinding } from './dockerPortBinding';
import { DockerResources } from './dockerResources';
import { DockerResourcesBlkioWeightDevice } from './dockerResourcesBlkioWeightDevice';
import { DockerResourcesUlimits } from './dockerResourcesUlimits';
import { DockerRestartPolicy } from './dockerRestartPolicy';
import { DockerThrottleDevice } from './dockerThrottleDevice';

/**
* Container configuration that depends on the host we are running on
*/
export class DockerHostConfig {
    /**
    * An integer value representing this container\'s relative CPU weight versus other containers.
    */
    'cpuShares'?: number;
    /**
    * Memory limit in bytes.
    */
    'memory'?: number;
    /**
    * Path to `cgroups` under which the container\'s `cgroup` is created. If the path is not absolute, the path is considered to be relative to the `cgroups` path of the init process. Cgroups are created if they do not already exist.
    */
    'cgroupParent'?: string;
    /**
    * Block IO weight (relative weight).
    */
    'blkioWeight'?: number;
    /**
    * Block IO weight (relative device weight) in the form `[{\"Path\": \"device_path\", \"Weight\": weight}]`. 
    */
    'blkioWeightDevice'?: Array<DockerResourcesBlkioWeightDevice>;
    /**
    * Limit read rate (bytes per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`. 
    */
    'blkioDeviceReadBps'?: Array<DockerThrottleDevice>;
    /**
    * Limit write rate (bytes per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`. 
    */
    'blkioDeviceWriteBps'?: Array<DockerThrottleDevice>;
    /**
    * Limit read rate (IO per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`. 
    */
    'blkioDeviceReadIOps'?: Array<DockerThrottleDevice>;
    /**
    * Limit write rate (IO per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`. 
    */
    'blkioDeviceWriteIOps'?: Array<DockerThrottleDevice>;
    /**
    * The length of a CPU period in microseconds.
    */
    'cpuPeriod'?: number;
    /**
    * Microseconds of CPU time that the container can get in a CPU period.
    */
    'cpuQuota'?: number;
    /**
    * The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks.
    */
    'cpuRealtimePeriod'?: number;
    /**
    * The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks.
    */
    'cpuRealtimeRuntime'?: number;
    /**
    * CPUs in which to allow execution (e.g., `0-3`, `0,1`)
    */
    'cpusetCpus'?: string;
    /**
    * Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.
    */
    'cpusetMems'?: string;
    /**
    * A list of devices to add to the container.
    */
    'devices'?: Array<DockerDeviceMapping>;
    /**
    * a list of cgroup rules to apply to the container
    */
    'deviceCgroupRules'?: Array<string>;
    /**
    * Disk limit (in bytes).
    */
    'diskQuota'?: number;
    /**
    * Kernel memory limit in bytes.
    */
    'kernelMemory'?: number;
    /**
    * Memory soft limit in bytes.
    */
    'memoryReservation'?: number;
    /**
    * Total memory limit (memory + swap). Set as `-1` to enable unlimited swap.
    */
    'memorySwap'?: number;
    /**
    * Tune a container\'s memory swappiness behavior. Accepts an integer between 0 and 100.
    */
    'memorySwappiness'?: number | null;
    /**
    * CPU quota in units of 10<sup>-9</sup> CPUs.
    */
    'nanoCPUs'?: number;
    /**
    * Disable OOM Killer for the container.
    */
    'oomKillDisable'?: boolean;
    /**
    * Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used.
    */
    'init'?: boolean | null;
    /**
    * Tune a container\'s pids limit. Set -1 for unlimited.
    */
    'pidsLimit'?: number | null;
    /**
    * A list of resource limits to set in the container. For example: `{\"Name\": \"nofile\", \"Soft\": 1024, \"Hard\": 2048}`\" 
    */
    'ulimits'?: Array<DockerResourcesUlimits>;
    /**
    * The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last. 
    */
    'cpuCount'?: number;
    /**
    * The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last. 
    */
    'cpuPercent'?: number;
    /**
    * Maximum IOps for the container system drive (Windows only)
    */
    'iOMaximumIOps'?: number;
    /**
    * Maximum IO in bytes per second for the container system drive (Windows only)
    */
    'iOMaximumBandwidth'?: number;
    /**
    * A list of volume bindings for this container. Each volume binding is a string in one of these forms:  - `host-src:container-dest` to bind-mount a host path into the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `host-src:container-dest:ro` to make the bind mount read-only inside the container. Both `host-src`, and `container-dest` must be an _absolute_ path. - `volume-name:container-dest` to bind-mount a volume managed by a volume driver into the container. `container-dest` must be an _absolute_ path. - `volume-name:container-dest:ro` to mount the volume read-only inside the container.  `container-dest` must be an _absolute_ path. 
    */
    'binds'?: Array<string>;
    /**
    * Path to a file where the container ID is written
    */
    'containerIDFile'?: string;
    'logConfig'?: DockerHostConfigAllOfLogConfig;
    /**
    * Network mode to use for this container. Supported standard values are: `bridge`, `host`, `none`, and `container:<name|id>`. Any other value is taken as a custom network\'s name to which this container should connect to.
    */
    'networkMode'?: string;
    /**
    * PortMap describes the mapping of container ports to host ports, using the container\'s port-number and protocol as key in the format `<port>/<protocol>`, for example, `80/udp`.  If a container\'s port is mapped for multiple protocols, separate entries are added to the mapping table. 
    */
    'portBindings'?: { [key: string]: Array<DockerPortBinding>; };
    'restartPolicy'?: DockerRestartPolicy;
    /**
    * Automatically remove the container when the container\'s process exits. This has no effect if `RestartPolicy` is set.
    */
    'autoRemove'?: boolean;
    /**
    * Driver that this container uses to mount volumes.
    */
    'volumeDriver'?: string;
    /**
    * A list of volumes to inherit from another container, specified in the form `<container name>[:<ro|rw>]`.
    */
    'volumesFrom'?: Array<string>;
    /**
    * Specification for mounts to be added to the container.
    */
    'mounts'?: Array<DockerMount>;
    /**
    * A list of kernel capabilities to add to the container.
    */
    'capAdd'?: Array<string>;
    /**
    * A list of kernel capabilities to drop from the container.
    */
    'capDrop'?: Array<string>;
    /**
    * A list of DNS servers for the container to use.
    */
    'dns'?: Array<string>;
    /**
    * A list of DNS options.
    */
    'dnsOptions'?: Array<string>;
    /**
    * A list of DNS search domains.
    */
    'dnsSearch'?: Array<string>;
    /**
    * A list of hostnames/IP mappings to add to the container\'s `/etc/hosts` file. Specified in the form `[\"hostname:IP\"]`. 
    */
    'extraHosts'?: Array<string>;
    /**
    * A list of additional groups that the container process will run as.
    */
    'groupAdd'?: Array<string>;
    /**
    * IPC sharing mode for the container. Possible values are:  - `\"none\"`: own private IPC namespace, with /dev/shm not mounted - `\"private\"`: own private IPC namespace - `\"shareable\"`: own private IPC namespace, with a possibility to share it with other containers - `\"container:<name|id>\"`: join another (shareable) container\'s IPC namespace - `\"host\"`: use the host system\'s IPC namespace  If not specified, daemon default is used, which can either be `\"private\"` or `\"shareable\"`, depending on daemon version and configuration. 
    */
    'ipcMode'?: string;
    /**
    * Cgroup to use for the container.
    */
    'cgroup'?: string;
    /**
    * A list of links for the container in the form `container_name:alias`.
    */
    'links'?: Array<string>;
    /**
    * An integer value containing the score given to the container in order to tune OOM killer preferences.
    */
    'oomScoreAdj'?: number;
    /**
    * Set the PID (Process) Namespace mode for the container. It can be either:  - `\"container:<name|id>\"`: joins another container\'s PID namespace - `\"host\"`: use the host\'s PID namespace inside the container 
    */
    'pidMode'?: string;
    /**
    * Gives the container full access to the host.
    */
    'privileged'?: boolean;
    /**
    * Allocates an ephemeral host port for all of a container\'s exposed ports.  Ports are de-allocated when the container stops and allocated when the container starts. The allocated port might be changed when restarting the container.  The port is selected from the ephemeral port range that depends on the kernel. For example, on Linux the range is defined by `/proc/sys/net/ipv4/ip_local_port_range`. 
    */
    'publishAllPorts'?: boolean;
    /**
    * Mount the container\'s root filesystem as read only.
    */
    'readonlyRootfs'?: boolean;
    /**
    * A list of string values to customize labels for MLS systems, such as SELinux.
    */
    'securityOpt'?: Array<string>;
    /**
    * Storage driver options for this container, in the form `{\"size\": \"120G\"}`. 
    */
    'storageOpt'?: { [key: string]: string; };
    /**
    * A map of container directories which should be replaced by tmpfs mounts, and their corresponding mount options. For example: `{ \"/run\": \"rw,noexec,nosuid,size=65536k\" }`. 
    */
    'tmpfs'?: { [key: string]: string; };
    /**
    * UTS namespace to use for the container.
    */
    'uTSMode'?: string;
    /**
    * Sets the usernamespace mode for the container when usernamespace remapping option is enabled.
    */
    'usernsMode'?: string;
    /**
    * Size of `/dev/shm` in bytes. If omitted, the system uses 64MB.
    */
    'shmSize'?: number;
    /**
    * A list of kernel parameters (sysctls) to set in the container. For example: `{\"net.ipv4.ip_forward\": \"1\"}` 
    */
    'sysctls'?: { [key: string]: string; };
    /**
    * Runtime to use with this container.
    */
    'runtime'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "cpuShares",
            "baseName": "CpuShares",
            "type": "number"
        },
        {
            "name": "memory",
            "baseName": "Memory",
            "type": "number"
        },
        {
            "name": "cgroupParent",
            "baseName": "CgroupParent",
            "type": "string"
        },
        {
            "name": "blkioWeight",
            "baseName": "BlkioWeight",
            "type": "number"
        },
        {
            "name": "blkioWeightDevice",
            "baseName": "BlkioWeightDevice",
            "type": "Array<DockerResourcesBlkioWeightDevice>"
        },
        {
            "name": "blkioDeviceReadBps",
            "baseName": "BlkioDeviceReadBps",
            "type": "Array<DockerThrottleDevice>"
        },
        {
            "name": "blkioDeviceWriteBps",
            "baseName": "BlkioDeviceWriteBps",
            "type": "Array<DockerThrottleDevice>"
        },
        {
            "name": "blkioDeviceReadIOps",
            "baseName": "BlkioDeviceReadIOps",
            "type": "Array<DockerThrottleDevice>"
        },
        {
            "name": "blkioDeviceWriteIOps",
            "baseName": "BlkioDeviceWriteIOps",
            "type": "Array<DockerThrottleDevice>"
        },
        {
            "name": "cpuPeriod",
            "baseName": "CpuPeriod",
            "type": "number"
        },
        {
            "name": "cpuQuota",
            "baseName": "CpuQuota",
            "type": "number"
        },
        {
            "name": "cpuRealtimePeriod",
            "baseName": "CpuRealtimePeriod",
            "type": "number"
        },
        {
            "name": "cpuRealtimeRuntime",
            "baseName": "CpuRealtimeRuntime",
            "type": "number"
        },
        {
            "name": "cpusetCpus",
            "baseName": "CpusetCpus",
            "type": "string"
        },
        {
            "name": "cpusetMems",
            "baseName": "CpusetMems",
            "type": "string"
        },
        {
            "name": "devices",
            "baseName": "Devices",
            "type": "Array<DockerDeviceMapping>"
        },
        {
            "name": "deviceCgroupRules",
            "baseName": "DeviceCgroupRules",
            "type": "Array<string>"
        },
        {
            "name": "diskQuota",
            "baseName": "DiskQuota",
            "type": "number"
        },
        {
            "name": "kernelMemory",
            "baseName": "KernelMemory",
            "type": "number"
        },
        {
            "name": "memoryReservation",
            "baseName": "MemoryReservation",
            "type": "number"
        },
        {
            "name": "memorySwap",
            "baseName": "MemorySwap",
            "type": "number"
        },
        {
            "name": "memorySwappiness",
            "baseName": "MemorySwappiness",
            "type": "number"
        },
        {
            "name": "nanoCPUs",
            "baseName": "NanoCPUs",
            "type": "number"
        },
        {
            "name": "oomKillDisable",
            "baseName": "OomKillDisable",
            "type": "boolean"
        },
        {
            "name": "init",
            "baseName": "Init",
            "type": "boolean"
        },
        {
            "name": "pidsLimit",
            "baseName": "PidsLimit",
            "type": "number"
        },
        {
            "name": "ulimits",
            "baseName": "Ulimits",
            "type": "Array<DockerResourcesUlimits>"
        },
        {
            "name": "cpuCount",
            "baseName": "CpuCount",
            "type": "number"
        },
        {
            "name": "cpuPercent",
            "baseName": "CpuPercent",
            "type": "number"
        },
        {
            "name": "iOMaximumIOps",
            "baseName": "IOMaximumIOps",
            "type": "number"
        },
        {
            "name": "iOMaximumBandwidth",
            "baseName": "IOMaximumBandwidth",
            "type": "number"
        },
        {
            "name": "binds",
            "baseName": "Binds",
            "type": "Array<string>"
        },
        {
            "name": "containerIDFile",
            "baseName": "ContainerIDFile",
            "type": "string"
        },
        {
            "name": "logConfig",
            "baseName": "LogConfig",
            "type": "DockerHostConfigAllOfLogConfig"
        },
        {
            "name": "networkMode",
            "baseName": "NetworkMode",
            "type": "string"
        },
        {
            "name": "portBindings",
            "baseName": "PortBindings",
            "type": "{ [key: string]: Array<DockerPortBinding>; }"
        },
        {
            "name": "restartPolicy",
            "baseName": "RestartPolicy",
            "type": "DockerRestartPolicy"
        },
        {
            "name": "autoRemove",
            "baseName": "AutoRemove",
            "type": "boolean"
        },
        {
            "name": "volumeDriver",
            "baseName": "VolumeDriver",
            "type": "string"
        },
        {
            "name": "volumesFrom",
            "baseName": "VolumesFrom",
            "type": "Array<string>"
        },
        {
            "name": "mounts",
            "baseName": "Mounts",
            "type": "Array<DockerMount>"
        },
        {
            "name": "capAdd",
            "baseName": "CapAdd",
            "type": "Array<string>"
        },
        {
            "name": "capDrop",
            "baseName": "CapDrop",
            "type": "Array<string>"
        },
        {
            "name": "dns",
            "baseName": "Dns",
            "type": "Array<string>"
        },
        {
            "name": "dnsOptions",
            "baseName": "DnsOptions",
            "type": "Array<string>"
        },
        {
            "name": "dnsSearch",
            "baseName": "DnsSearch",
            "type": "Array<string>"
        },
        {
            "name": "extraHosts",
            "baseName": "ExtraHosts",
            "type": "Array<string>"
        },
        {
            "name": "groupAdd",
            "baseName": "GroupAdd",
            "type": "Array<string>"
        },
        {
            "name": "ipcMode",
            "baseName": "IpcMode",
            "type": "string"
        },
        {
            "name": "cgroup",
            "baseName": "Cgroup",
            "type": "string"
        },
        {
            "name": "links",
            "baseName": "Links",
            "type": "Array<string>"
        },
        {
            "name": "oomScoreAdj",
            "baseName": "OomScoreAdj",
            "type": "number"
        },
        {
            "name": "pidMode",
            "baseName": "PidMode",
            "type": "string"
        },
        {
            "name": "privileged",
            "baseName": "Privileged",
            "type": "boolean"
        },
        {
            "name": "publishAllPorts",
            "baseName": "PublishAllPorts",
            "type": "boolean"
        },
        {
            "name": "readonlyRootfs",
            "baseName": "ReadonlyRootfs",
            "type": "boolean"
        },
        {
            "name": "securityOpt",
            "baseName": "SecurityOpt",
            "type": "Array<string>"
        },
        {
            "name": "storageOpt",
            "baseName": "StorageOpt",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "tmpfs",
            "baseName": "Tmpfs",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "uTSMode",
            "baseName": "UTSMode",
            "type": "string"
        },
        {
            "name": "usernsMode",
            "baseName": "UsernsMode",
            "type": "string"
        },
        {
            "name": "shmSize",
            "baseName": "ShmSize",
            "type": "number"
        },
        {
            "name": "sysctls",
            "baseName": "Sysctls",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "runtime",
            "baseName": "Runtime",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DockerHostConfig.attributeTypeMap;
    }
}

