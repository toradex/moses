#!/bin/sh

application=$($TDSKT load $MOSES_CURRENT_APPLICATION_FOLDER)

$TDSKT application $application setprop props.appname test common
$TDSKT application $application setprop props.main main.py common
