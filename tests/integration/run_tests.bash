# BATS command
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
