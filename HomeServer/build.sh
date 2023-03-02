#!/bin/bash
docker build -f Dockerfile -t localhost:32000/homeserver:0.1.0 .
docker push localhost:32000/homeserver:0.1.0