FROM #%platform.sdkbaseimage%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install \
    gdb rsync \
    #%application.devpackages%#\
    && rm -rf /var/lib/apt/lists/*

#%application.sdkpostinstallcommands%#
