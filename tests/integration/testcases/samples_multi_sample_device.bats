load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    export MOSES_DEV_COMPATIBLE=0

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$MOSES_CURRENT_APPLICATION_FOLDER" | sed 's/\\/\\\\/g')
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    export MOSES_CURRENT_PLATFORM=$($TDSKT application $application info | grep platformid | awk '{ print $2 }')

    run $TDSKT platform $MOSES_CURRENT_PLATFORM compatible

    if [[ "$output" == *"$MOSES_CURRENT_DEVICE"* ]]; then
        MOSES_DEV_COMPATIBLE=1
    fi
}

@test "ide-backend: deploy debug sample with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application deploy debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run debug sample with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application run debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: get debug container" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run debug sample" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application run debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: stop debug sample" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application stop debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: get debug container logs" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application logs debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: deploy release sample with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application deploy release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run release sample with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application run release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: get release container" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run release sample" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application run release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: stop release sample" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application stop release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: get release container logs" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application logs release $MOSES_CURRENT_DEVICE
    assert_success
}

teardown_file() {
    if [ ! "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
        keyfile=$($TDSKT device $MOSES_CURRENT_DEVICE key)
        ip=$($TDSKT device $MOSES_CURRENT_DEVICE ip)

        if [ "$TIE_ON_WINDOWS" == "1" ]; then
            winkeyfile=$(wslpath "$keyfile" | tr -d '\r')
            keyfile="/tmp/$MOSES_CURRENT_DEVICE.rsa"
            cp -f "$winkeyfile" "$keyfile"
            chmod 0600 "$keyfile"
        fi

        run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null torizon@$ip "docker stop \$(docker container ls --format '{{.Names}}' | grep --fixed-strings $application)"
        run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null torizon@$ip "docker rm \$(docker container ls -a --format '{{.Names}}' | grep --fixed-strings $application)"
        run ssh -i "$keyfile" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null torizon@$ip "docker rmi \$(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings $application)"
    fi
}