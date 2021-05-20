load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$MOSES_CURRENT_APPLICATION_FOLDER" | sed 's/\\/\\\\/g')
    fi
}

@test "ide-backend: load sample" {
    run $TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER
    assert_success
}

@test "ide-backend: sample info" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')
    run $TDSKT application $application info
    assert_success
}

@test "ide-backend: sample get private key" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application key
    assert_success
    keypath=$output
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        keypath=$(echo $output | tr -d '\r')
        keypath=$(wslpath $keypath)
    fi
    if [ ! -f "$keypath" ]; then
        fail "Key file not found."
    fi
}

check_sdk_support() {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    sdk=$($TDSKT application $application info | grep -A 2 "sdkimagetags" | awk '{print $NF}')
    sdk=$(echo "$sdk" | grep --invert-match --word-regexp "debug" || true)
    sdk=$(echo "$sdk" | grep --invert-match --word-regexp "release" || true)
    if [ -z "$sdk" ]; then
        return 0
    else
        return 1
    fi
}

@test "ide-backend: sample get docker command line for debug version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application cmdline debug
    assert_success
}

@test "°ide-backend: sample get docker command line for release version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application cmdline release
    assert_success
}

@test "°ide-backend: sample get docker compose file for debug version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application composefile debug
    assert_success
    dockercomposefile="$TIE_TEMP_DIR/$application-debug-docker-compose.yml"
    printf "%s\n" "${lines[@]}" >"$dockercomposefile"
    run docker-compose -f "$dockercomposefile" config -q
    assert_success

    if [ "$status" == 0 ]; then
        rm "$dockercomposefile"
    fi
}

@test "°ide-backend: sample get docker compose file for release version" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application composefile debug
    assert_success
    dockercomposefile="$TIE_TEMP_DIR/$application-release-debug-docker-compose.yml"
    printf "%s\n" "${lines[@]}" >"$dockercomposefile"
    run docker-compose -f "$dockercomposefile" config -q
    assert_success
    if [ "$status" == 0 ]; then
        rm "$dockercomposefile"
    fi
}

@test "°ide-backend: sample build debug with progress" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application build debug
    assert_success
}

@test "°ide-backend: sample build release with progress" {
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application build release
    assert_success
}

@test "°ide-backend: sample update sdk debug with progress" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application updatesdk debug
    assert_success
}

@test "°ide-backend: sample run sdk debug" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application runsdk debug
    assert_success
}

@test "°ide-backend: sample update sdk release with progress" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT -p application $application updatesdk release
    assert_success
}

@test "°ide-backend: sample run sdk release" {
    if check_sdk_support ; then
        skip "Application has no SDK."
    fi
    application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

    run $TDSKT application $application runsdk release
    assert_success
}
