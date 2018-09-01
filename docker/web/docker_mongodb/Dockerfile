FROM mongo:4.1.2

ARG user=mongodb_user

RUN apt update
RUN apt-get install -y vim sudo curl wget bash-completion openssl expect build-essential libssl-dev git \
      && \
      apt-get clean

RUN useradd --create-home --shell /bin/bash --password $(openssl passwd -1 icl) $user

RUN adduser $user sudo
RUN echo 'root:icl' | chpasswd

#define working directoty
WORKDIR /data

