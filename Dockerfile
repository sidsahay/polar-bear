FROM alpine:latest
MAINTAINER Siddharth Sahay (siddharthsahay9700@gmail.com)
RUN apk update && apk add python3-dev py3-pip git g++
RUN git clone https://github.com/sidsahay/poefixer.git
RUN cd poefixer && pip3 install .
ENTRYPOINT ["python3", "src/script.py"]
