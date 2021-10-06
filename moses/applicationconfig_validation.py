"""Validation of the application configuration."""
import copy
import threading
from typing import Any,Callable, Dict, List, Optional, Tuple
from applicationconfig_base import ApplicationConfigBase
from moses_exceptions import InternalServerError
import platformconfig
import validation

validation_table :  Dict[str,
                                List[
                                Tuple[
                                        bool,
                                        Callable[...,Optional[str]],
                                        Any]]] = {
    "username": [
        (True,validation.validate_non_empty_string, None),
        (True,validation.validate_username, None)
        ],
    "otapackageversion": [
        (False, validation.validate_semantic_version, None)],
    "dockercomposefile": [
        (True, validation.validate_relative_file_path, None)],
    "startupscript": [
        (True, validation.validate_relative_file_path, None)],
    "shutdownscript": [
        (True, validation.validate_relative_file_path, None)],
}

skip_table :  Dict[str,
                   List[Callable[...,bool]]]= {
    "username": [validation.skip_if_contains_tags],
    "otapackagename": [validation.skip_if_empty, validation.skip_if_contains_tags],
    "otapackageversion": [validation.skip_if_empty, validation.skip_if_contains_tags],
    "dockercomposefile": [validation.skip_if_empty, validation.skip_if_contains_tags],
    "startupscript": [validation.skip_if_empty, validation.skip_if_contains_tags],
    "shutdownscript": [validation.skip_if_empty, validation.skip_if_contains_tags],
    "networks": [validation.skip_if_contains_tags],
    "devices": [validation.skip_if_contains_tags],
    "volumes": [validation.skip_if_contains_tags],
    "ports": [validation.skip_if_contains_tags],
    "extraparms": [validation.skip_if_contains_tags],
}

array_validation_table : Dict[str,
                                List[
                                Tuple[
                                        bool,
                                        Callable[...,Optional[str]],
                                        Any]]] = {
    "networks": [
        (True, validation.validate_non_empty_string, None),
        (True, validation.validate_docker_name, None),
        (True, validation.validate_unique_items, None),
    ],
    "devices": [
        (True, validation.validate_non_empty_string, None),
        (True, validation.validate_unique_items, None),
        (True, validation.validate_remote_path, None),
        (False, validation.validate_device_name, None),
    ],
}

