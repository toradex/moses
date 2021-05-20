load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: get devices list" {
    run $TDSKT devices
    assert_success
}

@test "ide-backend: check that devices list matches device subfolders" {
    returned=$(expr $($TDSKT devices | wc -l) - 1)
    folders=$(ls -1d $MOSES_DEVICES_DIR/* | wc -l)
    assert_equal $folders $returned
}

@test "ide-backend: invalid device-id" {
    run $TDSKT device blablabla info
    assert_failure 2
}

@test "ide-backend: detect device via serial port" {
    if [ -z "$TIE_SERIAL_PORT" ]; then
        skip "No serial port configured (you have to define TIE_SERIAL_PORT)"
    fi
    run $TDSKT detect --uart $TIE_SERIAL_PORT torizon torizon
    assert_success
    deviceid=$(echo "$output" | grep '^id' | awk '{print $2}')
    sleep 60
    run $TDSKT device $deviceid images
    assert_success
}

@test "ide-backend: detect device via serial port (wrong username)" {
    if [ -z "$TIE_SERIAL_PORT" ]; then
        skip "No serial port configured (you have to define TIE_SERIAL_PORT)"
    fi
    run $TDSKT detect --uart $TIE_SERIAL_PORT blabla blabla
    assert_output --partial "Login failed"
    assert_failure 38
}

@test "ide-backend: detect device via serial port (wrong password)" {
    if [ -z "$TIE_SERIAL_PORT" ]; then
        skip "No serial port configured (you have to define TIE_SERIAL_PORT)"
    fi
    run $TDSKT detect --uart $TIE_SERIAL_PORT torizon blabla
    assert_output --partial "Login failed"
    assert_failure 38
}

@test "ide-backend: detect device via serial port (invalid port)" {
    run $TDSKT detect --uart /dev/ttyUSB999 torizon torizon
    assert_output --partial "Serial port error"
    assert_failure 36
}

@test "ide-backend: detect device via network" {
    if [ -z "$TIE_NETWORK_DEVICE" ]; then
        skip "No device address configured (you have to define TIE_NETWORK_DEVICE)"
    fi
    run $TDSKT detect --network $TIE_NETWORK_DEVICE torizon torizon
    assert_success
    deviceid=$(echo "$output" | grep '^id' | awk '{print $2}')
    sleep 60
    run $TDSKT device $deviceid images
    assert_success
}

@test "ide-backend: detect device via network (wrong username)" {
    if [ -z "$TIE_NETWORK_DEVICE" ]; then
        skip "No device address configured (you have to define TIE_NETWORK_DEVICE)"
    fi
    run $TDSKT detect --network $TIE_NETWORK_DEVICE blabla torizon
    assert_output --partial "Authentication failed"
    assert_failure 33
}

@test "ide-backend: detect device via network (wrong password)" {
    if [ -z "$TIE_NETWORK_DEVICE" ]; then
        skip "No device address configured (you have to define TIE_NETWORK_DEVICE)"
    fi
    run $TDSKT detect --network $TIE_NETWORK_DEVICE torizon blabla
    assert_output --partial "Authentication failed"
    assert_failure 33
}

@test "ide-backend: detect device via network (invalid name)" {
    run $TDSKT detect --network blablabla  torizon torizon
    assert_failure
}
