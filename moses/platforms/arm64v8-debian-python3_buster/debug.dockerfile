FROM torizon/arm64v8-debian-base:buster

EXPOSE 6502
#%application.expose%#

#%application.arg%#

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND="noninteractive"

#%application.env%#

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.preinstallcommands%#

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    #%application.extrapackages%#\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install ptvsd

COPY work/setup.sh /setup.sh
COPY work/cleanup.sh /cleanup.sh
COPY work/requirements.txt /requirements.txt

WORKDIR /
RUN chmod a+x /setup.sh &&\
    chmod a+x /cleanup.sh &&\
    /setup.sh debug &&\
    pip install -r /requirements.txt &&\
    /cleanup.sh debug

RUN echo "#!/bin/sh" > /startptvsd && \
    echo "cd /#%application.appname%#" >> /startptvsd && \
    echo "echo \"running #%application.appname%#\"" >> /startptvsd && \
    echo "/usr/bin/python3 -m ptvsd --host 0.0.0.0 --port 6502 --wait #%application.main%# #%application.appargs%#" >> /startptvsd && \
    chmod a+x /startptvsd

#%application.buildfiles%#
#%application.buildcommands%#

#%application.targetfiles%#

USER #%application.username%#

ENTRYPOINT ["/startptvsd"]
