load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

source '../testcases/validation_functions.bash'
source '../run_tests.bash'

setup_file() {
    export MOSES_CURRENT_APPLICATION_FOLDER=$TIE_TEMP_DIR/appconfig_0
    export APP_TEMP_FOLDER=$TIE_TEMP_DIR

    linuxdir=$MOSES_CURRENT_APPLICATION_FOLDER

    mkdir -p $linuxdir

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        APP_TEMP_FOLDER=$(wslpath -w $TIE_TEMP_DIR | sed 's/\\/\\\\/g')
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$TIE_TEMP_DIR/appconfig_0" | sed 's/\\/\\\\/g')
    fi

    rm -fr $linuxdir

    export APP_ID=$($TDSKT create $MOSES_CURRENT_PLATFORM $APP_TEMP_FOLDER)
}

@test "ide-backend: validate username" {
    run $TDSKT application $APP_ID validate parameter common username torizon
    assert_success
    run $TDSKT application $APP_ID validate parameter common username "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate parameter common username bla@bla
    assert_output --partial "Value is not a valid Linux username"
    assert_failure 1
    run $TDSKT application $APP_ID validate parameter common username "bla bla"
    assert_output --partial "Value is not a valid Linux username"
    assert_failure 1
    run $TDSKT application $APP_ID validate parameter common username ""
    assert_output --partial "Value can't be an empty string"
    assert_failure 1
}

@test "ide-backend: validate otapackagename" {
    run $TDSKT application $APP_ID validate parameter common otapackagename blablabla
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackagename ""
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackagename "#%dummy%#"
    assert_success
}

@test "ide-backend: validate otapackageversion" {
    run $TDSKT application $APP_ID validate parameter common otapackageversion "1.0.0"
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackageversion "1.0.1234"
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackageversion ""
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackageversion "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate parameter common otapackageversion "1.aaa.0"
    assert_output --partial "Value does not appear to be a valid version number in the format maj.min.build"
    assert_failure 2
    run $TDSKT application $APP_ID validate parameter common otapackageversion "blablabla"
    assert_output --partial "Value does not appear to be a valid version number in the format maj.min.build"
    assert_failure 2
    run $TDSKT application $APP_ID validate parameter common otapackageversion "1.2.3.4.5.6.7"
    assert_output --partial "Value does not appear to be a valid version number in the format maj.min.build"
    assert_failure 2
}

@test "ide-backend: validate dockercomposefile" {
    run $TDSKT application $APP_ID validate parameter common dockercomposefile "docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common dockercomposefile "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate parameter common dockercomposefile "dummy/docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common dockercomposefile "/dummy/docker-compose.yml"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
    run $TDSKT application $APP_ID validate parameter common dockercomposefile "blablabla@@!_ //"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
}

@test "ide-backend: validate startupscript" {
    run $TDSKT application $APP_ID validate parameter common startupscript "docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common startupscript "dummy/docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common startupscript "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate parameter common startupscript "/dummy/docker-compose.yml"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
    run $TDSKT application $APP_ID validate parameter common startupscript "blablabla@@!_ //"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
}

@test "ide-backend: validate shutdownscript" {
    run $TDSKT application $APP_ID validate parameter common shutdownscript "docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common shutdownscript "dummy/docker-compose.yml"
    assert_success
    run $TDSKT application $APP_ID validate parameter common shutdownscript "/dummy/docker-compose.yml"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
    run $TDSKT application $APP_ID validate parameter common shutdownscript "blablabla@@!_ //"
    assert_output --partial "Value does not appear to be a valid relative file path."
    assert_failure 1
}

@test "ide-backend: validate networks" {
    run $TDSKT application $APP_ID validate item common networks "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate item common networks "mynetwork"
    assert_success
    run $TDSKT application $APP_ID setprop networks "[\"mynetwork\"]" common
    assert_success
    run $TDSKT application $APP_ID validate item common networks "mynetwork2"
    assert_success
    run $TDSKT application $APP_ID validate item common networks "mynetwork"
    assert_output --partial "Duplicated value"
    assert_failure 1
    run $TDSKT application $APP_ID validate item common networks "mynetwork" 0
    assert_success
    run $TDSKT application $APP_ID validate item common networks "mynetwork@@//"
    assert_output --partial "Value does not appear to be a valid docker object name"
    assert_failure 1
}

