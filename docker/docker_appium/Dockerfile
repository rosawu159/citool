FROM appium/appium

#define working directoty
WORKDIR /data

RUN apt update
RUN apt install -y vim python3-pip python3-dev build-essential git

RUN pip3 install Appium-Python-Client
RUN pip3 install pytest

CMD ["appium","-p","2020"]
#RUN git clone https://github.com/appium-boneyard/sample-code.git




