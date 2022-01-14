FROM --platform=#%platform.architecture%# #%platform.baseimage%#

# SSH
EXPOSE 2222

#%application.expose%#

# can be overridden by application
ARG SSHUSERNAME=torizon

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
    openssl \
    openssh-server \
    rsync \
    #%application.extrapackages%#\
    && apt-get clean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# copies RSA key to enable SSH login for user
COPY id_rsa.pub /id_rsa.pub

# create folders needed for the different components
# configures SSH access to the container and sets environment by default
RUN mkdir /var/run/sshd \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
    && if test $SSHUSERNAME != root ; then mkdir -p /home/$SSHUSERNAME/.ssh ; else mkdir -p /root/.ssh ; fi \
    && if test $SSHUSERNAME != root ; then cp /id_rsa.pub /home/$SSHUSERNAME/.ssh/authorized_keys ; else cp /id_rsa.pub /root/.ssh/authorized_keys ; fi \
    && echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config \
    && echo "Port 2222" >> /etc/ssh/sshd_config \
    && su -c "env" $SSHUSERNAME > /etc/environment

RUN rm -r /etc/ssh/ssh*key \
    && dpkg-reconfigure openssh-server

#%application.buildfiles%#
#%application.buildcommands%#

#%application.targetfiles%#

CMD ["/usr/sbin/sshd", "-D"]
