load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    export MOSES_CURRENT_APPLICATION_FOLDER=$TIE_TEMP_DIR/appconfig_0
    export APP_TEMP_FOLDER=$TIE_TEMP_DIR
    export MOSES_DEV_COMPATIBLE=0

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        APP_TEMP_FOLDER=$(wslpath -w $TIE_TEMP_DIR | sed 's/\\/\\\\/g')
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$TIE_TEMP_DIR/appconfig_0" | sed 's/\\/\\\\/g')
    fi

    run $TDSKT platform $MOSES_CURRENT_PLATFORM compatible

    if [[ "$output" == *"$MOSES_CURRENT_DEVICE"* ]]; then
        MOSES_DEV_COMPATIBLE=1
    fi
}

is_container_running() {
    sleep 30

    state="created"
    while [ "$state" == "created" ]
    do
        state=$($TDSKT -p application $1 container $2 $MOSES_CURRENT_DEVICE | grep state | grep status | awk '{ print $3 }')
    done

    case  $state in
        running)
            return 0
            ;;
        paused)
            echo "container paused."
            return 1
            ;;
        restarting)
            echo "container restarting."
            return 2
            ;;
        removing)
            echo "container removing."
            return 3
            ;;
        exited)
            echo "container exited."
            echo $($TDSKT -p application $1 logs $2 $MOSES_CURRENT_DEVICE)
            return 4
            ;;
        dead)
            echo "container dead."
            return 5
            ;;
        *)
            echo "container state: $state"
            return 6
            ;;
    esac
}

@test "ide-backend: deploy debug application" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application deploy debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: deploy debug application with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application deploy debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run debug application with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application run debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: check that debug container is running" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    # first check is used to verify that container exist, following one to verify that
    # it's in running state
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container debug $MOSES_CURRENT_DEVICE
    assert_success
    if ! is_container_running $application debug; then
        fail "container is not running."
    fi
}

@test "ide-backend: run debug application" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application run debug $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: check that debug container is running after restart" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container debug $MOSES_CURRENT_DEVICE
    assert_success
    if ! is_container_running $application debug; then
        fail "container is not running."
    fi
}

@test "ide-backend: stop debug application" {

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

@test "ide-backend: check that debug container has been removed" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    run $TDSKT -p application $application container debug $MOSES_CURRENT_DEVICE
    assert_failure 2
}

@test "ide-backend: deploy release application" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application deploy release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: deploy release application with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application deploy release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: run release application with progress" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application run release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: check that release container is running" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container release $MOSES_CURRENT_DEVICE
    assert_success
    if ! is_container_running $application release; then
        fail "container is not running."
    fi
}

@test "ide-backend: run release application" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application run release $MOSES_CURRENT_DEVICE
    assert_success
}

@test "ide-backend: check that release container is running after restart" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container release $MOSES_CURRENT_DEVICE
    assert_success
    if ! is_container_running $application release; then
        fail "container is not running."
    fi
}

@test "ide-backend: stop release application" {

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

@test "ide-backend: check that release container has been removed" {

    if [ "$MOSES_DEV_COMPATIBLE" -eq "0" ]; then
        skip "device is not compatible with current platform"
    fi

    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT -p application $application container release $MOSES_CURRENT_DEVICE
    assert_failure 2
}

teardown_file() {
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
}