@test "ide-backend: validate devices" {
    run $TDSKT application $APP_ID validate item common devices "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate item common devices "/dev/ttyUSB0"
    assert_success
    run $TDSKT application $APP_ID setprop devices "[\"/dev/ttyUSB0\"]" common
    assert_success
    run $TDSKT application $APP_ID validate item common devices "/dev/ttyUSB1"
    assert_success
    run $TDSKT application $APP_ID validate item common devices "/dev/ttyUSB0"
    assert_output --partial "Duplicated value"
    assert_failure 1
    run $TDSKT application $APP_ID validate item common devices "/dev/ttyUSB0" 0
    assert_success
    run $TDSKT application $APP_ID validate item common devices "/dev/ttyUSB0@@//"
    assert_output --partial "Value does not appear to be a valid path"
    assert_failure 1
    run $TDSKT application $APP_ID validate item common devices "/mydev/bla"
    assert_output --partial "Device name should start with /dev"
    assert_failure 2
}

@test "ide-backend: validate ports" {
    run $TDSKT application $APP_ID validate entry common ports "8000/udp" "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate entry common ports "8000/udp" ""
    assert_success
    run $TDSKT application $APP_ID setprop ports "{ 8000/udp: \"1234\"}" common
    assert_success
    run $TDSKT application $APP_ID validate entry common ports "8000/udp" "9999"
    assert_success
    run $TDSKT application $APP_ID validate entry common ports "8000/udp" "1234" --newitem
    assert_output --partial "Duplicated key"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "blablabla" "" --newitem
    assert_output --partial "Invalid port name, must be a port number or number/protocol(tcp,udp,sctp)"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "blablabla/udp" "" --newitem
    assert_output --partial "Invalid port number"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "8000/bla" "" --newitem
    assert_output --partial "Protocol should be tcp, udp or sctp"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "9000/tcp" "bla"
    assert_output --partial "Value does not appear to be a valid number"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "9000/tcp" "-22"
    assert_output --partial "Value is not in the allowed range"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common ports "9000/tcp" "99999"
    assert_output --partial "Value is not in the allowed range"
    assert_failure 1
}

@test "ide-backend: validate volumes" {
    run $TDSKT application $APP_ID validate entry common volumes "/dummy" "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate entry common volumes "/home/torizon" "/dummy"
    assert_success
    run $TDSKT application $APP_ID validate entry common volumes "/home/torizon" "/dummy,ro"
    assert_success
    run $TDSKT application $APP_ID validate entry common volumes "/home/torizon" "/dummy,rw"
    assert_success
    run $TDSKT application $APP_ID setprop volumes "{ \"/home/torizon\": \"/dummy,rw\" }" common
    assert_success
    run $TDSKT application $APP_ID validate entry common volumes "/home/torizon" "/dummy,ro"
    assert_success
    run $TDSKT application $APP_ID validate entry common volumes "/home/torizon" "/dummy,ro" --newitem
    assert_output --partial "Duplicated key"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common volumes "/home/@@@torizon" "/dummy,ro" --newitem
    assert_output --partial "Value does not appear to be a valid path"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry common volumes "/home/blablabla" "/dummy//@@,ro" --newitem
    assert_output --partial "Invalid mount point"
    assert_failure 1
}

@test "ide-backend: validate extraparms" {
    run $TDSKT application $APP_ID validate entry common extraparms "dummy" "#%dummy%#"
    assert_success
    run $TDSKT application $APP_ID validate entry common extraparms "dummy parm" "dummy"
    assert_output --partial "Value must use only alphanumerical characters and the underscore"
    run $TDSKT application $APP_ID validate entry common extraparms "dummy" "[ bla:ciao }"
    assert_output --partial "YAML parsing error"
    assert_failure 1
}

@test "ide-backend: validate extraparms - auto_remove" {
    validate_boolean_parm "extraparms"  "auto_remove"
}

