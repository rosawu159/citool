#! /bin/bash

#Install
export USER=$(whoami)

sudo apt-get update
sudo apt-get install git-core gnupg flex bison gperf build-essential \
  zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
  libgl1-mesa-dev libxml2-utils xsltproc unzip -y

sudo apt-get install python-pip libyaml-dev -y
sudo apt-get install python-dev bc -y
sudo pip install prettytable Mako pyaml dateutils --upgrade
sudo apt-get install genisoimage -y
sudo apt-get install syslinux -y
sudo apt-get install gettext -y

#Install java, jdk8 at least
sudo apt-get install -y --no-install-recommends software-properties-common
sudo add-apt-repository -y ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install -y openjdk-8-jdk
sudo update-alternatives --config java



