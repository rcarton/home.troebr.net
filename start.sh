#!/bin/bash

cd ~/troebr.net/troebr
source ../bin/activate
exec gunicorn_django -c ../gunicorn.conf.py

 