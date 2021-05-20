#!/bin/sh

application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER)

$TDSKT application $application setprop appname test common
$TDSKT application $application setprop main main.py common
