# Moses project

This repo contains all the different components related to IDE extensions for [Torizon](https://www.toradex.com/operating-systems/torizon) and devices running Linux and Docker.

This code is licensed under GPLv3, you can find the license file [here](gpl-30.md)

- moses -- is the folder with the back-end service providing most of the features
- cli -- command line interface
- clients -- mostly auto-generated code for the different clients used by integrations
- tests -- tests built using BATS
## IDE-extensions

Currently this backend is used by two IDE extensions:
- [Visual Studio 2019](https://marketplace.visualstudio.com/items?itemName=Toradex.toradex-torizon-ccpp-support)
- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Toradex.torizon)

If you want to use this backend with a different IDE, please [check our API definition](moses/swagger.yaml) and feel free to contact us for additional information, suggestions or discussions about possible implementations.

If you want to collaborate by providing code, documentation etc. please check our [Developer Certificate of Origin](dco.txt).

## Architecture

The backend exposes a REST-based API, by default on port 5000.
You can find some more documentation on [Toradex's developer website](https://developer.toradex.com).
Architecture documentation is still a WIP, but please contact us if you want more details about it.


## Python setup

Both the backend and the cli interface are developed in python.
To be able to run them you have to install the required packages.
Best thing would be setting up a virtual enviroment so this won't be impacted by changes to your global python setup.
You need python 3 (tested with 3.8).
On Windows 10 just type "python3" in a command prompt and the system will allow you to download and install the interpreter.

* if you don't have virtualenv installed, you can install it with pip (if you still have python2 installed you may have to use python3 instead of just python):

```
python -m pip install virtualenv
```

* create virtual enviroment in the root folder of the repo:

```
python -m virtualenv .pyenv
```

* activate your new virtual environment:

Linux:

```
. ./.pyenv/bin/activate
```

Windows:

```
.\.pyenv\Scripts\activate
```

* install required packages:

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

You also need to add the python client to the environment to be able to run/build the command line tool:

```
cd clients/python
python -m setup install
```

* now you can run moses.py (backend) or the command-line interface tdskt.py. Remember to activate your virtual enviroment every time you run those tools.
* if you use Visual Studio Code for python development you can just add the following entry to your .vscode/.settings file to have it automatically activated on debug and used for auto-completition etc.

Linux:

```
"python.pythonPath": "../../.pyenv/bin/python"
```

Windows:

```
"python.pythonPath": "..\\.pyenv\\Scripts\\python.exe"
```

## Build executable for the backend

You can cd into the moses subfolder and run the buildexe.bat or buildexe.sh script (Windows/Linux).
This will generate two folders named moses-<OS> and tdskt-<OS>, the two tools are merged in the moses-<OS> folder that is the one you'll have to distribute.
