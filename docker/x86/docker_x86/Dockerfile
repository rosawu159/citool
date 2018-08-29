FROM ubuntu:16.04

ARG user=web_user

RUN apt update

RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev \
			git-core gnupg flex bison gperf build-essential \
  			zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  			lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
			libgl1-mesa-dev libxml2-utils xsltproc unzip \
                        python-pip libyaml-dev python-dev bc \
			genisoimage syslinux gettext \
RUN apt install -y 
    

RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user
RUN adduser $user sudo
RUN echo 'root:root' | chpasswd
