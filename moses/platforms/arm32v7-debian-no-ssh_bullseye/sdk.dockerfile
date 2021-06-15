FROM #%platform.sdkbaseimage%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y upgrade \
    && apt-get -q -y install gdb-multiarch procps rsync openssh-client\
    #%application.devpackages%#\
    #%application.sdkpackages%#\
    && rm -rf /var/lib/apt/lists/*

RUN if [ ! -z "#%application.devpackages%#" ]; then \
    apt-get -q -y update \
    && apt-get -q -y install #%application.devpackages%# \
    && rm -rf /var/lib/apt/lists/* ; \
    fi

RUN if [ ! -z "#%application.sdkpackages%#" ]; then \
    apt-get -q -y update \
    && apt-get -q -y install #%application.sdkpackages%# \
    && rm -rf /var/lib/apt/lists/* ; \
    fi




#%application.sdkpostinstallcommands%#
