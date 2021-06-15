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
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN if [ ! -z "#%application.extrapackages%#" ]; then \
    apt-get -q -y update \
    && apt-get -q -y install #%application.extrapackages%# \
    && rm -rf /var/lib/apt/lists/* ; \
    fi

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
