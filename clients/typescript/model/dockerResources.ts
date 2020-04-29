/**
 * Torizon Deployment API
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { DockerDeviceMapping } from './dockerDeviceMapping';
import { DockerResourcesBlkioWeightDevice } from './dockerResourcesBlkioWeightDevice';
import { DockerResourcesUlimits } from './dockerResourcesUlimits';
import { DockerThrottleDevice } from './dockerThrottleDevice';

/**
* A container\'s resources (cgroups config, ulimits, etc)
*/
export class DockerResources {
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
    'memorySwappiness'?: number;
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
    'init'?: boolean;
    /**
    * Tune a container\'s pids limit. Set -1 for unlimited.
    */
    'pidsLimit'?: number;
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
        }    ];

    static getAttributeTypeMap() {
        return DockerResources.attributeTypeMap;
    }
}

