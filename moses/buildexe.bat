call ..\.pyenv\scripts\activate.bat
set PYTHONOPTIMIZE=1
pyinstaller -y moses.windows.spec
pyinstaller -y ../cli/tdskt.windows.spec
xcopy /sy dist\tdskt-windows dist\moses-windows
