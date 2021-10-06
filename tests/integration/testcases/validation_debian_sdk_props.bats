load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'
source '../testcases/validation_functions.bash'

@test "ide-backend: validate extrapackages property" {
    validate_debian_packages_property "devpackages"
    validate_debian_packages_property "sdkpackages"
    validate_container_template_property "sdkpreinstallcommands"
    validate_container_template_property "sdkpostinstallcommands"
}