@test "ide-backend: validate extraparms - command" {
    validate_string_or_list_parm "extraparms"  "command" "/bin/bash -c" "[ \"/bin/bash\", \"-c\"]"
}

@test "ide-backend: validate extraparms - blkio_weight_device" {
    check_valid_value "extraparms"  "blkio_weight_device" "{ Path: \"/dev/sda\", Weight: 50 }"
    check_invalid_yaml_value "extraparms"  "blkio_weight_device" "{ Path: \"/dev/sda\"}"
    check_invalid_yaml_value "extraparms"  "blkio_weight_device" "{ Path: \"/dev/sda\", Weight: 2500 }"
    check_invalid_yaml_value "extraparms"  "blkio_weight_device" "[ 1, 2, 3 ]"
}

@test "ide-backend: validate extraparms - blkio_weight" {
    check_valid_value "extraparms"  "blkio_weight" "50"
    check_invalid_yaml_value "extraparms"  "blkio_weight" "blablabla"
    check_invalid_yaml_value "extraparms"  "blkio_weight" "999999"
}

@test "ide-backend: validate extraparms - cap_add" {
    validate_string_list_parm "extraparms"  "cap_add" "[ \"SYS_ADMIN\", \"MKNOD\" ]" "[ \"SYS_ADMIN\" ]"
}

@test "ide-backend: validate extraparms - cap_drop" {
    validate_string_list_parm "extraparms"  "cap_drop" "[ \"SYS_ADMIN\", \"MKNOD\" ]" "[ \"SYS_ADMIN\" ]"
}

@test "ide-backend: validate extraparms - group_parent" {
    validate_string_parm "extraparms"  "cgroup_parent" "dummy"
}

@test "ide-backend: validate extraparms - cpu_period" {
    validate_integer_parm "extraparms"  "cpu_period"
}

@test "ide-backend: validate extraparms - cpu_quota" {
    validate_integer_parm "extraparms"  "cpu_quota"
}

@test "ide-backend: validate extraparms - cpu_rt_period" {
    validate_integer_parm "extraparms"  "cpu_rt_period"
}

@test "ide-backend: validate extraparms - cpu_rt_quota" {
    validate_integer_parm "extraparms"  "cpu_rt_quota"
}

@test "ide-backend: validate extraparms - cpu_shares" {
    validate_integer_parm "extraparms"  "cpu_shares"
}

@test "ide-backend: validate extraparms - cpuset_cpus" {
    validate_string_parm "extraparms"  "cpuset_cpus" "0-3"
}

@test "ide-backend: validate extraparms - detach" {
    validate_boolean_parm "extraparms"  "detach"
}

@test "ide-backend: validate extraparms - device_cgroup_rules" {
    validate_string_list_parm "extraparms"  "device_cgroup_rules" "[ \"c 1:3 mr\", \"a 7:* rmw\" ]" "[ \"c 1:3 mr\"]"
}

@test "ide-backend: validate extraparms - device_read_bps" {
    check_valid_value "extraparms"  "device_read_bps" "[ { Path: /dev/sdc, Rate: 12000000 }, { Path: /dev/sda, Rate: 1000000 } ]"
    check_invalid_yaml_value "extraparms"  "device_read_bps" "[ { Path: /dev/sdb, Rate: 12mb } ]"
    check_invalid_yaml_value "extraparms"  "device_read_bps" "[ { Path: /dev/sdc } ]"
    check_invalid_yaml_value "extraparms"  "device_read_bps" "[ { Path: /dev/sdc, Rate: blablabla } ]"
}

@test "ide-backend: validate extraparms - device_read_iops" {
    check_valid_value "extraparms"  "device_read_iops" "[ { Path: /dev/sdc, Rate: 12000000 }, { Path: /dev/sda, Rate: 1000000 } ]"
    check_invalid_yaml_value "extraparms"  "device_read_iops" "[ { Path: /dev/sdb, Rate: 12mb } ]"
    check_invalid_yaml_value "extraparms"  "device_read_iops" "[ { Path: /dev/sdc } ]"
    check_invalid_yaml_value "extraparms"  "device_read_iops" "[ { Path: /dev/sdc, Rate: blablabla } ]"
}

