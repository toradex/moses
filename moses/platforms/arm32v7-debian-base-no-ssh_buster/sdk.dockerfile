FROM torizon/debian-cross-toolchain-armhf:buster

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install gdb rsync openssh-client\
    #%application.devpackages%#\
    && rm -rf /var/lib/apt/lists/*

#%application.sdkpostinstallcommands%#
