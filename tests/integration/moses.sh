export MOSES_DIR=$TIE_MOSES_DIR
export TIE_ON_WINDOWS="0"

MOSES_EXE="moses"
MOSES_PORT=$TIE_MOSES_PORT
MOSES_DEBUG=""

TDSKT_EXE="tdskt"

export MOSES_DEVICES_DIR=""

if [ ! -z "$WSL_DISTRO_NAME" ]; then
    TIE_ON_WINDOWS="1"
    MOSES_EXE=$MOSES_EXE.exe
    TDSKT_EXE=$TDSKT_EXE.exe
    if [ -z "$MOSES_PATH" ]; then
        MOSES_DIR=../../moses/dist/moses-windows
    fi
    MOSES_DEVICES_DIR=$(wslpath $(wslvar USERPROFILE)\\.moses\\devices)
else
    if [ -z "$MOSES_PATH" ]; then
        MOSES_DIR=../../moses/dist/moses-linux
    fi
    MOSES_DEVICES_DIR=$HOME/.moses/devices
fi

if [ -z "$MOSES_PORT" ]; then
    MOSES_PORT=5000
fi

if [ ! -z "$TIE_MOSES_DEBUG" ]; then
    MOSES_DEBUG=--debug
fi

export TDSKT=$(realpath $MOSES_DIR/$TDSKT_EXE)
export MOSES_PID=""
export MOSES_PLATFORMS_DIR=$(realpath $MOSES_DIR/platforms)
export MOSES_EULAS_DIR=$(realpath $MOSES_DIR/eulas)

start_moses() {
    MOSES_LOG_FILE_PATH=$MOSES_LOG_FILE
    touch $MOSES_LOG_FILE_PATH
    if [ "$TIE_ON_WINDOWS" == "1" ]; then
        MOSES_LOG_FILE_PATH=$(wslpath -a -w $MOSES_LOG_FILE)
    fi
    cd $MOSES_DIR
    ./$MOSES_EXE --port $MOSES_PORT $MOSES_DEBUG --logfile=$MOSES_LOG_FILE_PATH > /dev/null 2>&1 &
    MOSES_PID=$!
    cd - > /dev/null
}

check_moses() {
    if ! ps -p $MOSES_PID > /dev/null 2>&1; then
        return 1
    fi
    return 0
}

stop_moses() {
    if ! check_moses; then
        return 0
    fi

    if [ ! -z $MOSES_PID ]; then
        kill $MOSES_PID > /dev/null 2>&1
    fi
}
