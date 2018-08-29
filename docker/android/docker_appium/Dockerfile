FROM appium/appium

#define working directoty
#ARG user=appium_user
#WORKDIR /home/$user
WORKDIR /data

#Install tools
RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect \
      && \
      apt-get clean

#User setting
#RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user
#RUN adduser $user sudo
RUN echo 'root:icl' | chpasswd

#Python3
RUN apt install -y vim python3-pip python3-dev build-essential git
RUN pip3 install Appium-Python-Client
RUN pip3 install pytest

CMD ["appium","-p","2020"]
#RUN git clone https://github.com/appium-boneyard/sample-code.git




