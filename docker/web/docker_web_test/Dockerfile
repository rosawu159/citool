FROM ubuntu:16.04

ARG user=web_test_user

RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev git \
      && \
      apt-get clean

RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user

RUN adduser $user sudo
RUN echo 'root:icl' | chpasswd


COPY package.json /home/$user/package.json
#COP init_web_test.sh /home/$user/init_web_test.sh
COPY start_web_test.sh /home/$user/start_web_test.sh
#COPY package.json /data/package.json
#COPY init_web_test.sh /data/init_web_test.sh
#COPY start_web_test.sh /data/start_web_test.sh


#
#define working directoty
WORKDIR /data
#RUN chown -R $user:$user /data
#WORKDIR /home/$user
#WORKDIR /tmp

#Python 
RUN  apt install -y python3-pip python3-dev
#RUN  pip3 install androguard 

#Nodejs
#Setting $user .bashrc
RUN echo "export NVM_DIR=\"/usr/local/nvm\"" >> /home/$user/.bashrc
RUN echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\" " >> /home/$user/.bashrc
RUN echo "[ -s \"\$NVM_DIR/bash_completion\" ] && \. \"\$NVM_DIR/bash_completion\" " >> /home/$user/.bashrc
 
#Setting root .bashrc
RUN echo "export NVM_DIR=\"/usr/local/nvm\"" >> /root/.bashrc
RUN echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && \. \"\$NVM_DIR/nvm.sh\" " >> /root/.bashrc
RUN echo "[ -s \"\$NVM_DIR/bash_completion\" ] && \. \"\$NVM_DIR/bash_completion\" " >> /root/.bashrc

ARG tmp=/tmp/tmpfile.sh
RUN echo "#! /bin/bash" >> $tmp
RUN echo "git clone https://github.com/creationix/nvm.git /usr/local/nvm" >> $tmp
RUN echo "cd /usr/local/nvm && git checkout v0.33.11" >> $tmp
RUN echo ". /usr/local/nvm/nvm.sh" >> $tmp
RUN echo "nvm install 6.11.3" >> $tmp
RUN echo "node -v " >> $tmp
RUN echo "npm -v " >> $tmp
#RUN echo "npm i pm2 -g" >> /tmp/source.sh
RUN echo "npm i mocha -g" >> $tmp
RUN echo "source /etc/profile" >> $tmp
RUN chmod +x $tmp && bash $tmp
RUN chown -R $user:$user /usr/local/nvm

#
##Ruby
##init file
RUN echo "" > $tmp 
RUN echo "#! /bin/bash" > $tmp 
RUN echo " curl -sSL https://rvm.io/mpapis.asc | gpg --import - " >> $tmp 
RUN echo " curl -sSL https://get.rvm.io | bash -s stable " >> $tmp 
RUN echo "source /etc/profile.d/rvm.sh " >> $tmp 
RUN echo "echo \"success\" " >> $tmp 
RUN chmod +x $tmp && bash $tmp 


ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN rvm requirements
RUN rvm install 2.5.1

ENV PATH /usr/local/rvm/rubies/ruby-2.5.1/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PATH /usr/local/nvm/versions/node/v6.11.3/bin:/usr/local/rvm/rubies/ruby-2.5.1/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#RUN gem i bundler
#RUN gem i thor
RUN gem i watir
RUN gem i webdrivers
RUN rvm alias create default 2.5.1

RUN adduser $user rvm

RUN echo "export PATH=\$PATH:/usr/local/rvm/bin:/usr/local/rvm/rubies/ruby-2.5.1/bin" >> /home/$user/.bashrc
#USER $user

