FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install pkg-config -y
RUN apt-get install libcairo2-dev -y

RUN mkdir /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./ /app
WORKDIR /app
RUN python3 /app/manage.py migrate
CMD ["gunicorn"  , "-b", "0.0.0.0:80", "HomeServer.wsgi"]
