load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: create application (invalid platform)" {
    run $TDSKT create arm33v7-debian-python3_buster $TEMP_DIR
    assert_failure 2
}

@test "ide-backend: create application (invalid folder)" {
    run $TDSKT create arm32v7-debian-python3_buster /bla/bla/bla
    assert_failure 40
}

@test "ide-backend: application info (invalid format)" {
    run $TDSKT application blablabla info
    assert_failure 255
}

@test "ide-backend: application info (invalid id)" {
    run $TDSKT application aabbccdd-1234-1234-1234-123456789abc info
    assert_failure 2
}

@test "ide-backend: application build (invalid application id format)" {
    run $TDSKT application blablabla build debug
    assert_failure 255
}

@test "ide-backend: application build (invalid application id)" {
    run $TDSKT application aabbccdd-1234-1234-1234-123456789abc build debug
    assert_failure 2
}

