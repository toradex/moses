# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerResources(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cpu_shares': 'int',
        'memory': 'int',
        'cgroup_parent': 'str',
        'blkio_weight': 'int',
        'blkio_weight_device': 'list[DockerResourcesBlkioWeightDevice]',
        'blkio_device_read_bps': 'list[DockerThrottleDevice]',
        'blkio_device_write_bps': 'list[DockerThrottleDevice]',
        'blkio_device_read_i_ops': 'list[DockerThrottleDevice]',
        'blkio_device_write_i_ops': 'list[DockerThrottleDevice]',
        'cpu_period': 'int',
        'cpu_quota': 'int',
        'cpu_realtime_period': 'int',
        'cpu_realtime_runtime': 'int',
        'cpuset_cpus': 'str',
        'cpuset_mems': 'str',
        'devices': 'list[DockerDeviceMapping]',
        'device_cgroup_rules': 'list[str]',
        'disk_quota': 'int',
        'kernel_memory': 'int',
        'memory_reservation': 'int',
        'memory_swap': 'int',
        'memory_swappiness': 'int',
        'nano_cp_us': 'int',
        'oom_kill_disable': 'bool',
        'init': 'bool',
        'pids_limit': 'int',
        'ulimits': 'list[DockerResourcesUlimits]',
        'cpu_count': 'int',
        'cpu_percent': 'int',
        'io_maximum_i_ops': 'int',
        'io_maximum_bandwidth': 'int'
    }

    attribute_map = {
        'cpu_shares': 'CpuShares',
        'memory': 'Memory',
        'cgroup_parent': 'CgroupParent',
        'blkio_weight': 'BlkioWeight',
        'blkio_weight_device': 'BlkioWeightDevice',
        'blkio_device_read_bps': 'BlkioDeviceReadBps',
        'blkio_device_write_bps': 'BlkioDeviceWriteBps',
        'blkio_device_read_i_ops': 'BlkioDeviceReadIOps',
        'blkio_device_write_i_ops': 'BlkioDeviceWriteIOps',
        'cpu_period': 'CpuPeriod',
        'cpu_quota': 'CpuQuota',
        'cpu_realtime_period': 'CpuRealtimePeriod',
        'cpu_realtime_runtime': 'CpuRealtimeRuntime',
        'cpuset_cpus': 'CpusetCpus',
        'cpuset_mems': 'CpusetMems',
        'devices': 'Devices',
        'device_cgroup_rules': 'DeviceCgroupRules',
        'disk_quota': 'DiskQuota',
        'kernel_memory': 'KernelMemory',
        'memory_reservation': 'MemoryReservation',
        'memory_swap': 'MemorySwap',
        'memory_swappiness': 'MemorySwappiness',
        'nano_cp_us': 'NanoCPUs',
        'oom_kill_disable': 'OomKillDisable',
        'init': 'Init',
        'pids_limit': 'PidsLimit',
        'ulimits': 'Ulimits',
        'cpu_count': 'CpuCount',
        'cpu_percent': 'CpuPercent',
        'io_maximum_i_ops': 'IOMaximumIOps',
        'io_maximum_bandwidth': 'IOMaximumBandwidth'
    }

    def __init__(self, cpu_shares=None, memory=0, cgroup_parent=None, blkio_weight=None, blkio_weight_device=None, blkio_device_read_bps=None, blkio_device_write_bps=None, blkio_device_read_i_ops=None, blkio_device_write_i_ops=None, cpu_period=None, cpu_quota=None, cpu_realtime_period=None, cpu_realtime_runtime=None, cpuset_cpus=None, cpuset_mems=None, devices=None, device_cgroup_rules=None, disk_quota=None, kernel_memory=None, memory_reservation=None, memory_swap=None, memory_swappiness=None, nano_cp_us=None, oom_kill_disable=None, init=None, pids_limit=None, ulimits=None, cpu_count=None, cpu_percent=None, io_maximum_i_ops=None, io_maximum_bandwidth=None, local_vars_configuration=None):  # noqa: E501
        """DockerResources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_shares = None
        self._memory = None
        self._cgroup_parent = None
        self._blkio_weight = None
        self._blkio_weight_device = None
        self._blkio_device_read_bps = None
        self._blkio_device_write_bps = None
        self._blkio_device_read_i_ops = None
        self._blkio_device_write_i_ops = None
        self._cpu_period = None
        self._cpu_quota = None
        self._cpu_realtime_period = None
        self._cpu_realtime_runtime = None
        self._cpuset_cpus = None
        self._cpuset_mems = None
        self._devices = None
        self._device_cgroup_rules = None
        self._disk_quota = None
        self._kernel_memory = None
        self._memory_reservation = None
        self._memory_swap = None
        self._memory_swappiness = None
        self._nano_cp_us = None
        self._oom_kill_disable = None
        self._init = None
        self._pids_limit = None
        self._ulimits = None
        self._cpu_count = None
        self._cpu_percent = None
        self._io_maximum_i_ops = None
        self._io_maximum_bandwidth = None
        self.discriminator = None

        if cpu_shares is not None:
            self.cpu_shares = cpu_shares
        if memory is not None:
            self.memory = memory
        if cgroup_parent is not None:
            self.cgroup_parent = cgroup_parent
        if blkio_weight is not None:
            self.blkio_weight = blkio_weight
        if blkio_weight_device is not None:
            self.blkio_weight_device = blkio_weight_device
        if blkio_device_read_bps is not None:
            self.blkio_device_read_bps = blkio_device_read_bps
        if blkio_device_write_bps is not None:
            self.blkio_device_write_bps = blkio_device_write_bps
        if blkio_device_read_i_ops is not None:
            self.blkio_device_read_i_ops = blkio_device_read_i_ops
        if blkio_device_write_i_ops is not None:
            self.blkio_device_write_i_ops = blkio_device_write_i_ops
        if cpu_period is not None:
            self.cpu_period = cpu_period
        if cpu_quota is not None:
            self.cpu_quota = cpu_quota
        if cpu_realtime_period is not None:
            self.cpu_realtime_period = cpu_realtime_period
        if cpu_realtime_runtime is not None:
            self.cpu_realtime_runtime = cpu_realtime_runtime
        if cpuset_cpus is not None:
            self.cpuset_cpus = cpuset_cpus
        if cpuset_mems is not None:
            self.cpuset_mems = cpuset_mems
        if devices is not None:
            self.devices = devices
        if device_cgroup_rules is not None:
            self.device_cgroup_rules = device_cgroup_rules
        if disk_quota is not None:
            self.disk_quota = disk_quota
        if kernel_memory is not None:
            self.kernel_memory = kernel_memory
        if memory_reservation is not None:
            self.memory_reservation = memory_reservation
        if memory_swap is not None:
            self.memory_swap = memory_swap
        self.memory_swappiness = memory_swappiness
        if nano_cp_us is not None:
            self.nano_cp_us = nano_cp_us
        if oom_kill_disable is not None:
            self.oom_kill_disable = oom_kill_disable
        self.init = init
        self.pids_limit = pids_limit
        if ulimits is not None:
            self.ulimits = ulimits
        if cpu_count is not None:
            self.cpu_count = cpu_count
        if cpu_percent is not None:
            self.cpu_percent = cpu_percent
        if io_maximum_i_ops is not None:
            self.io_maximum_i_ops = io_maximum_i_ops
        if io_maximum_bandwidth is not None:
            self.io_maximum_bandwidth = io_maximum_bandwidth

    @property
    def cpu_shares(self):
        """Gets the cpu_shares of this DockerResources.  # noqa: E501

        An integer value representing this container's relative CPU weight versus other containers.  # noqa: E501

        :return: The cpu_shares of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_shares

    @cpu_shares.setter
    def cpu_shares(self, cpu_shares):
        """Sets the cpu_shares of this DockerResources.

        An integer value representing this container's relative CPU weight versus other containers.  # noqa: E501

        :param cpu_shares: The cpu_shares of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_shares = cpu_shares

    @property
    def memory(self):
        """Gets the memory of this DockerResources.  # noqa: E501

        Memory limit in bytes.  # noqa: E501

        :return: The memory of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this DockerResources.

        Memory limit in bytes.  # noqa: E501

        :param memory: The memory of this DockerResources.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def cgroup_parent(self):
        """Gets the cgroup_parent of this DockerResources.  # noqa: E501

        Path to `cgroups` under which the container's `cgroup` is created. If the path is not absolute, the path is considered to be relative to the `cgroups` path of the init process. Cgroups are created if they do not already exist.  # noqa: E501

        :return: The cgroup_parent of this DockerResources.  # noqa: E501
        :rtype: str
        """
        return self._cgroup_parent

    @cgroup_parent.setter
    def cgroup_parent(self, cgroup_parent):
        """Sets the cgroup_parent of this DockerResources.

        Path to `cgroups` under which the container's `cgroup` is created. If the path is not absolute, the path is considered to be relative to the `cgroups` path of the init process. Cgroups are created if they do not already exist.  # noqa: E501

        :param cgroup_parent: The cgroup_parent of this DockerResources.  # noqa: E501
        :type: str
        """

        self._cgroup_parent = cgroup_parent

    @property
    def blkio_weight(self):
        """Gets the blkio_weight of this DockerResources.  # noqa: E501

        Block IO weight (relative weight).  # noqa: E501

        :return: The blkio_weight of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._blkio_weight

    @blkio_weight.setter
    def blkio_weight(self, blkio_weight):
        """Sets the blkio_weight of this DockerResources.

        Block IO weight (relative weight).  # noqa: E501

        :param blkio_weight: The blkio_weight of this DockerResources.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                blkio_weight is not None and blkio_weight > 1000):  # noqa: E501
            raise ValueError("Invalid value for `blkio_weight`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                blkio_weight is not None and blkio_weight < 0):  # noqa: E501
            raise ValueError("Invalid value for `blkio_weight`, must be a value greater than or equal to `0`")  # noqa: E501

        self._blkio_weight = blkio_weight

    @property
    def blkio_weight_device(self):
        """Gets the blkio_weight_device of this DockerResources.  # noqa: E501

        Block IO weight (relative device weight) in the form `[{\"Path\": \"device_path\", \"Weight\": weight}]`.   # noqa: E501

        :return: The blkio_weight_device of this DockerResources.  # noqa: E501
        :rtype: list[DockerResourcesBlkioWeightDevice]
        """
        return self._blkio_weight_device

    @blkio_weight_device.setter
    def blkio_weight_device(self, blkio_weight_device):
        """Sets the blkio_weight_device of this DockerResources.

        Block IO weight (relative device weight) in the form `[{\"Path\": \"device_path\", \"Weight\": weight}]`.   # noqa: E501

        :param blkio_weight_device: The blkio_weight_device of this DockerResources.  # noqa: E501
        :type: list[DockerResourcesBlkioWeightDevice]
        """

        self._blkio_weight_device = blkio_weight_device

    @property
    def blkio_device_read_bps(self):
        """Gets the blkio_device_read_bps of this DockerResources.  # noqa: E501

        Limit read rate (bytes per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :return: The blkio_device_read_bps of this DockerResources.  # noqa: E501
        :rtype: list[DockerThrottleDevice]
        """
        return self._blkio_device_read_bps

    @blkio_device_read_bps.setter
    def blkio_device_read_bps(self, blkio_device_read_bps):
        """Sets the blkio_device_read_bps of this DockerResources.

        Limit read rate (bytes per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :param blkio_device_read_bps: The blkio_device_read_bps of this DockerResources.  # noqa: E501
        :type: list[DockerThrottleDevice]
        """

        self._blkio_device_read_bps = blkio_device_read_bps

    @property
    def blkio_device_write_bps(self):
        """Gets the blkio_device_write_bps of this DockerResources.  # noqa: E501

        Limit write rate (bytes per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :return: The blkio_device_write_bps of this DockerResources.  # noqa: E501
        :rtype: list[DockerThrottleDevice]
        """
        return self._blkio_device_write_bps

    @blkio_device_write_bps.setter
    def blkio_device_write_bps(self, blkio_device_write_bps):
        """Sets the blkio_device_write_bps of this DockerResources.

        Limit write rate (bytes per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :param blkio_device_write_bps: The blkio_device_write_bps of this DockerResources.  # noqa: E501
        :type: list[DockerThrottleDevice]
        """

        self._blkio_device_write_bps = blkio_device_write_bps

    @property
    def blkio_device_read_i_ops(self):
        """Gets the blkio_device_read_i_ops of this DockerResources.  # noqa: E501

        Limit read rate (IO per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :return: The blkio_device_read_i_ops of this DockerResources.  # noqa: E501
        :rtype: list[DockerThrottleDevice]
        """
        return self._blkio_device_read_i_ops

    @blkio_device_read_i_ops.setter
    def blkio_device_read_i_ops(self, blkio_device_read_i_ops):
        """Sets the blkio_device_read_i_ops of this DockerResources.

        Limit read rate (IO per second) from a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :param blkio_device_read_i_ops: The blkio_device_read_i_ops of this DockerResources.  # noqa: E501
        :type: list[DockerThrottleDevice]
        """

        self._blkio_device_read_i_ops = blkio_device_read_i_ops

    @property
    def blkio_device_write_i_ops(self):
        """Gets the blkio_device_write_i_ops of this DockerResources.  # noqa: E501

        Limit write rate (IO per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :return: The blkio_device_write_i_ops of this DockerResources.  # noqa: E501
        :rtype: list[DockerThrottleDevice]
        """
        return self._blkio_device_write_i_ops

    @blkio_device_write_i_ops.setter
    def blkio_device_write_i_ops(self, blkio_device_write_i_ops):
        """Sets the blkio_device_write_i_ops of this DockerResources.

        Limit write rate (IO per second) to a device, in the form `[{\"Path\": \"device_path\", \"Rate\": rate}]`.   # noqa: E501

        :param blkio_device_write_i_ops: The blkio_device_write_i_ops of this DockerResources.  # noqa: E501
        :type: list[DockerThrottleDevice]
        """

        self._blkio_device_write_i_ops = blkio_device_write_i_ops

    @property
    def cpu_period(self):
        """Gets the cpu_period of this DockerResources.  # noqa: E501

        The length of a CPU period in microseconds.  # noqa: E501

        :return: The cpu_period of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_period

    @cpu_period.setter
    def cpu_period(self, cpu_period):
        """Sets the cpu_period of this DockerResources.

        The length of a CPU period in microseconds.  # noqa: E501

        :param cpu_period: The cpu_period of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_period = cpu_period

    @property
    def cpu_quota(self):
        """Gets the cpu_quota of this DockerResources.  # noqa: E501

        Microseconds of CPU time that the container can get in a CPU period.  # noqa: E501

        :return: The cpu_quota of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_quota

    @cpu_quota.setter
    def cpu_quota(self, cpu_quota):
        """Sets the cpu_quota of this DockerResources.

        Microseconds of CPU time that the container can get in a CPU period.  # noqa: E501

        :param cpu_quota: The cpu_quota of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_quota = cpu_quota

    @property
    def cpu_realtime_period(self):
        """Gets the cpu_realtime_period of this DockerResources.  # noqa: E501

        The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks.  # noqa: E501

        :return: The cpu_realtime_period of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_realtime_period

    @cpu_realtime_period.setter
    def cpu_realtime_period(self, cpu_realtime_period):
        """Sets the cpu_realtime_period of this DockerResources.

        The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks.  # noqa: E501

        :param cpu_realtime_period: The cpu_realtime_period of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_realtime_period = cpu_realtime_period

    @property
    def cpu_realtime_runtime(self):
        """Gets the cpu_realtime_runtime of this DockerResources.  # noqa: E501

        The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks.  # noqa: E501

        :return: The cpu_realtime_runtime of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_realtime_runtime

    @cpu_realtime_runtime.setter
    def cpu_realtime_runtime(self, cpu_realtime_runtime):
        """Sets the cpu_realtime_runtime of this DockerResources.

        The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks.  # noqa: E501

        :param cpu_realtime_runtime: The cpu_realtime_runtime of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_realtime_runtime = cpu_realtime_runtime

    @property
    def cpuset_cpus(self):
        """Gets the cpuset_cpus of this DockerResources.  # noqa: E501

        CPUs in which to allow execution (e.g., `0-3`, `0,1`)  # noqa: E501

        :return: The cpuset_cpus of this DockerResources.  # noqa: E501
        :rtype: str
        """
        return self._cpuset_cpus

    @cpuset_cpus.setter
    def cpuset_cpus(self, cpuset_cpus):
        """Sets the cpuset_cpus of this DockerResources.

        CPUs in which to allow execution (e.g., `0-3`, `0,1`)  # noqa: E501

        :param cpuset_cpus: The cpuset_cpus of this DockerResources.  # noqa: E501
        :type: str
        """

        self._cpuset_cpus = cpuset_cpus

    @property
    def cpuset_mems(self):
        """Gets the cpuset_mems of this DockerResources.  # noqa: E501

        Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.  # noqa: E501

        :return: The cpuset_mems of this DockerResources.  # noqa: E501
        :rtype: str
        """
        return self._cpuset_mems

    @cpuset_mems.setter
    def cpuset_mems(self, cpuset_mems):
        """Sets the cpuset_mems of this DockerResources.

        Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.  # noqa: E501

        :param cpuset_mems: The cpuset_mems of this DockerResources.  # noqa: E501
        :type: str
        """

        self._cpuset_mems = cpuset_mems

    @property
    def devices(self):
        """Gets the devices of this DockerResources.  # noqa: E501

        A list of devices to add to the container.  # noqa: E501

        :return: The devices of this DockerResources.  # noqa: E501
        :rtype: list[DockerDeviceMapping]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DockerResources.

        A list of devices to add to the container.  # noqa: E501

        :param devices: The devices of this DockerResources.  # noqa: E501
        :type: list[DockerDeviceMapping]
        """

        self._devices = devices

    @property
    def device_cgroup_rules(self):
        """Gets the device_cgroup_rules of this DockerResources.  # noqa: E501

        a list of cgroup rules to apply to the container  # noqa: E501

        :return: The device_cgroup_rules of this DockerResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_cgroup_rules

    @device_cgroup_rules.setter
    def device_cgroup_rules(self, device_cgroup_rules):
        """Sets the device_cgroup_rules of this DockerResources.

        a list of cgroup rules to apply to the container  # noqa: E501

        :param device_cgroup_rules: The device_cgroup_rules of this DockerResources.  # noqa: E501
        :type: list[str]
        """

        self._device_cgroup_rules = device_cgroup_rules

    @property
    def disk_quota(self):
        """Gets the disk_quota of this DockerResources.  # noqa: E501

        Disk limit (in bytes).  # noqa: E501

        :return: The disk_quota of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._disk_quota

    @disk_quota.setter
    def disk_quota(self, disk_quota):
        """Sets the disk_quota of this DockerResources.

        Disk limit (in bytes).  # noqa: E501

        :param disk_quota: The disk_quota of this DockerResources.  # noqa: E501
        :type: int
        """

        self._disk_quota = disk_quota

    @property
    def kernel_memory(self):
        """Gets the kernel_memory of this DockerResources.  # noqa: E501

        Kernel memory limit in bytes.  # noqa: E501

        :return: The kernel_memory of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._kernel_memory

    @kernel_memory.setter
    def kernel_memory(self, kernel_memory):
        """Sets the kernel_memory of this DockerResources.

        Kernel memory limit in bytes.  # noqa: E501

        :param kernel_memory: The kernel_memory of this DockerResources.  # noqa: E501
        :type: int
        """

        self._kernel_memory = kernel_memory

    @property
    def memory_reservation(self):
        """Gets the memory_reservation of this DockerResources.  # noqa: E501

        Memory soft limit in bytes.  # noqa: E501

        :return: The memory_reservation of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._memory_reservation

    @memory_reservation.setter
    def memory_reservation(self, memory_reservation):
        """Sets the memory_reservation of this DockerResources.

        Memory soft limit in bytes.  # noqa: E501

        :param memory_reservation: The memory_reservation of this DockerResources.  # noqa: E501
        :type: int
        """

        self._memory_reservation = memory_reservation

    @property
    def memory_swap(self):
        """Gets the memory_swap of this DockerResources.  # noqa: E501

        Total memory limit (memory + swap). Set as `-1` to enable unlimited swap.  # noqa: E501

        :return: The memory_swap of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._memory_swap

    @memory_swap.setter
    def memory_swap(self, memory_swap):
        """Sets the memory_swap of this DockerResources.

        Total memory limit (memory + swap). Set as `-1` to enable unlimited swap.  # noqa: E501

        :param memory_swap: The memory_swap of this DockerResources.  # noqa: E501
        :type: int
        """

        self._memory_swap = memory_swap

    @property
    def memory_swappiness(self):
        """Gets the memory_swappiness of this DockerResources.  # noqa: E501

        Tune a container's memory swappiness behavior. Accepts an integer between 0 and 100.  # noqa: E501

        :return: The memory_swappiness of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._memory_swappiness

    @memory_swappiness.setter
    def memory_swappiness(self, memory_swappiness):
        """Sets the memory_swappiness of this DockerResources.

        Tune a container's memory swappiness behavior. Accepts an integer between 0 and 100.  # noqa: E501

        :param memory_swappiness: The memory_swappiness of this DockerResources.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_swappiness is not None and memory_swappiness > 100):  # noqa: E501
            raise ValueError("Invalid value for `memory_swappiness`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                memory_swappiness is not None and memory_swappiness < 0):  # noqa: E501
            raise ValueError("Invalid value for `memory_swappiness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._memory_swappiness = memory_swappiness

    @property
    def nano_cp_us(self):
        """Gets the nano_cp_us of this DockerResources.  # noqa: E501

        CPU quota in units of 10<sup>-9</sup> CPUs.  # noqa: E501

        :return: The nano_cp_us of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._nano_cp_us

    @nano_cp_us.setter
    def nano_cp_us(self, nano_cp_us):
        """Sets the nano_cp_us of this DockerResources.

        CPU quota in units of 10<sup>-9</sup> CPUs.  # noqa: E501

        :param nano_cp_us: The nano_cp_us of this DockerResources.  # noqa: E501
        :type: int
        """

        self._nano_cp_us = nano_cp_us

    @property
    def oom_kill_disable(self):
        """Gets the oom_kill_disable of this DockerResources.  # noqa: E501

        Disable OOM Killer for the container.  # noqa: E501

        :return: The oom_kill_disable of this DockerResources.  # noqa: E501
        :rtype: bool
        """
        return self._oom_kill_disable

    @oom_kill_disable.setter
    def oom_kill_disable(self, oom_kill_disable):
        """Sets the oom_kill_disable of this DockerResources.

        Disable OOM Killer for the container.  # noqa: E501

        :param oom_kill_disable: The oom_kill_disable of this DockerResources.  # noqa: E501
        :type: bool
        """

        self._oom_kill_disable = oom_kill_disable

    @property
    def init(self):
        """Gets the init of this DockerResources.  # noqa: E501

        Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used.  # noqa: E501

        :return: The init of this DockerResources.  # noqa: E501
        :rtype: bool
        """
        return self._init

    @init.setter
    def init(self, init):
        """Sets the init of this DockerResources.

        Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used.  # noqa: E501

        :param init: The init of this DockerResources.  # noqa: E501
        :type: bool
        """

        self._init = init

    @property
    def pids_limit(self):
        """Gets the pids_limit of this DockerResources.  # noqa: E501

        Tune a container's pids limit. Set -1 for unlimited.  # noqa: E501

        :return: The pids_limit of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._pids_limit

    @pids_limit.setter
    def pids_limit(self, pids_limit):
        """Sets the pids_limit of this DockerResources.

        Tune a container's pids limit. Set -1 for unlimited.  # noqa: E501

        :param pids_limit: The pids_limit of this DockerResources.  # noqa: E501
        :type: int
        """

        self._pids_limit = pids_limit

    @property
    def ulimits(self):
        """Gets the ulimits of this DockerResources.  # noqa: E501

        A list of resource limits to set in the container. For example: `{\"Name\": \"nofile\", \"Soft\": 1024, \"Hard\": 2048}`\"   # noqa: E501

        :return: The ulimits of this DockerResources.  # noqa: E501
        :rtype: list[DockerResourcesUlimits]
        """
        return self._ulimits

    @ulimits.setter
    def ulimits(self, ulimits):
        """Sets the ulimits of this DockerResources.

        A list of resource limits to set in the container. For example: `{\"Name\": \"nofile\", \"Soft\": 1024, \"Hard\": 2048}`\"   # noqa: E501

        :param ulimits: The ulimits of this DockerResources.  # noqa: E501
        :type: list[DockerResourcesUlimits]
        """

        self._ulimits = ulimits

    @property
    def cpu_count(self):
        """Gets the cpu_count of this DockerResources.  # noqa: E501

        The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last.   # noqa: E501

        :return: The cpu_count of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this DockerResources.

        The number of usable CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last.   # noqa: E501

        :param cpu_count: The cpu_count of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_count = cpu_count

    @property
    def cpu_percent(self):
        """Gets the cpu_percent of this DockerResources.  # noqa: E501

        The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last.   # noqa: E501

        :return: The cpu_percent of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        """Sets the cpu_percent of this DockerResources.

        The usable percentage of the available CPUs (Windows only).  On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last.   # noqa: E501

        :param cpu_percent: The cpu_percent of this DockerResources.  # noqa: E501
        :type: int
        """

        self._cpu_percent = cpu_percent

    @property
    def io_maximum_i_ops(self):
        """Gets the io_maximum_i_ops of this DockerResources.  # noqa: E501

        Maximum IOps for the container system drive (Windows only)  # noqa: E501

        :return: The io_maximum_i_ops of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._io_maximum_i_ops

    @io_maximum_i_ops.setter
    def io_maximum_i_ops(self, io_maximum_i_ops):
        """Sets the io_maximum_i_ops of this DockerResources.

        Maximum IOps for the container system drive (Windows only)  # noqa: E501

        :param io_maximum_i_ops: The io_maximum_i_ops of this DockerResources.  # noqa: E501
        :type: int
        """

        self._io_maximum_i_ops = io_maximum_i_ops

    @property
    def io_maximum_bandwidth(self):
        """Gets the io_maximum_bandwidth of this DockerResources.  # noqa: E501

        Maximum IO in bytes per second for the container system drive (Windows only)  # noqa: E501

        :return: The io_maximum_bandwidth of this DockerResources.  # noqa: E501
        :rtype: int
        """
        return self._io_maximum_bandwidth

    @io_maximum_bandwidth.setter
    def io_maximum_bandwidth(self, io_maximum_bandwidth):
        """Sets the io_maximum_bandwidth of this DockerResources.

        Maximum IO in bytes per second for the container system drive (Windows only)  # noqa: E501

        :param io_maximum_bandwidth: The io_maximum_bandwidth of this DockerResources.  # noqa: E501
        :type: int
        """

        self._io_maximum_bandwidth = io_maximum_bandwidth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerResources):
            return True

        return self.to_dict() != other.to_dict()
