load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

@test "ide-backend: samples" {
    if [ ! -d "$TIE_SAMPLES_DIR" ]; then
        fail "samples dir ($TIE_SAMPLES_DIR) does not exist"
    fi
}