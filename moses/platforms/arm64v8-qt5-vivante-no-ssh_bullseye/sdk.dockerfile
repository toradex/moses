FROM #%platform.sdkbaseimage%#

RUN HOLD_PKGS='libdrm-common libdrm-amdgpu1:arm64 libdrm2:arm64' \
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
    qt5-qmake:arm64 \
    qtbase5-dev:arm64 \
    && rm -rf /var/lib/apt/lists/*

# fix qt_lib_gui by setting opengles2 instead of opengl flags
RUN sed -i 's/QT.gui.CONFIG = opengl/QT.gui.CONFIG = opengles2/g' /usr/lib/aarch64-linux-gnu/qt5/mkspecs/modules/qt_lib_gui.pri

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
