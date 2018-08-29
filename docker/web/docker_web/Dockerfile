FROM ubuntu:16.04

ARG user=web_user

RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev git \
      && \
      apt-get clean

RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user

RUN adduser $user sudo
RUN echo 'root:root' | chpasswd

#define working directoty
WORKDIR /home/$user

#Python 
RUN  apt install -y python3-pip python3-dev
RUN  pip3 install androguard 

#Nodejs
RUN echo "export NVM_DIR=\"/usr/local/nvm\"" >> /home/$user/.bashrc
RUN echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\" " >> /home/$user/.bashrc
RUN echo "[ -s \"\$NVM_DIR/bash_completion\" ] && \. \"\$NVM_DIR/bash_completion\" " >> /home/$user/.bashrc
 
#RUN echo "export NVM_DIR=\"/usr/local/nvm\"" >> /root/.bashrc
#RUN echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\" " >> /root/.bashrc
#RUN echo "[ -s \"\$NVM_DIR/bash_completion\" ] && \. \"\$NVM_DIR/bash_completion\" " >> /root/.bashrc

RUN echo "#! /bin/bash" >> /tmp/source.sh
RUN echo "git clone https://github.com/creationix/nvm.git /usr/local/nvm" >> /tmp/source.sh
RUN echo "cd /usr/local/nvm && git checkout v0.33.11" >> /tmp/source.sh
RUN echo ". /usr/local/nvm/nvm.sh" >> /tmp/source.sh
RUN echo "nvm install 6.11.3" >> /tmp/source.sh
RUN echo "node -v " >> /tmp/source.sh
RUN echo "npm -v " >> /tmp/source.sh
RUN echo "npm i pm2 -g" >> /tmp/source.sh
RUN echo "source /etc/profile" >> /tmp/source.sh

RUN chmod +x /tmp/source.sh
RUN /tmp/source.sh
RUN chown -R web_user:web_user /usr/local/nvm

#Ruby
RUN echo "#! /bin/bash " > /tmp/source.sh
RUN echo " curl -sSL https://rvm.io/mpapis.asc | gpg --import - " >> /tmp/source.sh
RUN echo " curl -sSL https://get.rvm.io | bash -s stable " >> /tmp/source.sh
RUN echo "source /etc/profile.d/rvm.sh " >> /tmp/source.sh
RUN echo "echo \"success\" " >> /tmp/source.sh
RUN chmod +x /tmp/source.sh
RUN /tmp/source.sh

ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN rvm requirements
RUN rvm install 2.5.1

ENV PATH /usr/local/rvm/rubies/ruby-2.5.1/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN gem i bundler
RUN gem i thor
RUN rvm alias create default 2.5.1

RUN adduser $user rvm
USER $user

RUN echo "export PATH=\$PATH:/usr/local/rvm/bin:/usr/local/rvm/rubies/ruby-2.5.1/bin" >> /home/$user/.bashrc