@test "ide-backend: validate extraparms - device_write_bps" {
    check_valid_value "extraparms"  "device_write_bps" "[ { Path: /dev/sdc, Rate: 12000000 }, { Path: /dev/sda, Rate: 1000000 } ]"
    check_invalid_yaml_value "extraparms"  "device_write_bps" "[ { Path: /dev/sdb, Rate: 12mb } ]"
    check_invalid_yaml_value "extraparms"  "device_write_bps" "[ { Path: /dev/sdc } ]"
    check_invalid_yaml_value "extraparms"  "device_write_bps" "[ { Path: /dev/sdc, Rate: blablabla } ]"
}

@test "ide-backend: validate extraparms - device_write_iops" {
    check_valid_value "extraparms"  "device_write_iops" "[ { Path: /dev/sdc, Rate: 12000000 }, { Path: /dev/sda, Rate: 1000000 } ]"
    check_invalid_yaml_value "extraparms"  "device_write_iops" "[ { Path: /dev/sdb, Rate: 12mb } ]"
    check_invalid_yaml_value "extraparms"  "device_write_iops" "[ { Path: /dev/sdc } ]"
    check_invalid_yaml_value "extraparms"  "device_write_iops" "[ { Path: /dev/sdc, Rate: blablabla } ]"
}

@test "ide-backend: validate extraparms - devices" {
    validate_string_list_parm "extraparms"  "devices" "[ \"/dev/sda:/dev/xvda:rwm\", \"/dev/sdb:/dev/xvdb:rwm\" ]" "[ \"/dev/sda:/dev/xvda:rwm\"]"
}

@test "ide-backend: validate extraparms - dns" {
    validate_string_or_list_parm "extraparms"  "dns" "[ 192.168.1.1, 8.8.8.8 ]" "8.8.8.8"
}

@test "ide-backend: validate extraparms - dns_search" {
    validate_string_or_list_parm "extraparms"  "dns" "[ example.com, example1.com ]" "example.com"
}

@test "ide-backend: validate extraparms - domainname" {
    validate_string_parm "extraparms"  "domainname" "example.com"
}

@test "ide-backend: validate extraparms - entrypoint" {
    validate_string_or_list_parm "extraparms"  "entrypoint" "/bin/sh" "[ /bin/sh, -c]"
}

@test "ide-backend: validate extraparms - env_file" {
    validate_string_or_list_parm "extraparms"  "env_file" ".env" "[ ./a.env, ./b.env ]"
}

@test "ide-backend: validate extraparms - environment" {
    validate_list_or_dict_parm "extraparms"  "environment" "{ RACK_ENV: development, SHOW:  \"true\", USER_INPUT: }" "[ RACK_ENV=development, SHOW=true, USER_INPUT ]"
}

@test "ide-backend: validate extraparms - extra_hosts" {
    validate_list_or_dict_parm "extraparms"  "extra_hosts" "[ \"somehost:162.242.195.82\", \"otherhost:50.31.209.229\" ]" "{ somehost:162.242.195.82, otherhost:50.31.209.229}"
}

@test "ide-backend: validate extraparms - group_add" {
    check_valid_value "extraparms"  "group_add" "[ mail ]"
    check_valid_value "extraparms"  "group_add" "[ mail, adm, sudo ]"
    check_invalid_yaml_value "extraparms"  "group_add" "[ 123 ]"
    check_invalid_yaml_value "extraparms"  "group_add" "mail"
}

@test "ide-backend: validate extraparms - healthcheck" {
    check_valid_value "extraparms"  "healthcheck" "{ test: [\"CMD\", \"curl\", \"-f\", \"http://localhost\"], interval: 1m30s, timeout: 10s, retries: 3, start_period: 40s }"
    check_invalid_yaml_value "extraparms"  "healthcheck" "{ test: 123, interval: 1m30s, timeout: 10s, retries: 3, start_period: 40s }"
    check_invalid_yaml_value "extraparms"  "healthcheck" "dummy"
}

@test "ide-backend: validate extraparms - hostname" {
    validate_string_parm "extraparms"  "hostname" "blabla"
}

@test "ide-backend: validate extraparms - init" {
    validate_boolean_parm "extraparms"  "init"
}

