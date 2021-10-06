check_valid_value() {
    run $TDSKT application $APP_ID validate entry common $1 $2 "$3"
    assert_success
    run $TDSKT application $APP_ID validate entry debug $1 $2 "$3"
    assert_success
    run $TDSKT application $APP_ID validate entry release $1 $2 "$3"
    assert_success
}

check_warning() {
    run $TDSKT application $APP_ID validate entry common $1 $2 "$3"
    assert_failure 2
    run $TDSKT application $APP_ID validate entry debug $1 $2 "$3"
    assert_failure 2
    run $TDSKT application $APP_ID validate entry release $1 $2 "$3"
    assert_failure 2
}

check_error() {
    run $TDSKT application $APP_ID validate entry common $1 $2 "$3"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry debug $1 $2 "$3"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry release $1 $2 "$3"
    assert_failure 1
}


check_invalid_yaml_value() {
    run $TDSKT application $APP_ID validate entry common $1 $2 "$3"
    assert_output --partial "YAML validation error"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry debug $1 $2 "$3"
    assert_output --partial "YAML validation error"
    assert_failure 1
    run $TDSKT application $APP_ID validate entry release $1 $2 "$3"
    assert_output --partial "YAML validation error"
    assert_failure 1
}

function validate_boolean_parm {
    check_valid_value $1 $2 "true"
    check_valid_value $1 $2 "false"
    check_invalid_yaml_value $1 $2 "blablabla"
}

function validate_string_or_list_parm {
    check_valid_value $1 $2 "$3"
    check_valid_value $1 $2 "$4"
    check_invalid_yaml_value $1 $2 "{  dummy: dummy }"
}

function validate_string_list_parm {
    check_valid_value $1 $2 "$3"
    check_valid_value $1 $2 "$4"
    check_invalid_yaml_value $1 $2 "[ \"string\", 123 ]"
    check_invalid_yaml_value $1 $2 "dummy"
}

function validate_string_parm {
    check_valid_value $1 $2 "$3"
    check_invalid_yaml_value $1 $2 "[ \"dummy\", 123 ]"
    check_invalid_yaml_value $1 $2 "123"
}

function validate_integer_parm {
    check_valid_value $1 $2 "0"
    check_valid_value $1 $2 "999"
    check_invalid_yaml_value $1 $2 "blablabla"
}

function validate_list_or_dict_parm {
    check_valid_value $1 $2 "$3"
    check_valid_value $1 $2 "$4"
    check_invalid_yaml_value $1 $2 "[ \"string\", 123 ]"
    check_invalid_yaml_value $1 $2 "dummy"
}

function validate_string_or_int_parm {
    check_valid_value $1 $2 "$3"
    check_valid_value $1 $2 "$4"
    check_invalid_yaml_value $1 $2 "[ \"string\", 123 ]"
    check_invalid_yaml_value $1 $2 "{ \"string\": 123 }"
}

validate_container_template_property() {
    check_valid_value "props" $1 "EXPOSE 80/tcp"
    check_valid_value "props" $1 "expose 80/tcp"
    check_valid_value "props" $1 "EXPOSE 80/tcp\nexpose 80/udp"
    check_valid_value "props" $1 "# just a comment"
    check_valid_value "props" $1 "ARG value"
    check_valid_value "props" $1 "ARG username=torizon"
    check_valid_value "props" $1 "ARG username=torizon"
    check_valid_value "props" $1 "ENV username=torizon"
    check_valid_value "props" $1 "RUN /bin/echo \"hello\""
    check_valid_value "props" $1 "RUN [/bin/echo,\"hello\"]"
    check_valid_value "props" $1 "CMD [/bin/python,\"myapp.py\"]"
    check_valid_value "props" $1 "ENTRYPOINT [/bin/bash]"
    check_valid_value "props" $1 "LABEL multi.label1=\"value1\" multi.label2=\"value2\" other=\"value3\""
    check_valid_value "props" $1 "ADD hom\* /mydir/"
    check_valid_value "props" $1 "ADD hom\?.txt /mydir/"
    check_valid_value "props" $1 "COPY test.txt relativeDir/"
    check_valid_value "props" $1 "VOLUME /myvol"
    check_valid_value "props" $1 "WORKDIR /home"
    check_valid_value "props" $1 "WORKDIR /home\nVOLUME /myvol"
    check_warning "props" $1 "bla bla bla"
    check_warning "props" $1 "[ dummy, 123 ]"
}

validate_debian_packages_property() {
    check_valid_value "props" $1 "python3-minimal"
    check_valid_value "props" $1 "python3-minimal python3-pip"
    check_valid_value "props" $1 "python3-minimal python3-pip zlib-dev:arm64"
    check_warning "props" $1 "python3-minimal python3-pip zlib-dev:z80"
    check_warning "props" $1 "PYTHON3-minimal python3-pip zlib-dev"
    check_warning "props" $1 "python3-minimal python3@@@-pip zlib-dev"
}
