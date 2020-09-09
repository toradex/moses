call ..\.pyenv\scripts\activate.bat
set PYTHONOPTIMIZE=1
python -m PyInstaller -y moses.windows.spec
python -m PyInstaller -y ../cli/tdskt.windows.spec
xcopy /sy dist\tdskt-windows dist\moses-windows
