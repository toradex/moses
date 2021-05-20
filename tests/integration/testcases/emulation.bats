load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: enable emulation" {
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        skip "Emulation should not be enabled on Windows machines."
    fi
    run $TDSKT enableemulation
    assert_success
}
