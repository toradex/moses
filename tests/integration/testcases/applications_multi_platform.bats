load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

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
}

@test "ide-backend: create application" {
    run $TDSKT create $MOSES_CURRENT_PLATFORM $APP_TEMP_FOLDER
    assert_success
    if [ -d $MOSES_PLATFORMS_DIR/$MOSES_CURRENT_PLATFORM/testfiles ]; then
        cp -R $MOSES_PLATFORMS_DIR/$MOSES_CURRENT_PLATFORM/testfiles $TIE_TEMP_DIR/appconfig_0/work
        if [ -f $MOSES_PLATFORMS_DIR/$MOSES_CURRENT_PLATFORM/testfiles/test_setup.sh ]; then
            run $MOSES_PLATFORMS_DIR/$MOSES_CURRENT_PLATFORM/testfiles/test_setup.sh
        fi
    fi

}

@test "ide-backend: load application" {
    run $TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER
    assert_success
}

@test "ide-backend: application info" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application info
    assert_success
}

@test "ide-backend: application get private key" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application key
    assert_success
    keypath=$output
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        keypath=$(echo $output | tr -d '\r')
        keypath=$(wslpath $keypath)
    fi
    if [ ! -f "$keypath" ]; then
        fail "Key file not found."
    fi
}

check_sdk_support() {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    sdk=$($TDSKT application $application info | grep -A 2 "sdkimagetags" | awk '{print $NF}')
    sdk=$(echo "$sdk" | grep --invert-match --word-regexp "debug" || true)
    sdk=$(echo "$sdk" | grep --invert-match --word-regexp "release" || true)
    if [ -z "$sdk" ]; then
        return 0
    else
        return 1
    fi
}

@test "ide-backend: set custom property" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application setprop props.dummy "dummy" common
    assert_success
    run $TDSKT application $application info
    assert_success
    assert_output --partial "'dummy': 'dummy'"
}

@test "ide-backend: set property" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application setprop volumes '{ /tmp: "/tmp" }' common
    assert_success
    run $TDSKT application $application info
    assert_success
    assert_output --partial "volumes            common   {'/tmp': '/tmp'}"
}

@test "ide-backend: clean property" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application setprop volumes '{}' common
    assert_success
    run $TDSKT application $application info
    assert_success
    assert_output --partial "volumes            common   {}"
}

@test "ide-backend: clean custom property" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application setprop props.dummy '' common
    assert_success
    run $TDSKT application $application info
    assert_success
    assert_output --partial "'dummy': ''"
}


@test "ide-backend: application get docker command line for debug version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application cmdline debug
    assert_success
}

@test "ide-backend: application get docker command line for release version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application cmdline release
    assert_success
}

@test "ide-backend: application get docker compose file for debug version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application composefile debug
    assert_success
    dockercomposefile="$TIE_TEMP_DIR/$application-debug-docker-compose.yml"
    printf "%s\n" "${lines[@]}" >"$dockercomposefile"
    run docker-compose -f "$dockercomposefile" config -q
    assert_success

    if [ "$status" == 0 ]; then
        rm "$dockercomposefile"
    fi
}

@test "ide-backend: application get docker compose file for release version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application composefile debug
    assert_success
    dockercomposefile="$TIE_TEMP_DIR/$application-release-debug-docker-compose.yml"
    printf "%s\n" "${lines[@]}" >"$dockercomposefile"
    run docker-compose -f "$dockercomposefile" config -q
    assert_success
    if [ "$status" == 0 ]; then
        rm "$dockercomposefile"
    fi
}

@test "ide-backend: application build debug" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application build debug
    assert_success
}

@test "ide-backend: application build debug with progress" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application build debug
    assert_success
}

@test "ide-backend: application build release" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application build release
    assert_success
}

@test "ide-backend: application build release with progress" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application build release
    assert_success
}

@test "ide-backend: application update sdk debug" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application updatesdk debug
    assert_success
}

@test "ide-backend: application update sdk debug with progress" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application updatesdk debug
    assert_success
}

@test "ide-backend: application run sdk debug" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application runsdk debug
    assert_success
}

@test "ide-backend: application update sdk release" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application updatesdk release
    assert_success
}

@test "ide-backend: application update sdk release with progress" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application updatesdk release
    assert_success
}

@test "ide-backend: application run sdk release" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application runsdk release
    assert_success
}