@test "ide-backend: validate extraparms - init_path" {
    validate_string_parm "extraparms"  "init_path" "/usr/local/bin/init"
}

@test "ide-backend: validate extraparms - ipc_mode" {
    validate_string_parm "extraparms"  "ipc_mode" "shareable"
}

@test "ide-backend: validate extraparms - isolation" {
    validate_string_parm "extraparms"  "isolation" "hyperv"
}

@test "ide-backend: validate extraparms - kernel_memory" {
    validate_string_or_int_parm "extraparms"  "kernel_memory" "512m" "33554432"
}

@test "ide-backend: validate extraparms - labels" {
    validate_list_or_dict_parm "extraparms"  "labels" "{ key1: value1, key2: value2 }" "[ key1=value1, key2=value2 ]"
}

@test "ide-backend: validate extraparms - log_config" {
    check_valid_value "extraparms"  "log_config" "{ Type: \"json-file\", Config: {\"labels\": \"production_status,geo\", \"max-size\": \"1g\"}}"
    check_invalid_yaml_value "extraparms"  "log_config" "blablabla"
}

@test "ide-backend: validate extraparms - mac_address" {
    validate_string_parm "extraparms"  "mac_address" "01:02:03:04:05:06"
}

@test "ide-backend: validate extraparms - mem_limit" {
    check_valid_value "extraparms"  "mem_limit" "64mb"
    check_valid_value "extraparms"  "mem_limit" "1000000000"
    check_invalid_yaml_value "extraparms"  "mem_limit" "[]"
}

@test "ide-backend: validate extraparms - mem_reservation" {
    check_valid_value "extraparms"  "mem_reservation" "64mb"
    check_valid_value "extraparms"  "mem_reservation" "1000000000"
    check_invalid_yaml_value "extraparms"  "mem_reservation" "[]"
}

@test "ide-backend: validate extraparms - memswap_limit" {
    check_valid_value "extraparms"  "memswap_limit" "64mb"
    check_valid_value "extraparms"  "memswap_limit" "1000000000"
    check_invalid_yaml_value "extraparms"  "memswap_limit" "[]"
}

@test "ide-backend: validate extraparms - mounts" {
    check_valid_value "extraparms"  "mounts" "[ { source: /tmp/a, target: /tmp/b, type: bind, readonly: true, consistency: consistent, propagation: shared, labels: { bla: bla}, driver_config: {}, tmpfs_size: 10Mb, tmpfs_mode: 666 } ]"
    check_invalid_yaml_value "extraparms"  "mounts" "blabla"
    check_invalid_yaml_value "extraparms"  "mounts" "{}"
}

@test "ide-backend: validate extraparms - nano_cpus" {
    validate_integer_parm "extraparms"    "nano_cpus" "15"
}

@test "ide-backend: validate extraparms - network" {
    validate_string_parm "extraparms"    "network" "blabla"
}

@test "ide-backend: validate extraparms - network_disabled" {
    validate_boolean_parm "extraparms"    "network_disabled"
}

@test "ide-backend: validate extraparms - network_mode" {
    validate_string_parm "extraparms"    "network_mode" "host"
}

@test "ide-backend: validate extraparms - oom_kill_disable" {
    validate_boolean_parm "extraparms"    "oom_kill_disable"
}

@test "ide-backend: validate extraparms - oom_score_adj" {
    validate_integer_parm "extraparms"    "oom_score_adj" "15"
}

@test "ide-backend: validate extraparms - pid_mode" {
    validate_string_parm "extraparms"    "pid_mode" "host"
}

@test "ide-backend: validate extraparms - pids_limit" {
    validate_integer_parm "extraparms"    "pids_limit" "9999"
    validate_integer_parm "extraparms"    "pids_limit" "-1"
}

@test "ide-backend: validate extraparms - platform" {
    validate_string_parm "extraparms"    "platform" "linux/arm"
}

@test "ide-backend: validate extraparms - ports" {
    check_valid_value "extraparms"  "ports" "{ 8000:, 8001/tcp:1234, 8002/udp: [999,9999] }"
    check_valid_value "extraparms"  "ports" "{}"
    check_invalid_yaml_value "extraparms"  "ports" "blablabla"
    check_invalid_yaml_value "extraparms"  "ports" "8000"
}

