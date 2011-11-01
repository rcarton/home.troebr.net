from fabric.api import *
import os
from fabric.contrib.console import confirm

env.hosts = ['troebr@home.troebr.net']

PROJECT_ROOT = '/home/troebr/home.troebr.net'
DJANGO_ROOT = os.path.join(PROJECT_ROOT, 'home')


def deploy():
    prepare_deploy()
    update_code()
    restart()

def prepare_deploy():
    # commit
    pass

def update_code():
    with cd(PROJECT_ROOT):
        # Git update
        run("git pull")
        run("source bin/activate")
        
    # Deploy static files
    with cd(DJANGO_ROOT):
        with settings(warn_only=True):
            run("python manage.py collectstatic --noinput")

def restart():
    with cd(PROJECT_ROOT):
        with settings(warn_only=True):
            run("./restart.sh")

        
