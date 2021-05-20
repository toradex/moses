load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: pull containers with progress" {
    run $TDSKT -p pull
    assert_success
}

@test "ide-backend: pull containers" {
    run $TDSKT pull
    assert_success
}
