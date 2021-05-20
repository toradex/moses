load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: get platforms list" {
    run $TDSKT platforms
    assert_success
}

@test "ide-backend: check that platforms list matches platforms subfolders" {
    # if you disabled a platform, increase this number, otherwise test will fail
    disabled=1
    returned=$(expr $($TDSKT platforms | wc -l) - 1)
    folders=$(ls -1d $MOSES_PLATFORMS_DIR/* | wc -l)
    if [ ! $folders -eq $(expr $returned + $disabled) ]; then
        fail "platforms returned by backend ($(expr $returned + $disabled)) don't match those defined in the platform folder ($folders). Check the number of disabled ones in this test and that all eulas have been accepted."
    fi
}

@test "ide-backend: invalid platform-id (format)" {
    run $TDSKT platform blablabla info
    assert_failure 255
}

@test "ide-backend: invalid platform-id (non-existing)" {
    run $TDSKT platform arm33v7-debian-python3_buster info
    assert_failure 2
}

@test "ide-backend: invalid platform-compatible devices (format)" {
    run $TDSKT platform blablabla compatible
    assert_failure 255
}

@test "ide-backend: invalid platform-compatible devices (non-existing)" {
    run $TDSKT platform arm33v7-debian-python3_buster compatible
    assert_failure 2
}
