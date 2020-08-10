FROM torizon/arm64v8-debian-base:buster

#%application.expose%#
#%application.arg%#

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND="noninteractive"

#%application.env%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.preinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN if [ ! -z "#%application.extrapackages%#" ]; then \
    apt-get -q -y update \
    && apt-get -q -y install #%application.extrapackages%# \
    && rm -rf /var/lib/apt/lists/* ; \
    fi

# commands that should be run after all packages have been installed (RUN/COPY/ADD)
#%application.buildfiles%#
#%application.buildcommands%#

COPY work/#%application.appname%# /#%application.appname%#
#%application.targetfiles%#

USER #%application.username%#

WORKDIR /#%application.appname%#

# commands that will run on the target (ENTRYPOINT or CMD)
CMD /#%application.appname%#/#%application.exename%# #%application.appargs%#
#%application.targetcommands%#
