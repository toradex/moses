FROM #%platform.sdkbaseimage%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN if [ ! -z "#%application.devpackages%#" ]; then apt-get -q -y update \
    && apt-get upgrade -q -y \
    && apt-get -q -y install \
    gdb \
    #%application.devpackages%#\
    && rm -rf /var/lib/apt/lists/*; \
    fi

#%application.sdkpostinstallcommands%#