dictionary_validation_table : Dict[str,
                                List[
                                Tuple[
                                        bool,
                                        Callable[...,Optional[str]],
                                        Any]]] = {
    "ports": [
        (True, validation.validate_non_empty_key, None),
        (True, validation.validate_key, (validation.validate_port, None)),
        (True, validation.validate_unique_keys, None),
        (True, validation.validate_or, [
            (validation.validate_empty_string, None),
            (validation.validate_number, (0,65535))]),
    ],
    "volumes": [
        (True, validation.validate_non_empty_key, None),
        (True, validation.validate_unique_keys, None),
        (True, validation.validate_non_empty_string, None),
        (True, validation.validate_key, (validation.validate_remote_path, None)),
        (True, validation.validate_mount_info, None),
    ],
    "extraparms": [
        (True, validation.validate_non_empty_key, None),
        (True, validation.validate_non_empty_string, None),
        (True, validation.validate_unique_keys, None),
        (True, validation.validate_yaml, None),
        (True, validation.validate_key, (validation.validate_id, None)),
        (True, validation.validate_entry,
            ("auto_remove", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("command", validation.validate_yaml_schema, validation.YAML_STRING_OR_LIST)),
        (True, validation.validate_entry,
            ("blkio_weight_device", validation.validate_yaml_schema, "\
                type: object\n\
                properties:\n\
                    Path:\n\
                        type: string\n\
                    Weight:\n\
                        type: integer\n\
                        minimum: 10\n\
                        maximum: 1000\n\
                required: [ \"Path\", \"Weight\"]\n\
                ")),
        (True, validation.validate_entry,
            ("blkio_weight", validation.validate_yaml_schema, "\
                type: integer\n\
                minimum: 10\n\
                maximum: 1000\n\
                ")),
        (True, validation.validate_entry,
            ("cap_add", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("cap_drop", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("cgroup_parent", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("cpu_period", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("cpu_quota", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("cpu_rt_period", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("cpu_rt_quota", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("cpu_shares", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("cpuset_cpus", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("detach", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("device_cgroup_rules", validation.validate_yaml_schema,
             validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("device_read_bps", validation.validate_yaml_schema, "\
                type: array\n\
                items:\n\
                    type: object\n\
                    properties:\n\
                        Path:\n\
                            type: string\n\
                        Rate:\n\
                            type: integer\n\
                    required: [ \"Path\", \"Rate\"]\n\
                ")),
        (True, validation.validate_entry,
            ("device_read_iops", validation.validate_yaml_schema, "\
                type: array\n\
                items:\n\
                    type: object\n\
                    properties:\n\
                        Path:\n\
                            type: string\n\
                        Rate:\n\
                            type: integer\n\
                    required: [ \"Path\", \"Rate\"]\n\
                ")),
        (True, validation.validate_entry,
            ("device_write_bps", validation.validate_yaml_schema, "\
                type: array\n\
                items:\n\
                    type: object\n\
                    properties:\n\
                        Path:\n\
                            type: string\n\
                        Rate:\n\
                            type: integer\n\
                    required: [ \"Path\", \"Rate\"]\n\
                ")),
        (True, validation.validate_entry,
            ("device_write_iops", validation.validate_yaml_schema, "\
                type: array\n\
                items:\n\
                    type: object\n\
                    properties:\n\
                        Path:\n\
                            type: string\n\
                        Rate:\n\
                            type: integer\n\
                    required: [ \"Path\", \"Rate\"]\n\
                ")),
        (True, validation.validate_entry,
            ("devices", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("dns", validation.validate_yaml_schema, validation.YAML_STRING_OR_LIST)),
        (True, validation.validate_entry,
            ("dns_search", validation.validate_yaml_schema, validation.YAML_STRING_OR_LIST)),
        (True, validation.validate_entry,
            ("domainname", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("entrypoint", validation.validate_yaml_schema, validation.YAML_STRING_OR_LIST)),
        (True, validation.validate_entry,
            ("env_file", validation.validate_yaml_schema, validation.YAML_STRING_OR_LIST)),
        (True, validation.validate_entry,
            ("environment", validation.validate_yaml_schema, validation.YAML_LIST_OR_DICT)),
        (True, validation.validate_entry,
            ("extra_hosts", validation.validate_yaml_schema, validation.YAML_LIST_OR_DICT)),
        (True, validation.validate_entry,
            ("group_add", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("healthcheck", validation.validate_yaml_schema, "\
            type: [ object, 'null' ]\n\
            properties:\n\
                interval:\n\
                    type: [ string, number ]\n\
                start_period:\n\
                    type: [ string, number ]\n\
                timeout:\n\
                    type: [ string, number ]\n\
                retries:\n\
                    type: number\n\
                test:\n\
                    oneOf:\n\
                    - type: string\n\
                    - type: array\n\
                      items:\n\
                        type: string\n\
                disable:\n\
                    type: boolean\n\
            additionalProperties: false\n\
            ")),
        (True, validation.validate_entry,
            ("hostname", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("init", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("init_path", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("ipc_mode", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("isolation", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("kernel_memory", validation.validate_yaml_schema, "{ type: [string, integer] }")),
        (True, validation.validate_entry,
            ("labels", validation.validate_yaml_schema, validation.YAML_LIST_OR_DICT)),
        (True, validation.validate_entry,
            ("log_config", validation.validate_yaml_schema, "\
            type: object\n\
            properties:\n\
                Type:\n\
                    type: string\n\
                Config:\n\
                    type: object\n\
                    patternProperties:\n\
                        ^.+$:\n\
                            type:\n\
                                - string\n\
                                - number\n\
                                - 'null'\n\
            additionalProperties: false\n\
            ")),
        (True, validation.validate_entry,
            ("mac_address", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("mem_limit", validation.validate_yaml_schema, "{ type: [string, integer] }")),
        (True, validation.validate_entry,
            ("mem_reservation", validation.validate_yaml_schema, "{ type: [string, integer] }")),
        (True, validation.validate_entry,
            ("memswap_limit", validation.validate_yaml_schema, "{ type: [string, integer] }")),
        (True, validation.validate_entry,
            ("mounts", validation.validate_yaml_schema, "\
            type: array\n\
            items:\n\
                type: object\n\
                properties:\n\
                    target:\n\
                        type: string\n\
                    source:\n\
                        type: string\n\
                    type:\n\
                        type: string\n\
                    readonly:\n\
                        type: boolean\n\
                    consistency:\n\
                        type: string\n\
                    propagation:\n\
                        type: string\n\
                    no_copy:\n\
                        type: boolean\n\
                    labels:\n\
                        type: object\n\
                        additionalProperties: true\n\
                    driver_config:\n\
                        type: object\n\
                        properties:\n\
                            name:\n\
                                type: string\n\
                            options:\n\
                                type: object\n\
                                additionalProperties: true\n\
                    tmpfs_size:\n\
                        type:\n\
                          - string\n\
                          - integer\n\
                    tmpfs_mode:\n\
                        type: integer\n\
                additionalProperties: true\n\
            ")),
        (True, validation.validate_entry,
            ("nano_cpus", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("network", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("network_disabled", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("network_mode", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("oom_kill_disable", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("oom_score_adj", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("pid_mode", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("pids_limit", validation.validate_yaml_schema, validation.YAML_INTEGER)),
        (True, validation.validate_entry,
            ("platform", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("ports", validation.validate_yaml_schema, validation.YAML_DICT)),
        (True, validation.validate_entry,
            ("privileged", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("publish_all_ports", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("read_only", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("remove", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("restart_policy", validation.validate_yaml_schema, "\
            type: object\n\
            properties:\n\
                Name:\n\
                    type: string\n\
                MaximumRetryCount:\n\
                    type: integer\n\
            ")),
        (True, validation.validate_entry,
            ("runtime", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("security_opt", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("shm_size", validation.validate_yaml_schema, "{ type: [string, integer]}")),
        (True, validation.validate_entry,
            ("stdin_open", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("stop_signal", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("tty", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("ulimits", validation.validate_yaml_schema, "\
            type: array\n\
            items:\n\
                type: object\n\
                properties:\n\
                    Hard:\n\
                        type: integer\n\
                    Soft:\n\
                        type: integer\n\
                    Name:\n\
                        type: string\n\
                required:\n\
                - Soft\n\
                - Hard\n\
                - Name\n\
                additionalProperties: false\n\
            ")),
        (True, validation.validate_entry,
            ("use_config_proxy", validation.validate_yaml_schema, validation.YAML_BOOLEAN)),
        (True, validation.validate_entry,
            ("user", validation.validate_yaml_schema, "{ type: [string, integer]}")),
        (True, validation.validate_entry,
            ("userns_mode", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("uts_mode", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("version", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("volume_driver", validation.validate_yaml_schema, validation.YAML_STRING)),
        (True, validation.validate_entry,
            ("volumes", validation.validate_yaml_schema, "\
            type:\n\
                - array\n\
                - object\n\
            items:\n\
                type: string\n\
            patternProperties:\n\
                \"^[a-zA-Z0-9._-]+$\":\n\
                    type: object\n\
                    properties:\n\
                        bind:\n\
                            type: string\n\
                        mode:\n\
                            type: string\n\
            ")),
        (True, validation.validate_entry,
            ("volumes_from", validation.validate_yaml_schema, validation.YAML_LIST_OF_STRINGS)),
        (True, validation.validate_entry,
            ("working_dir", validation.validate_yaml_schema, validation.YAML_STRING)),
    ],
    "props": [
        (True, validation.validate_non_empty_key, None),
        (True, validation.validate_key, (validation.validate_id, None)),
    ]
}

def init(self: ApplicationConfigBase) -> None:
    """Initialize the validation tables for the application."""
    validation.ExtendedValidation.__init__(
        self,
        copy.deepcopy(validation_table),
        copy.deepcopy(skip_table),
        copy.deepcopy(array_validation_table),
        copy.deepcopy(dictionary_validation_table))

    platformid = self.platformid

    platform = platformconfig.PlatformConfigs().get_platform(platformid)

    if platform.init_validation_tables is not None:
        platform.init_validation_tables(self)

configuration_lock = threading.RLock()
#pylint: disable=invalid-name
current_configuration = None

#pylint: disable=global-statement
def _check_current_configuration() -> bool:
    global current_configuration

    if current_configuration is None:
        raise InternalServerError("No configuration selected for validation")

def get_array(self: validation.ExtendedValidation, array_name: str) -> List[Any]:
    """Get array values.

    :param array_name: array name
    :type array_name: str
    :return: array value
    :rtype: List[Any]
    """
    _check_current_configuration()

    if not array_name in ["networks","devices"]:
        raise InternalServerError("Invalid array name")

    return self.__dict__[array_name][current_configuration]


def get_dictionary(self: validation.ExtendedValidation, dictionary_name: str) -> Dict[str, Any]:
    """Get dictionary values.

    :param dictionary_name: dictionary name
    :type dictionary_name: str
    :return: dictionary value
    :rtype: Dict[str, Any]
    """
    _check_current_configuration()

    if not dictionary_name in ["volumes","ports","props","extraparms"]:
        raise InternalServerError("Invalid dictionary name")

    return self.__dict__[dictionary_name][current_configuration]

#pylint: disable=global-statement
def validate_parameter(self: ApplicationConfigBase,
                       configuration: str,
                       parameter: str,
                       value: str) -> validation.ValidationResult:
    """Validate a configuration parameter.

    :param configuration: release/debug/common
    :type configuration: str
    :param parameter: parameter name
    :type parameter: str
    :param value: parameter value
    :type value: str
    """
    global current_configuration

    with configuration_lock:
        try:
            current_configuration = configuration
            return self.validate(parameter, value)
        finally:
            current_configuration = None


#pylint: disable=global-statement
def validate_array_item(self: ApplicationConfigBase,
                        configuration: str,
                        array: str,
                        value: str,
                        index: int) -> validation.ValidationResult:
    """Validate a configuration parameter.

    :param configuration: release/debug/common
    :type configuration: str
    :param array: array name
    :type array: str
    :param value: parameter value
    :type value: str
    """
    global current_configuration

    with configuration_lock:
        try:
            current_configuration = configuration
            return self.validate_array_item(array, value, index)
        finally:
            current_configuration = None

# pylint: disable=too-many-arguments
def validate_dictionary_entry(self: ApplicationConfigBase,
                              configuration: str,
                              dictionary: str,
                              key: str,
                              value: str,
                              newitem: bool) -> validation.ValidationResult:
    """Validate a configuration parameter.

    :param configuration: release/debug/common
    :type configuration: str
    :param dictionary: dictionary name
    :type dictionary: str
    :param key: key value
    :type key: str
    :param value: parameter value
    :type value: str
    :param newitem: True if the key is new
    :type newitem: bool
    """
    global current_configuration

    with configuration_lock:
        try:
            current_configuration = configuration
            return self.validate_dictionary_entry(dictionary, key, value, newitem)
        finally:
            current_configuration = None
