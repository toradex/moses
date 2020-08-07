FROM torizon/debian-cross-toolchain-arm64:buster

# we temporarely remove Toradex feed for an issue with qtdeclarative5-dev package
RUN sed -i '/feeds.toradex.com/d' /etc/apt/sources.list

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install gdb-multiarch procps rsync openssh-client\
    qt5-qmake:arm64 \
    qtbase5-dev:arm64 \
    #%application.devpackages%#\
    #%application.sdkpackages%#\
    && rm -rf /var/lib/apt/lists/*

# fix qt_lib_gui by setting opengles2 instead of opengl flags
RUN sed -i 's/QT.gui.CONFIG = opengl/QT.gui.CONFIG = opengles2/g' /usr/lib/aarch64-linux-gnu/qt5/mkspecs/modules/qt_lib_gui.pri

#%application.sdkpostinstallcommands%#
