load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

source '../run_tests.bash'

@test "ide-backend: validate platform-specific properties" {
    run_tests "$TESTCASES_DIR/validation_containers_props.bats"
    run_tests "$TESTCASES_DIR/validation_debian_containers_props.bats"
    run_tests "$TESTCASES_DIR/validation_debian_sdk_props.bats"
}
