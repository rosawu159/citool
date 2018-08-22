FROM jenkins/jenkins

#define working directoty
WORKDIR /var/jenkins_home

#USER 
RUN ssh-keygen -t rsa
RUN cat .ssh/id_rsa.pub | ssh icl@10.200.20.2 'cat >> .ssh/authorized_keys'
ARG user=jenkins_user

