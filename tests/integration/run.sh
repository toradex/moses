#!/bin/bash

BASE_DIR=$PWD
WORK_DIR=$PWD/workdir
TESTCASES_DIR=$BASE_DIR/testcases

REPORT_DIR=$WORK_DIR/reports
REPORT_FILE=$REPORT_DIR/$(date +"%Y%02m%02d%H%M%S").log
MOSES_LOG_FILE=$REPORT_DIR/$(date +"%Y%02m%02d%H%M%S").moses.log

TESTCASES="\
$TESTCASES_DIR/emulation.bats \
$TESTCASES_DIR/backend.bats \
$TESTCASES_DIR/eulas.bats \
$TESTCASES_DIR/pull.bats \
$TESTCASES_DIR/platforms.bats \
$TESTCASES_DIR/devices.bats \
$TESTCASES_DIR/applications.bats \
$TESTCASES_DIR/samples.bats \
"

# BATS command
BATS_BIN="./bats/bats-core/bin/bats"
BATS_ERRORS_COUNT=0

set -o pipefail

run_tests() {
    if [ "$TIE_REPORT" = "1" ]; then
        $BATS_BIN --timing $@ 2>&1 | tee -a $REPORT_FILE
    else
        $BATS_BIN --timing $@
    fi
    if [ ! "$?" -eq "0" ]; then
        BATS_ERRORS_COUNT=$(expr $BATS_ERRORS_COUNT + 1)
    fi
}

# test case to run
if [ ! -z "$TIE_TESTCASE" ]; then
    TESTCASES="\
    $TESTCASES_DIR/emulation.bats \
    $TESTCASES_DIR/eulas.bats \
    $TESTCASES_DIR/$TIE_TESTCASE.bats \
    "
fi


# check if setup.sh was sourced.
if [ -z "$TIE_SETUP_LAUNCHED" ]; then
    echo "Error: setup.sh was not sourced. Please execute 'source setup.sh' before running the test cases."
    exit 1
fi

# back-end related functions
. ./moses.sh

# we need this folder to store moses logs
mkdir -p $REPORT_DIR

export TIE_TEMP_DIR=$WORK_DIR/temp
export TIE_EULASPATH=$TIE_TEMP_DIR/eulas
export TIE_SAMPLES_DIR=$BASE_DIR/samples

if [ -z "$TIE_DEBUG_BACKEND" ]; then
    # start backend
    start_moses

    if ! check_moses; then
        echo "Error starting ide-backend."
        cat $MOSES_LOG_FILE
        exit -1
    fi

    MOSES_TIMEOUT=10

    echo "Backend started with PID $MOSES_PID, waiting $MOSES_TIMEOUT'' for initialization."

    # delay to allow backend to process requests in further steps
    sleep $MOSES_TIMEOUT

    if ! check_moses; then
        echo "Error during ide-backend initialization."
        cat $MOSES_LOG_FILE
        exit -1
    fi
fi

# prepare tests
cd $WORK_DIR

rm -fR $TIE_TEMP_DIR
mkdir -p $TIE_TEMP_DIR

mkdir -p $TIE_EULASPATH

run_tests $TESTCASES

if [ ! -z "$TIE_PLATFORM" ]; then
    declare -a MOSES_PLATFORMS_LIST
    MOSES_PLATFORMS_LIST[0]="$TIE_PLATFORM"
else
    readarray -t MOSES_PLATFORMS_LIST < <($TDSKT platforms | tail -n +2 | awk '{ print $1 }')
fi

if [ ! -z "$TIE_DEVICE" ]; then
    if [ "$TIE_DEVICE" == "*" ]; then
        readarray -t MOSES_DEVICES_LIST < <($TDSKT devices | tail -n +2 | awk '{ print $1 }')
    else
        declare -a MOSES_DEVICES_LIST
        MOSES_DEVICES_LIST[0]="$TIE_DEVICE"
    fi
else
    declare -a MOSES_DEVICES_LIST
fi

export MOSES_CURRENT_PLATFORM=""
export MOSES_CURRENT_DEVICE=""

# run per-platform tests
for MOSES_CURRENT_PLATFORM in "${MOSES_PLATFORMS_LIST[@]}"
do
    for test in $TESTCASES
    do
        filename=$(basename -- "$test")
        dir=$(dirname "$test")
        multipath="$dir/${filename%.*}_multi_platform.bats"

        if [ -f "$multipath" ]; then
            echo "# Testing $filename on $MOSES_CURRENT_PLATFORM"
            run_tests $multipath
        fi

        multipath="$dir/${filename%.*}_multi_platform_device.bats"

        if [ -f "$multipath" ]; then
            for MOSES_CURRENT_DEVICE in "${MOSES_DEVICES_LIST[@]}"
            do
                echo "# Testing $filename on $MOSES_CURRENT_PLATFORM / $MOSES_CURRENT_DEVICE"
                run_tests $multipath
            done
        fi

        multipath="$dir/${filename%.*}_multi_platform_teardown.bats"

        if [ -f "$multipath" ]; then
            run_tests $multipath
        fi
    done
done

# run per-device tests
for MOSES_CURRENT_DEVICE in "${MOSES_DEVICES_LIST[@]}"
do
    for test in $TESTCASES
    do
        filename=$(basename -- "$test")
        dir=$(dirname "$test")
        multipath="$dir/${filename%.*}_multi_device.bats"

        if [ -f "$multipath" ]; then
            echo "# Testing $filename on $MOSES_CURRENT_DEVICE"
            run_tests $multipath
        fi
    done

    multipath="$dir/${filename%.*}_multi_device_teardown.bats"

    if [ -f "$multipath" ]; then
        run_tests $multipath
    fi
done

# run tests on samples
readarray -t subfolders < <(find $TIE_SAMPLES_DIR -maxdepth 1 -mindepth 1 -type d)

for subfolder in "${subfolders[@]}"
do
        readarray -t appconfigs < <(find $subfolder -maxdepth 1 -mindepth 1 -type d | grep appconfig_)

        for appconfig in "${appconfigs[@]}"
        do
            export MOSES_CURRENT_APPLICATION_FOLDER=$appconfig
            for test in $TESTCASES
            do
                filename=$(basename -- "$test")
                dir=$(dirname "$test")
                multipath="$dir/${filename%.*}_multi_sample.bats"

                if [ -f "$multipath" ]; then
                    echo "# Testing $filename on $appconfig"
                    run_tests $multipath
                fi

                multipath="$dir/${filename%.*}_multi_sample_device.bats"

                if [ -f "$multipath" ]; then
                    for MOSES_CURRENT_DEVICE in "${MOSES_DEVICES_LIST[@]}"
                    do
                        echo "# Testing $filename on $appconfig and $MOSES_CURRENT_DEVICE"
                        run_tests $multipath
                    done
                fi
            done

            multipath="$dir/${filename%.*}_multi_sample_teardown.bats"

            if [ -f "$multipath" ]; then
                run_tests $multipath
            fi
        done
done

if [ -z "$TIE_DEBUG_BACKEND" ]; then
    stop_moses
    wait
fi

if [ "$TIE_REPORT" = "1" ]; then
    echo "Test report available in $REPORT_FILE"
fi

RETCODE=0

if [ "$BATS_ERRORS_COUNT" -eq "0" ]; then
    echo "Integration test completed successfully"
else
    echo "$BATS_ERRORS_COUNT test(s) failed."
    RETCODE=$BATS_ERRORS_COUNT
fi

cd $BASE_DIR
exit $RETCODE


