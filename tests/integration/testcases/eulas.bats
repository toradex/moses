load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: get eulas list" {
    run $TDSKT eulas
    assert_success
}

@test "ide-backend: check that eulas list matches eulas subfolders" {
    returned=$(expr $($TDSKT eulas | wc -l) - 1)
    folders=$(ls -1d $MOSES_EULAS_DIR/* | wc -l)
    assert_equal $folders $returned
}

@test "ide-backend: get eula info" {
    run $TDSKT eula nxp-la-opt-v5 info
    assert_success
}

@test "ide-backend: invalid eula-id (non-existing)" {
    run $TDSKT eula blablabla info
    assert_failure 2
}

@test "ide-backend: accept eula" {
    run $TDSKT eula nxp-la-opt-v5 setprop accepted true
    assert_success
}

