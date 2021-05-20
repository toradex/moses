load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: check tdskt" {
    # if this test fails because the output does not match then you probably added some commands,
    # please fix the string below and add tests for the new commands!
    run $TDSKT
    assert_output --partial usage: tdskt [-h] [-p] {devices,device,eulas,platforms,platform,application,detect,create,load,pull,enableemulation,version,dockerversion}
}

@test "ide-backend: check backend version" {
    run $TDSKT version
    assert_success
}

@test "ide-backend: check docker version" {
    run $TDSKT dockerversion
    assert_success
}
