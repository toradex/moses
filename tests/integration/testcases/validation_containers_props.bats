load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'
source '../testcases/validation_functions.bash'

@test "ide-backend: validate expose property" {
    validate_container_template_property "expose"
}

@test "ide-backend: validate arg property" {
    validate_container_template_property "arg"
}

@test "ide-backend: validate env property" {
    validate_container_template_property "env"
}

@test "ide-backend: validate preinstallcommands property" {
    validate_container_template_property "preinstallcommands"
}

@test "ide-backend: validate buildfiles property" {
    validate_container_template_property "buildfiles"
}

@test "ide-backend: validate buildcommands property" {
    validate_container_template_property "buildcommands"
}

@test "ide-backend: validate targetfiles property" {
    validate_container_template_property "targetfiles"
}

@test "ide-backend: validate targetcommands property" {
    validate_container_template_property "targetcommands"
}

@test "ide-backend: validate appname property" {
    check_valid_value "props" "appname" "myapp"
    check_warning "props" "appname" "user name"
    check_warning "props" "appname" "user@@@name"
}

@test "ide-backend: validate username property" {
    check_valid_value "props" "username" "torizon"
    check_warning "props" "username" "1234"
    check_warning "props" "username" "user name"
    check_warning "props" "username" "user@@@name"
}

@test "ide-backend: validate exename property" {
    check_valid_value "props" "exename" "bin/myexe"
    check_valid_value "props" "exename" "myexe"
    check_warning "props" "exename" "/bin/myexe"
    check_warning "props" "exename" "exe name"
    check_warning "props" "exename" "exe@@@name"
}