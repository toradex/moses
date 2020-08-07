FROM torizon/arm64v8-debian-wayland-base-vivante:buster

# GDB-remote (we can use any port there)
EXPOSE 6502

#%application.expose%#

#%application.arg%#

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND="noninteractive"

#%application.env%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.preinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install \
    gdbserver \
    procps \
    #%application.extrapackages%#\
    && rm -rf /var/lib/apt/lists/*

#%application.buildfiles%#
#%application.buildcommands%#

#%application.targetfiles%#

USER #%application.username%#

WORKDIR /#%application.appname%#

CMD gdbserver host:6502 /#%application.appname%#/#%application.exename%# #%application.appargs%#
