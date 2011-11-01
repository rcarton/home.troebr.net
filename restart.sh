#!/bin/bash

cd ~/home.troebr.net/home
kill -HUP `cat ~/home.troebr.net/home/gunicorn.pid`
./start.sh
 
