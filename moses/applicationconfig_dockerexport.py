"""Docker export features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been 
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
from api import eulas_eula_get
import os
import logging
import yaml
import docker
import docker.models.containers
import platformconfig
import exceptions
import tags
import progresscookie
import dockerapi
from typing import Optional, Dict, Callable, Tuple, Any
from applicationconfig_base import ApplicationConfigBase


def _blkio_weight_device_cmdline_helper(devices: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in devices:
        cmdline += "--blkio-weight-device " + v["Path"] + ":" + str(v["Weight"]) + " "

    return cmdline


def _device_read_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-read-bps " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_write_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-write-bps " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_read_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-read-iops " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_write_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-write-iops " + +v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _log_config_cmdline_helper(value: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = "--log-driver " + value["type"]

    for v in value["config"].items():
        cmdline += " --log-opt " + v[0] + "=" + v[1] + " "

    return cmdline


def _mounts_cmdline_helper(mounts: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for m in mounts:
        cmdline += "--mount "
        cmdline += "type=" + m["type"]
        cmdline += ",source=" + m["source"]
        cmdline += ",target=" + m["target"]
        cmdline += ",readonly=" + ("1" if m["read_only"] else "0") + " "

    return cmdline


def _ports_cmdline_helper(ports: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for p in ports.items():
        cmdline += "--publish "
        containerport = p[0]

        if p[1] is None:
            cmdline += containerport + " "
        elif isinstance(p[1], int):
            cmdline += str(p[1]) + ":" + containerport + " "
        elif isinstance(p[1], tuple):
            cmdline += p[1][0] + ":" + p[1][1] + ":" + containerport + " "

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

    for u in ulimits:
        cmdline += "--ulimit " + u.name + "=" + str(u.soft) + ":" + str(u.hard) + " "

    return cmdline


def _volumes_cmdline_helper(volumes: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in volumes.items():
        cmdline += " --volume " + v[0] + v[1]["bind"] + "," + v[1]["mode"]

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
    "mem_limit": "--memory",
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
    if parm in _boolean_parms and value:
        return _boolean_parms[parm]

    if isinstance(value, str) and parm in _str_parms:
        return _str_parms[parm] + " '" + value + "'"

    if isinstance(value, int) and parm in _int_parms:
        return _int_parms[parm] + " " + str(value)

    if isinstance(value, list):
        if parm in _repeated_list_parms:
            cmdline = ""
            for v in value:
                cmdline += " " + _repeated_list_parms[parm] + " '" + v + "' "
            return cmdline

        if parm in _joined_list_parms:
            cmdline = _repeated_list_parms[parm][0] + " '"
            for v in value:
                cmdline += v + _repeated_list_parms[parm][1]
            cmdline += "'"
            return cmdline

    if isinstance(value, dict):
        if parm in _key_val_dict_parms:
            cmdline = ""
            for v in value.items():
                cmdline += (
                    _key_val_dict_parms[parm][0]
                    + " "
                    + v[0]
                    + _key_val_dict_parms[parm][1]
                    + v[1]
                    + " "
                )
            return cmdline

    if parm in _special_parms:
        return _special_parms[parm](value)

    return None


def get_docker_commandline(self: ApplicationConfigBase, configuration: str) -> str:
    """Return a docker command line that can be used to run the application's container.

    :param configuration: debug/release
    :type configuration: str
    :returns: command line for Linux target
    :rtype: str

    """
    plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

    if plat is None:
        return None

    ports = self._merge_props(plat, configuration, "ports")
    volumes = self._merge_props(plat, configuration, "volumes")
    devices = self._append_props(plat, configuration, "devices")
    extraparms = self._merge_props(plat, configuration, "extraparms")
    networks = list(dict.fromkeys(self._append_props(plat, configuration, "networks")))

    cmdline = "docker run"

    # parse extraparms
    for parm in extraparms:
        rawvalue = extraparms[parm]

        rawvalue = tags.replace_tags(
            rawvalue,
            lambda obj, tag, args: self._get_value(obj, tag, args),
            configuration,
        )
        value = yaml.full_load(rawvalue)

        parmvalue = _process_extra_parameter(parm, value)

        if parmvalue is None:
            logging.warning(
                "Parameter %s can't be converted into command line parameter", parm
            )
        else:
            cmdline += " " + parmvalue

    # parse mountpoints
    for v in volumes.items():
        cmdline += " --volume " + v[0] + ":" + v[1]

    # parse networks
    for n in networks:
        cmdline += " --network " + n

    # parse devices
    for d in devices:
        cmdline += " --device " + d + ":" + d

    # parse ports
    for p in ports.items():
        if p[1] is None:
            cmdline += " --publish " + p[0]
        else:
            cmdline += " --publish " + str(p[1]) + ":" + p[0]

    cmdline += " " + self._get_image_name(configuration)

    # check if there's a command specified in extra parms
    if "command" in extraparms:
        value = extraparms["command"]

        if isinstance(value, list):
            cmdline += " '" + (" ".join(value)) + "'"
        else:
            cmdline += " '" + str(value) + "'"

    return cmdline


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
    "name": lambda x: ("container_name", x),
    "network_mode": None,
    "pid_mode": lambda x: ("pid", x),
    "ports": lambda x: (
        "ports",
        list(map(lambda y: str(y[0]) + ":" + str(y[1]), x[1].items())),
    ),
    "privileged": None,
    "read_only": None,
    "restart": None,
    "shm_size": None,
    "stdin_open": None,
    "tty": None,
    "user": None,
    "volumes": (
        lambda x: (
            "volumes",
            list(
                map(
                    lambda y: str(y[0])
                    + ":"
                    + str(y[1]["bind"])
                    + ","
                    + str(y[1]["mode"]),
                    x[1].items(),
                )
            ),
        )
    ),
    "working_dir": None,
}


def get_docker_composefile(
    self: ApplicationConfigBase, configuration: str
) -> Optional[str]:
    """Return a docker-compose file that can be used to run the application's container and its dependencies.

    :param configuration: debug/release
    :type configuration: str
    :returns: content of the compose file (*nix line-endings)
    :rtype: str | None

    """
    plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

    if plat is None:
        return None

    ports = self._merge_props(plat, configuration, "ports")
    volumes = self._merge_props(plat, configuration, "volumes")
    devices = self._append_props(plat, configuration, "devices")
    extraparms = self._merge_props(plat, configuration, "extraparms")
    networks = list(dict.fromkeys(self._append_props(plat, configuration, "networks")))

    composefile = self._get_prop(configuration, "dockercomposefile")

    if composefile is not None and len(composefile) > 0:
        assert self.folder is not None

        with open(os.path.join(self.folder, composefile), "r") as f:
            composeyaml = yaml.load(f, Loader=yaml.FullLoader)
    else:
        composeyaml = yaml.load("services: {}", Loader=yaml.FullLoader)

    # create and fill new service
    service = dict()

    # merge volumes, devices, ports into extraparms (we can't have multiple instances of the same parameter)
    if not "ports" in extraparms:
        extraparms["ports"] = dict()

    if not "devices" in extraparms:
        extraparms["devices"] = list()

    if not "volumes" in extraparms:
        extraparms["volumes"] = dict()

    for p in ports.items():
        if p[1] == "":
            extraparms["ports"][p[0]] = None
        else:
            extraparms["ports"][p[0]] = p[1]

    for v in volumes.items():
        bind, mode = (v[1] + ",rw").split(",")[0:2]
        extraparms["volumes"][v[0]] = {"bind": bind, "mode": mode}

    extraparms["devices"].extend(devices)

    # process extraparms and add them to the dictionary
    for ep in extraparms.keys():
        if ep in _compose_parms:
            if _compose_parms[ep] is None:
                service[ep] = extraparms[ep]
            else:

                helperfn = _compose_parms[ep]

                assert helperfn is not None

                parm, value = helperfn((ep, extraparms[ep]))
                service[parm] = value

    service["image"] = self._get_image_name(configuration)

    if self._get_prop(configuration, "depends_on") is not None:
        service["depends_on"] = self._get_prop(configuration, "depends_on")
    else:
        service["depends_on"] = list(composeyaml["services"].keys())

    composeyaml["services"][self._get_image_name(configuration)] = service

    return yaml.dump(composeyaml)


def push_to_registry(
    self: ApplicationConfigBase,
    configuration: str,
    username: str,
    password: str,
    progress: Optional[progresscookie.ProgressCookie],
) -> None:
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
    tag = self._get_custom_prop(configuration, "tag")

    if tag is None:
        raise exceptions.NoTagError()

    repository = None

    parts = tag.split(":")
    if len(parts) > 1:
        repository, tag = parts
    else:
        repository = tag
        tag = None

    imgid = self.images[configuration]

    if imgid is None or imgid == "":
        logging.error("Image has never been build for application %s.", self.folder)
        raise exceptions.ImageNotFoundError("")

    localdocker = docker.from_env()

    try:
        limg = localdocker.images.get(imgid)
    except docker.errors.ImageNotFound:
        logging.error(
            "Image %s not found when deploying application %s.",
            imgid,
            self.folder,
        )
        raise exceptions.ImageNotFoundError(imgid)

    # ensure that the image is correctly tagged
    limg.tag(repository, tag)

    dockerapi.push_image(localdocker, repository, tag, username, password, progress)
