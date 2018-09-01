FROM ubuntu:16.04

ARG user=android_user

#define working directoty
#WORKDIR /home/$user
WORKDIR /data

#Install tools
RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential git\
      && \
      apt-get clean

#User setting
RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user
RUN adduser $user sudo
RUN echo 'root:icl' | chpasswd

#Python3
RUN apt install -y python3-pip python3-dev 


#Android studio
#RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386 zip 
#RUN wget -P https://dl.google.com/dl/android/studio/ide-zips/3.1.4.0/android-studio-ide-173.4907809-linux.zip

#VNC
COPY keyboard /etc/default/keyboard
RUN apt-get install -y xorg lxde-core tightvncserver
RUN mkdir /home/$user/.vnc/
#RUN echo "iclicl" > /home/$user/.vnc/passwd
RUN echo "iclicl" | tightvncpasswd -f > /home/$user/.vnc/passwd
RUN chmod 600 /home/$user/.vnc/passwd
#RUN tightvncpasswd -f > /home/$user/.vnc/passwd
RUN echo "lxterminal & /usr/bin/lxsession -s LXDE &" >> /home/$user/.vnc/xstartup
#RUN whoami
#CMD ['tightvncserver',':1']

#RUN apt-get install -y x11vnc xvfb 
#RUN mkdir ~/.vnc
#RUN x11vnc -storepasswd icl ~/.vnc/passwd
#COPY entrypoint.sh /entrypoint.sh
#
#ENTRYPOINT ["/entrypoint.sh"]

