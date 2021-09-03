FROM torizon/debian-cross-toolchain-armhf:buster

# commands that should be run before installing packages (ex: to add a feed or keys)
#%application.sdkpreinstallcommands%#

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update \
    && apt-get -q -y install \
    gdb-multiarch \
    procps \
    rsync \
    openssh-client \
    python3-minimal \
    qt5-qmake:armhf \
    qtbase5-dev:armhf \
    #%application.devpackages%#\
    #%application.sdkpackages%#\
    && rm -rf /var/lib/apt/lists/*

# add qt pretty printer
RUN mkdir -p /home/torizon/.gdb/qt5printers/ && \
    cd /home/torizon/.gdb/qt5printers && \
echo 'python \n\
import sys, os.path \n\
sys.path.insert(0, os.path.expanduser("~/.gdb")) \n\
import qt5printers \n\
qt5printers.register_printers(gdb.current_objfile()) \n\
end' > /home/torizon/.gdbinit

ADD sdkfiles /home/torizon/.gdb/qt5printers/

#%application.sdkpostinstallcommands%#
