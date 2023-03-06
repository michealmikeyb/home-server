#!/bin/bash
docker build -f Dockerfile -t localhost:32000/homeserver:0.2.0 .
docker push localhost:32000/homeserver:0.2.0