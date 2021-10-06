load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'
source '../testcases/validation_functions.bash'

@test "ide-backend: validate extrapackages property" {
    validate_debian_packages_property "extrapackages"
}
