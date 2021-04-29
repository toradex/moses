"""Docker export features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
import os
import logging
from typing import Optional, Dict, Callable, Tuple, Any, List
import yaml
import docker
import docker.models.containers
import platformconfig
import tags
import progresscookie
import dockerapi
from applicationconfig_base import ApplicationConfigBase
from moses_exceptions import (NoTagError, ImageNotFoundError)
from remotedocker import get_mount_info


def _blkio_weight_device_cmdline_helper(devices: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for device in devices:
        cmdline += "--blkio-weight-device " + \
            device["Path"] + ":" + str(device["Weight"]) + " "

    return cmdline


def _device_read_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for limit in limits:
        cmdline += "--device-read-bps " + \
            limit["Path"] + ":" + str(limit["Rate"]) + " "

    return cmdline


def _device_write_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for limit in limits:
        cmdline += "--device-write-bps " + \
            limit["Path"] + ":" + str(limit["Rate"]) + " "

    return cmdline


def _device_read_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for limit in limits:
        cmdline += "--device-read-iops " + \
            limit["Path"] + ":" + str(limit["Rate"]) + " "

    return cmdline


def _device_write_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for limit in limits:
        cmdline += "--device-write-iops " + + \
            limit["Path"] + ":" + str(limit["Rate"]) + " "

    return cmdline


def _log_config_cmdline_helper(value: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = "--log-driver " + value["type"]

    for limit in value["config"].items():
        cmdline += " --log-opt " + limit[0] + "=" + limit[1] + " "

    return cmdline

_mount_parms: Dict[str, str] = {
    "type":"type",
    "source":"source",
    "target":"target",
    "propagation":"bind-propagation"
    }

def _mounts_cmdline_helper(mounts: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for mount in mounts:
        cmdline += "--mount "
        firstparm = True
        for key,value in _mount_parms.items():
            if key in mount:
                cmdline+=("" if firstparm else ",")+value+"="+mount[key]
                firstparm=False

        if "readonly" in mount and mount["readonly"]:
            cmdline += ("" if firstparm else ",") + \
                "readonly=" + ("1" if mount["read_only"] else "0") + " "

    return cmdline


def _ports_cmdline_helper(ports: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for port in ports.items():
        cmdline += "--publish "
        containerport = port[0]

        if port[1] is None:
            cmdline += containerport + " "
        elif isinstance(port[1], int):
            cmdline += str(port[1]) + ":" + containerport + " "
        elif isinstance(port[1], tuple):
            cmdline += port[1][0] + ":" + \
                port[1][1] + ":" + containerport + " "

    return cmdline


def _restart_policy_cmdline_helper(value: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    cmdline += "--restart-condition " + value["Name"] + " "
    cmdline += "--restart-max-attempts" + value["MaximumRetryCount"] + " "

    return cmdline


def _ulimits_cmdline_helper(ulimits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for ulimit in ulimits:
        cmdline += "--ulimit " + ulimit.name + "=" + \
            str(ulimit.soft) + ":" + str(ulimit.hard) + " "

    return cmdline


def _volumes_cmdline_helper(volumes: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for volume in volumes.items():
        cmdline += " --volume " + volume[0] + \
            volume[1]["bind"] + "," + volume[1]["mode"]

    return cmdline


_boolean_parms: Dict[str, str] = {
    "auto_remove": "--rm",
    "detach": "--detach",
    "init": "--init",
    "network_disabled": "--network=none",
    "oom_kill_disable": "--oom-kill-disable",
    "privileged": "--privileged",
    "publish_all_ports": "--publish-all",
    "read_only": "--read-only",
    "remove": "--rm",
    "tty": "--tty",
}

_str_parms: Dict[str, str] = {
    "cgroup_parent": "--cgroup-parent",
    "cpuset_cpus": "--cpuset-cpus",
    "cpuset_mems": "--cpuset-mems",
    "domainname": "--domainname",
    "entrypoint": "--entrypoint",
    "hostname": "--hostname",
    "ipc_mode": "--ipc",
    "isolation": "--isolation",
    "kernel_memory": "--kernel-memory",
    "mac_address": "--mac-address",
    "mem_limit": "--memory",
    "mem_reservation": "--memory-reservation",
    "memswap_limit": "--memory-swap",
    "name": "--name",
    "network": "--network",
    "network_mode": "--network",
    "pid_mode": "--pid",
    "pids_limit": "--pids-limit",
    "platform": "--platform",
    "runtime": "--runtime",
    "shm_size": "--shm-size",
    "stop_signal": "--stop-signal",
    "user": "--user",
    "userns_mode": "--userns",
    "uts_mode": "--uts",
    "volume_driver": "--volume-driver",
    "working_dir": "--workdir",
}

_int_parms: Dict[str, str] = {
    "blkio_weight": "--blkio-weight",
    "cpu_period": "--cpu-period",
    "cpu_quota": "--cpu_quota",
    "cpu_rt_period": "--cpu-rt-period",
    "cpu_rt_runtime": "--cpu-rt-runtime",
    "cpu_shares": "--cpu-shares",
    "kernel_memory": "--kernel-memory",
    "mem_limit": "--memory",
    "mem_reservation": "--memory-reservation",
    "mem_swappiness": "--memory-swappiness",
    "memswap_limit": "--memory-swap",
    "oom_score_adj": "--oom-score-adj",
    "pids_limit": "--pids-limit",
    "shm_size": "--shm-size",
    "user": "--user",
}

_repeated_list_parms: Dict[str, str] = {
    "cap_add": "--cap-add",
    "cap_drop": "--cap-drop",
    "device_cgroup_rules": "--device-cgroup-rule",
    "devices": "--device",
    "dns": "--dns",
    "dns_opt": "--dns-option",
    "dns_search": "--dns-search",
    "domainname": "--domainname",
    "environment": "--env",
    "group_add": "--group-add",
    "labels": "--label",
    "security_opt": "--security-opt",
    "volumes_from": "--volumes-from",
}

_joined_list_parms: Dict[str, Tuple] = {"entrypoint": ("--entrypoint", " ")}

_key_val_dict_parms: Dict[str, Tuple] = {
    "environment": ("--env", "="),
    "extra_hosts": ("--add-host", ":"),
    "labels": ("--label", "="),
    "links": ("--link", ":"),
    "storage_opts": ("--storage-opt", "="),
    "sysctls": ("--sysctl", "="),
}

_special_parms: Dict[str, Callable[..., str]] = {
    "blkio_weight_device": _blkio_weight_device_cmdline_helper,
    "device_read_bps": _device_read_bps_cmdline_helper,
    "device_write_bps": _device_write_bps_cmdline_helper,
    "device_read_iops": _device_read_iops_cmdline_helper,
    "device_write_iops": _device_write_iops_cmdline_helper,
    "log_config": _log_config_cmdline_helper,
    "mounts": _mounts_cmdline_helper,
    "ports": _ports_cmdline_helper,
    "restart_policy": _restart_policy_cmdline_helper,
    "ulimits": _ulimits_cmdline_helper,
    "volumes": _volumes_cmdline_helper,
}


def _process_extra_parameter(parm: str, value: Any) -> Optional[str]:
    """Convert the parameter to command line format.

    :param parm: parameter name
    :type parm: str
    :param value: parameter value (as decoded from Yaml)
    :type value: Any
    :return: string to be appended to the command line
    :rtype: str | None
    """
    retvalue = None
    if parm in _special_parms:
        retvalue = _special_parms[parm](value)
    elif parm in _boolean_parms and value:
        retvalue = _boolean_parms[parm]
    elif isinstance(value, str) and parm in _str_parms:
        retvalue = _str_parms[parm] + " '" + value + "'"
    elif isinstance(value, int) and parm in _int_parms:
        retvalue = _int_parms[parm] + " " + str(value)
    elif isinstance(value, list):
        if parm in _repeated_list_parms:
            cmdline = ""
            for val in value:
                cmdline += " " + _repeated_list_parms[parm] + " '" + val + "' "
            retvalue = cmdline
        elif parm in _joined_list_parms:
            cmdline = _repeated_list_parms[parm][0] + " '"
            for val in value:
                cmdline += val + _repeated_list_parms[parm][1]
            cmdline += "'"
            retvalue = cmdline
    elif isinstance(value, dict):
        if parm in _key_val_dict_parms:
            cmdline = ""
            for val in value.items():
                cmdline += (
                    _key_val_dict_parms[parm][0]
                    + " "
                    + val[0]
                    + _key_val_dict_parms[parm][1]
                    + val[1]
                    + " "
                )
            retvalue = cmdline

    return retvalue

# pylint: disable = too-many-locals


def get_docker_commandline(self: ApplicationConfigBase,
                           configuration: str) -> str:
    """Return a docker command line that can be used to run the application's container.

    :param configuration: debug/release
    :type configuration: str
    :returns: command line for Linux target
    :rtype: str

    """
    # this function will be part of ApplicationConfig via import
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert plat is not None

    ports = self._merge_props(plat, configuration, "ports")
    volumes = self._merge_props(plat, configuration, "volumes")
    devices = self._append_props(plat, configuration, "devices")
    extraparms = self._merge_props(plat, configuration, "extraparms")
    networks = list(dict.fromkeys(
        self._append_props(plat, configuration, "networks")))

    cmdline = "docker run"

    # parse extraparms
    for parm in extraparms:
        parmvalue = extraparms[parm]

        parmvalue = tags.replace_tags(
            parmvalue,
            self._get_value,
            configuration,
        )
        parmvalue = yaml.full_load(parmvalue)

        parmvalue = _process_extra_parameter(parm, parmvalue)

        if parmvalue is None:
            logging.warning(
                "Parameter %s can't be converted into command line parameter", parm
            )
        else:
            cmdline += " " + parmvalue

    # parse mountpoints
    for volume in volumes.items():
        destvolume = volume[1]
        destvolume=destvolume.replace(",", ":")

        cmdline += " --volume " + volume[0] + ":" + destvolume

    # parse networks
    for network in networks:
        cmdline += " --network " + network

    # parse devices
    for device in devices:
        cmdline += " --device " + device + ":" + device

    # parse ports
    for port in ports.items():
        if port[1] is None:
            cmdline += " --publish " + port[0]
        else:
            cmdline += " --publish " + str(port[1]) + ":" + port[0]

    cmdline += " " + self._get_image_name(configuration)

    # check if there's a command specified in extra parms
    if "command" in extraparms:
        value = extraparms["command"]

        if isinstance(value, list):
            cmdline += " '" + (" ".join(value)) + "'"
        else:
            cmdline += " '" + str(value) + "'"

    return cmdline

_compose_mount_map : Dict[str,List[str]]= {
    "type" : [ "type" ],
    "source" : [ "source" ],
    "target" : [ "target" ],
    "read_only": [ "read_only" ],
    "consistency": [ "consistency" ],
    "propagation": [ "bind", "propagation" ],
    "no_copy": ["volume", "nocopy"],
    "tmpfs_size": ["tmpfs", "size"]
}

def _translate_mounts(mounts: List[Dict[str,Any]]) -> list:
    compose_mounts = []

    for mount in mounts:

        compose_mount : Dict[str,Any]= {}

        for field in _compose_mount_map.items():
            if not field[0] in mount:
                continue

            target_dict = compose_mount

            for k in field[1][:-1]:
                target_dict[k]={}
                target_dict=target_dict[k]

            target_dict[field[1][-1]]=mount[field[0]]

        compose_mounts.append(compose_mount)

    return compose_mounts

_compose_parms: Dict[str, Optional[Callable]] = {
    "cap_add": None,
    "cap_drop": None,
    "cgroup_parent": None,
    "command": None,
    "devices": None,
    "domainname": None,
    "dns": None,
    "dns_search": None,
    "entrypoint": None,
    "environment": None,
    "extra_hosts": lambda x: (
        "extra_hosts",
        map((lambda h: h[0] + ":" + h[1]), x.items()),
    ),
    "healtcheck": None,
    "hostname": None,
    "init": None,
    "isolation": None,
    "labels": None,
    "log_config": None,
    "mounts": (
        lambda x: (
            "volumes",
            _translate_mounts(
                yaml.load(x[1], Loader=yaml.FullLoader),
            )
        )
    ),
    "name": lambda x: ("container_name", x),
    "network_mode": None,
    "pid_mode": lambda x: ("pid", x),
    "ports": lambda x: (
        "ports",
        list(map(lambda y:
            (str(y[1])+":" if y[1] is not None else "")+ \
            str(y[0])
            , x[1].items())),
    ),
    "privileged": None,
    "read_only": None,
    "restart": None,
    "shm_size": None,
    "stdin_open": None,
    "tty": None,
    "user": None,
    "version": None,
    "volumes": (
        lambda x: (
            "volumes",
            list(
                map(
                    lambda y: str(y[0])
                    + ":"
                    + str(y[1]["bind"])
                    + ":"
                    + str(y[1]["mode"]),
                    x[1].items(),
                )
            ),
        )
    ),
    "working_dir": None,
}


# pylint: disable = too-many-locals
# pylint: disable = too-many-branches
def get_docker_composefile(self: ApplicationConfigBase,
                           configuration: str) -> Optional[str]:
    """Return a docker-compose file that can be used to run the application's container.

    The docker-compose file will start also the dependencies.

    :param configuration: debug/release
    :type configuration: str
    :returns: content of the compose file (*nix line-endings)
    :rtype: str | None

    """
    # this function will be part of ApplicationConfig via import
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert plat is not None

    ports = self._merge_props(plat, configuration, "ports")
    volumes = self._merge_props(plat, configuration, "volumes")
    devices = self._append_props(plat, configuration, "devices")
    extraparms = self._merge_props(plat, configuration, "extraparms")
    networks = list(dict.fromkeys(
        self._append_props(plat, configuration, "networks")))

    composeyaml = yaml.load("services: {}", Loader=yaml.FullLoader)

    composefile = self._get_prop(configuration, "dockercomposefile")
    composefilepath = self.folder

    # if no compose file is specified for the application, check platform
    if composefile is None or len(composefile) == 0:
        composefile = plat.get_prop(configuration, "dockercomposefile")
        composefilepath = plat.folder

    if composefile is not None and len(composefile) > 0:
        assert composefilepath is not None

        with open(os.path.join(composefilepath, composefile), "r") as composef:
            composeyaml = yaml.load(composef, Loader=yaml.FullLoader)

    composeyaml["version"]="2.4"

    # create and fill new service
    service : Dict[str,Any] = dict()

    # merge volumes, devices, ports into extraparms
    # (we can't have multiple instances of the same parameter)
    if not "ports" in extraparms:
        extraparms["ports"] = dict()

    if not "devices" in extraparms:
        extraparms["devices"] = list()

    if not "volumes" in extraparms:
        extraparms["volumes"] = dict()

    for port in ports.items():
        if port[1] == "":
            extraparms["ports"][port[0]] = None
        else:
            extraparms["ports"][port[0]] = port[1]

    for volume in volumes.items():
        extraparms["volumes"][volume[0]] = get_mount_info(volume[1])

    extraparms["devices"].extend(devices)

    # process extraparms and add them to the dictionary
    for extraparm,value in extraparms.items():
        if extraparm in _compose_parms:
            helperfn = _compose_parms[extraparm]

            if helperfn is None:
                service[extraparm] = value
                continue

            parm, value = helperfn((extraparm, value))

            # special case since we have two parameters (mounts and volumes)
            # that generate the same yaml tag
            if parm=="volumes" and "volumes" in service:
                service[parm].extend(value)
            else:
                service[parm] = value

    service["image"] = self._get_image_name(configuration)

    if self._get_prop(configuration, "depends_on") is not None:
        service["depends_on"] = self._get_prop(configuration, "depends_on")
    else:
        service["depends_on"] = list(composeyaml["services"].keys())

    composeyaml["services"][self._get_image_name(configuration)] = service

    for network in networks:
        composeyaml["networks"][network] = {}

    return yaml.dump(composeyaml)


def push_to_registry(self: ApplicationConfigBase, configuration: str, username: str,
                     password: str, progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Push the application container to a docker registry.

    :param configuration: debug/release
    :type configuration: str
    :param username: username
    :type username: str
    :param password: password
    :param password: str
    :param progress: object use to report operation progress
    :type progress: progresscookie.ProgressCookie, optional

    Image should have been built at least once for the required
    configuration.

    """
    # this function will be part of ApplicationConfig via import
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    tag = self.get_custom_prop(configuration, "tag")

    if tag is None:
        raise NoTagError()

    repository = None

    parts = tag.split(":")
    parts_count = len(parts)
    if parts_count > 1:
        repository = ":".join(parts[0:parts_count - 1])
        tag = parts[parts_count - 1]
    else:
        repository = tag
        tag = None

    imgid = self.images[configuration]

    if imgid is None or imgid == "":
        logging.error(
            "Image has never been build for application %s.", self.folder)
        raise ImageNotFoundError("")

    localdocker = docker.from_env()

    try:
        limg = localdocker.images.get(imgid)
    except docker.errors.ImageNotFound as exception:
        logging.error(
            "Image %s not found when deploying application %s.",
            imgid,
            self.folder,
        )
        raise ImageNotFoundError(imgid) from exception

    # ensure that the image is correctly tagged
    limg.tag(repository, tag)

    dockerapi.push_image(localdocker, repository, tag,
                         username, password, progress)
