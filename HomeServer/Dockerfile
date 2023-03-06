FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install pkg-config -y
RUN apt-get install libcairo2-dev -y
RUN apt-get install openssl -y
RUN apt-get install libjpeg-dev -y
RUN apt-get install zlib1g-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install gcc -y
RUN apt-get install libc-dev -y
RUN apt-get install postgresql -y
RUN apt-get install postgresql-contrib -y
RUN apt-get install libpq-dev -y

RUN mkdir /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./ /app
WORKDIR /app
CMD ["gunicorn"  , "-b", "0.0.0.0:80", "HomeServer.wsgi"]
