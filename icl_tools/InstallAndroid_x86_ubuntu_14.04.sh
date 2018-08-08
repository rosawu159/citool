#! /bin/bash

#Install
sudo apt-get update

sudo apt-get install git-core gnupg flex bison gperf build-essential \
  zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
  libgl1-mesa-dev libxml2-utils xsltproc unzip -y

sudo apt-get install python-pip libyaml-dev -y


sudo apt-get install syslinux -y

