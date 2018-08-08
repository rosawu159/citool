#! /bin/bash

#Install Docker
sudo apt-get update
sudo apt-get install docker -y

#check docker group 
cat /etc/group | grep docker

#add docker to group
#sudo groupadd docker

#add user to docker group
sudo gpasswd -a ${USER} docker

#docker retart
sudo service docker restart

echo "login again Please"

