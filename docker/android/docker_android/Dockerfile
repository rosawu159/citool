FROM ubuntu:16.04

ARG user=android_user
ARG password=s123

#Install tools
RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential git zip\
      && \
      apt-get clean

#User setting
RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 $password) $user
RUN adduser $user sudo
RUN echo 'root:s123' | chpasswd

#Setting user environment
ENV USER /home/$user/

#Install Python3
RUN apt install -y python3-pip python3-dev

#Install java
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa -y
RUN apt update
RUN apt-get install -y openjdk-8-jdk

#Ininstall VNC and VNC setting
COPY keyboard /etc/default/keyboard
RUN apt-get install -y tightvncserver

RUN mkdir ${USER}/.vnc/
RUN echo "iclicl" | tightvncpasswd -f > ${USER}/.vnc/passwd
RUN chmod 600 ${USER}/.vnc/passwd
RUN chown $user:$user -R ${USER}/.vnc

#define working directory
WORKDIR ${USER}/Android

#change user
USER $user

# copy vnc script to HOME
COPY vnc.sh ${USER}

#Start vnc Server
CMD ${USER}/vnc.sh
