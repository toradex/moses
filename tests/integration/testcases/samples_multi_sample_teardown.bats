load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        MOSES_CURRENT_APPLICATION_FOLDER=$(wslpath -w "$MOSES_CURRENT_APPLICATION_FOLDER" | sed 's/\\/\\\\/g')
    fi
}

@test "ide-backend: teardown" {
    skip "this is used to remove local containers after testing"
}

teardown_file() {
   application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER | tr -d '\r')

   run docker stop $(docker container ls --format '{{.Names}}' | grep --fixed-strings $application)
   run docker rm $(docker container ls -a --format '{{.Names}}' | grep --fixed-strings $application)
   run docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings $application)
}
