load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: get device info" {
    if [ -z $MOSES_CURRENT_DEVICE ]; then
        fail "Please configure a platform via $MOSES_CURRENT_DEVICE"
    fi
    run $TDSKT device "$MOSES_CURRENT_DEVICE" info
    assert_success
}

@test "ide-backend: get images" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" images
    assert_success
}

@test "ide-backend: get containers" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" containers
    assert_success
}

@test "ide-backend: get current ip" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" ip
    assert_success
}

@test "ide-backend: get memory info" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" mem
    assert_success
}

@test "ide-backend: get processes" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" ps
    assert_success
}

@test "ide-backend: get storage info" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" storage
    assert_success
}

@test "ide-backend: get ssh key" {
    run $TDSKT device "$MOSES_CURRENT_DEVICE" key
    assert_success
    keypath=$output
    if [ ! - keypath ]; then
        fail "returned key file does not exist."
    fi
}

@test "ide-backend: get image info" {
    readarray -t images < <($TDSKT device "$MOSES_CURRENT_DEVICE" images | tail -n +2 | awk '{ print $1 }')

    for image in  "${images[@]}"
    do
        run $TDSKT device "$MOSES_CURRENT_DEVICE" image $image info
        assert_success
    done
}

@test "ide-backend: get container info" {
    readarray -t containers < <($TDSKT device "$MOSES_CURRENT_DEVICE" containers | tail -n +2 | awk '{ print $1 } | grep -v ":" ')

    for container in  "${containers[@]}"
    do
        run $TDSKT device "$MOSES_CURRENT_DEVICE" container $container info
        assert_success
    done
}

@test "ide-backend: get container memory info" {
    readarray -t containers < <($TDSKT device "$MOSES_CURRENT_DEVICE" containers | tail -n +2 | awk '{ print $1 } | grep -v ":"')

    for container in  "${containers[@]}"
    do
        run $TDSKT device "$MOSES_CURRENT_DEVICE" container $container mem
        assert_success
    done
}

@test "ide-backend: get container processes" {
    readarray -t containers < <($TDSKT device "$MOSES_CURRENT_DEVICE" containers | tail -n +2 | awk '{ print $1 } | grep -v ":"')

    for container in  "${containers[@]}"
    do
        run $TDSKT device "$MOSES_CURRENT_DEVICE" container $container ps
        assert_success
    done
}

@test "ide-backend: get container storage info" {
    readarray -t containers < <($TDSKT device "$MOSES_CURRENT_DEVICE" containers | tail -n +2 | awk '{ print $1 } | grep -v ":"')

    for container in  "${containers[@]}"
    do
        run $TDSKT device "$MOSES_CURRENT_DEVICE" container $container storage
        assert_success
    done
}

@test "ide-backend: sync" {
    dir=$(pwd)/bats

    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        dir=$(wslpath -w "$dir" | sed 's/\\/\\\\/g')
    fi

    run $TDSKT device "$MOSES_CURRENT_DEVICE" sync $dir dummy
    assert_success
}