FROM #%platform.sdkbaseimage%#

# Debian Bullseye has higher versions of some same packages than the Toradex feed.
# Force install of Bullseye versions of these packages in order to keep the container equivalent for 32 and 64 bits architectures.
RUN HOLD_PKGS='libdrm-common libdrm-amdgpu1 libdrm2' \
    && apt-get -y update \
    && apt-get -y upgrade \
    && for P in $HOLD_PKGS ; do \
    echo ${P}=$(apt-cache show $P | sed -r -e '/^Version:/!d' -e 's/.* //' -e '/toradex/d' -e 'q') ; \
    done | xargs -r apt-get install -y --no-install-recommends \
    && apt-mark hold $HOLD_PKGS \
    && apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/*

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install gdb-multiarch procps rsync openssh-client\
    libglvnd-core-dev:armhf \
    libglvnd-dev:armhf \
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
