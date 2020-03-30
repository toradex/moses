#!/bin/sh

. ../.pyenv/bin/activate
export PYTHONOPTIMIZE=1
pyinstaller -y moses.linux.spec
pyinstaller -y ../cli/tdskt.linux.spec
cp -R dist/tdskt-linux/* dist/moses-linux/
cd dist/moses-linux
rm $(ls -1 lib*.so* | grep -v libffi | grep -v libpython | tr "\n" " ")
cd -
