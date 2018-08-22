FROM ubuntu:16.04

ARG user=web_user

RUN apt update
RUN apt install -y vim wget curl openssl

RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 s123) $user
RUN echo '$user ALL=(ALL) ALL' >> /etc/sudoers


#define working directoty
WORKDIR /home/$user

#Nodejs
RUN mkdir -p /opt/nodejs
RUN wget -P /opt/nodejs/ https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-x64.tar.gz
RUN tar xvzf /opt/nodejs/node-v6.11.3-linux-x64.tar.gz -C /opt/nodejs/
RUN cd /opt/nodejs/ && mv node-v6.11.3-linux-x64 6.11.3/
RUN ln -s /opt/nodejs/6.11.3/bin/node /bin/node && ln -s /opt/nodejs/6.11.3/bin/npm /bin/npm
RUN node -v && npm -v

RUN npm install -g eslint

RUN npm install -g mocha

#Ruby

RUN apt install -y ruby ruby-dev build-essential
RUN gem install rubocop
RUN gem install watir

USER $user

