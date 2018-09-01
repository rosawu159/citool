#! /bin/bash

path=/home/icl/docker-storage/jenkins
tar cvf $path.tar $path

timestamp="$(date +'%Y%m%d%H%M')"
if [ -d Log ]; then
  mkdir Log/$timestamp
else
  mkdir -p Log/$timestamp
fi

