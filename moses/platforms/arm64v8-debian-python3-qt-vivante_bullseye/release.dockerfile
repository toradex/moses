FROM --platform=#%platform.architecture%# #%platform.baseimage%#

#%application.expose%#
#%application.arg%#

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND="noninteractive"

#%application.env%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.preinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    dos2unix \
    python3-minimal \
    python3-pip \
    python3-setuptools \
    qml-module-qtquick-controls \
    qml-module-qtquick-controls2 \
    qml-module-qtquick2 \
    python3-pyside2.qtwidgets \
    python3-pyside2.qtgui \
    python3-pyside2.qtqml \
    python3-pyside2.qtcore \
    python3-pyside2.qtquick \
    python3-pyside2.qtnetwork \
    qml-module-qtquick-dialogs \
    #%application.extrapackages%#\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY work/setup.sh /setup.sh
COPY work/cleanup.sh /cleanup.sh
COPY work/requirements.txt /requirements.txt

WORKDIR /
RUN dos2unix /requirements.txt &&\
    dos2unix /setup.sh &&\
    dos2unix /cleanup.sh &&\
    chmod a+x /setup.sh &&\
    chmod a+x /cleanup.sh &&\
    /setup.sh debug &&\
    pip install -r /requirements.txt &&\
    /cleanup.sh debug

COPY work/#%application.appname%# /#%application.appname%#

# commands that should be run after all packages have been installed (RUN/COPY/ADD)
#%application.buildfiles%#
#%application.buildcommands%#

#%application.targetfiles%#

USER #%application.username%#
WORKDIR /#%application.appname%#

CMD /usr/bin/python3 #%application.main%# #%application.appargs%#

# commands that will run on the target (ENTRYPOINT or CMD)
#%application.targetcommands%#
