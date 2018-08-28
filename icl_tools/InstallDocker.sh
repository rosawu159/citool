#! /bin/bash


sudo apt-get update

#Install bridge
sudo apt-get install bridge-utils

#Install Docker
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install -y docker-ce

#check docker group 
cat /etc/group | grep docker

#add docker to group
#sudo groupadd docker

#add user to docker group
sudo gpasswd -a ${USER} docker

#docker restart
sudo service docker restart

echo "login again Please"

