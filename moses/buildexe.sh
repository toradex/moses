#!/bin/sh

. ../.pyenv/bin/activate
export PYTHONOPTIMIZE=1
pyinstaller -y moses.linux.spec
pyinstaller -y ../cli/tdskt.linux.spec
cp -R dist/tdskt-linux/* dist/moses-linux/
