#!/bin/bash
docker build -f Dockerfile -t homeserver:0.1.0 .
docker save homeserver:0.1.0 > ~/homeserver.tar
microk8s ctr image import ~/homeserver.tar