@test "ide-backend: validate extraparms - privileged" {
    validate_boolean_parm "extraparms"    "privileged"
}

@test "ide-backend: validate extraparms - publish_all_ports" {
    validate_boolean_parm "extraparms"    "publish_all_ports"
}

@test "ide-backend: validate extraparms - read_only" {
    validate_boolean_parm "extraparms"    "read_only"
}

@test "ide-backend: validate extraparms - remove" {
    validate_boolean_parm "extraparms"    "remove"
}

@test "ide-backend: validate extraparms - restart_policy" {
    check_valid_value "extraparms"  "restart_policy" "{ Name: \"on-failure\", MaximumRetryCount: 50 }"
    check_invalid_yaml_value "extraparms"  "restart_policy" "blablabla"
    check_invalid_yaml_value "extraparms"  "restart_policy" "8000"
}

@test "ide-backend: validate extraparms - runtime" {
    validate_string_parm "extraparms"   "runtime" "docker"
}

@test "ide-backend: validate extraparms - security_opt" {
    validate_string_list_parm "extraparms"   "security_opt" "[ label:user:USER, label:role:ROLE ]" "[ label:user:USER ]"
}

@test "ide-backend: validate extraparms - shm_size" {
    check_valid_value "extraparms"   "shm_size" "10Mb"
    check_valid_value "extraparms"   "shm_size" "10000000"
    check_invalid_yaml_value "extraparms"   "shm_size" "[]"
}

@test "ide-backend: validate extraparms - stdin_open" {
    validate_boolean_parm "extraparms"    "stdin_open"
}

@test "ide-backend: validate extraparms - stop_signal" {
    validate_string_parm "extraparms"   "stop_signal" "SIGUSR1"
}

@test "ide-backend: validate extraparms - tty" {
    validate_boolean_parm "extraparms"    "tty"
}

@test "ide-backend: validate extraparms - ulimits" {
    check_valid_value "extraparms"  "ulimits" "[{'Name': 'nproc', 'Hard': 0, 'Soft': 1024}]"
    check_invalid_yaml_value "extraparms"  "ulimits" "[{'Name': 'nproc', 'Soft': 1024}]"
    check_invalid_yaml_value "extraparms"  "ulimits" "[ aaa ]"
}

@test "ide-backend: validate extraparms - use_config_proxy" {
    validate_boolean_parm "extraparms"    "use_config_proxy"
}

@test "ide-backend: validate extraparms - user" {
    validate_string_or_int_parm "extraparms"    "user" "torizon" "1000"
}

@test "ide-backend: validate extraparms - userns_mode" {
    validate_string_parm "extraparms"    "userns_mode" "host"
}

@test "ide-backend: validate extraparms - uts_mode" {
    validate_string_parm "extraparms"    "uts_mode" "host"
}

@test "ide-backend: validate extraparms - version" {
    validate_string_parm "extraparms"  "version" "\"1.35\""
}

@test "ide-backend: validate extraparms - volume_driver" {
    validate_string_parm "extraparms"    "volume_driver" "blablabla"
}

@test "ide-backend: validate extraparms - volumes" {
    check_valid_value "extraparms"    "volumes" "{'/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},'/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}}"
    check_valid_value "extraparms"    "volumes" "['/home/user1/:/mnt/vol2','/var/www:/mnt/vol1']"
}

@test "ide-backend: validate extraparms - volumes_from" {
    validate_string_list_parm "extraparms"  "volumes_from" "[ bla, blabla]" "[bla]"
}

@test "ide-backend: validate extraparms - working_dir" {
    validate_string_parm "extraparms"  "working_dir" "/dummy"
}

@test "run platform-specific tests" {
    export PLAT_SCRIPT=$MOSES_PLATFORMS_DIR/$MOSES_CURRENT_PLATFORM/testfiles/validate.bats

    if [ -f "$PLAT_SCRIPT" ]; then
        run_tests $PLAT_SCRIPT
    else
        skip "no platform specific tests defined"
    fi
}
