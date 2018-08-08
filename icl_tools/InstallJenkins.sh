#! /bin/bash

#add java jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo add-apt-repository ppa:openjdk-r/ppa -y

#install java jenlins
sudo apt-get update
sudo apt-get install jenkins -y
sudo apt-get install openjdk-8-jdk -y 

echo ""
echo "If you want to chage port, you can edit /etc/default/jenkins, search \" HTTP_PORT=8080 \" "

#show java version
echo " "
echo "Java version: " $( java -version )


#show jenkins 
sudo /etc/init.d/jenkins status
echo " "
echo "+sleep 3"

sleep 3
echo " "
echo "Your Passowrd Path : /var/lib/jenkins/secrets/initialAdminPassword "
echo "Your Password : " $(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)

