FROM torizon/debian-cross-toolchain-arm64:buster

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install gdb-multiarch procps rsync openssh-client\
    qt5-qmake:arm64 \
    qtbase5-vivante-dev:arm64 \
    #%application.devpackages%#\
    #%application.sdkpackages%#\
    && rm -rf /var/lib/apt/lists/*

#%application.sdkpostinstallcommands%#
