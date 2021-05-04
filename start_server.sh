#!/bin/bash
git pull
source django-env/bin/activate
pip3 install -r requirements.txt
cd HomeServer
python3 manage.py migrate
gunicorn -b 0.0.0.0:443 HomeServer.wsgi