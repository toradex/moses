load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    export MOSES_CURRENT_APPLICATION_FOLDER=$TIE_TEMP_DIR/appconfig_0
    export APP_TEMP_FOLDER=$TIE_TEMP_DIR
    export MOSES_CURRENT_DEVICE=$TIE_DEVICE
    export MOSES_CURRENT_PLATFORM=$TIE_PLATFORM

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        APP_TEMP_FOLDER=$(wslpath -w $TIE_TEMP_DIR | sed 's/\\/\\\\/g')
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$TIE_TEMP_DIR/appconfig_0" | sed 's/\\/\\\\/g')
    fi
}

@test "ide-backend: create application" {

    if [ -z "$MOSES_CURRENT_PLATFORM" ]; then
        fail "please define TIE_PLATFORM."
    fi

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

@test "ide-backend: application build release with progress" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application build release
    assert_success
}

@test "ide-backend: deploy release application" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application deploy release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: deploy release application with progress" {

    if [ -z "$MOSES_CURRENT_DEVICE"]; then
        skip "no device selected"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application deploy release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run release application with progress" {

    if [ -z "$MOSES_CURRENT_DEVICE"]; then
        skip "no device selected"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application run release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: get release container" {

    if [ -z "$MOSES_CURRENT_DEVICE"]; then
        skip "no device selected"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container release $MOSES_CURRENT_DEVICE
    assert_success
}

teardown_file() {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run docker stop $(docker container ls --format '{{.Names}}' | grep --fixed-strings "$application")
    run docker rm $(docker container ls -a --format '{{.Names}}' | grep --fixed-strings "$application")
    run docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings "$application")

    keyfile=$($TDSKT device $MOSES_CURRENT_DEVICE key)
    ip=$($TDSKT device $MOSES_CURRENT_DEVICE ip)

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        keyfile=$(wslpath $keyfile)
    fi

    run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile /dev/null torizon@$ip "docker stop $(docker container ls --format '{{.Names}}' | grep --fixed-strings $application)"
    run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile /dev/null torizon@$ip "docker rm $(docker container ls -a --format '{{.Names}}' | grep --fixed-strings $application)"
    run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile /dev/null torizon@$ip "docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings $application)"
}