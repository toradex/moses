load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: query platform information" {
    if [ -z $MOSES_CURRENT_PLATFORM ]; then
        fail "Please configure a platform via $MOSES_CURRENT_PLATFORM"
    fi
    run $TDSKT platform $MOSES_CURRENT_PLATFORM info
    assert_success
}
       
@test "ide-backend: platform-compatible devices" {
    run $TDSKT platform $MOSES_CURRENT_PLATFORM compatible
    assert_success
}   

