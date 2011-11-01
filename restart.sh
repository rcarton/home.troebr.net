#!/bin/bash

kill -HUP `cat ~/home.troebr.net/home/gunicorn.pid`
./start.sh
 
