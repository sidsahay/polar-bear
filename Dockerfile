FROM alpine:latest
MAINTAINER Siddharth Sahay (siddharthsahay@gmail.com)
RUN apk update
RUN apk add python3-dev git py3-pip g++
RUN git clone https://github.com/ajs/poefixer.git
RUN cd poefixer && pip3 install .
COPY src/script.py script.py
ENTRYPOINT ["python3", "script.py"]
