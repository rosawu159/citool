FROM ubuntu:14.04

ARG user=x86_user
WORKDIR /data
COPY runAndroid.sh /data/runAndroid.sh

RUN apt update

#RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev \
#			git-core gnupg flex bison gperf build-essential \
#  			zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
#  			lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
#			libgl1-mesa-dev libxml2-utils xsltproc unzip \
#                        python-pip libyaml-dev python-dev bc \
#			genisoimage syslinux gettext \

RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev
RUN apt-get install -y git-core gnupg flex bison gperf build-essential
RUN apt-get install -y zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386
RUN apt-get install -y lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache
RUN apt-get install -y libgl1-mesa-dev libxml2-utils xsltproc unzip
RUN apt-get install -y python-pip libyaml-dev python-dev bc 
RUN apt-get install -y genisoimage syslinux gettext software-properties-common 

RUN add-apt-repository -y ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get install -y openjdk-8-jdk
RUN update-alternatives --config java


RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user
RUN adduser $user sudo
RUN echo 'root:icl' | chpasswd
ENV USER=$(whoami)




