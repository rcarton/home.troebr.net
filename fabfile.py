from fabric.api import *
import os
from fabric.contrib.console import confirm

PROJECT_ROOT = '/home/troebr/home.troebr.net'
DJANGO_ROOT = os.path.join(PROJECT_ROOT, 'home')

env.directory = PROJECT_ROOT
env.hosts = ['troebr@home.troebr.net']
env.activate = 'source '+ os.path.join(PROJECT_ROOT, 'bin/activate')
env.deploy_user = 'troebr'

def virtualenv(command):
    run(env.activate + ' && ' + command)

def deploy():
    prepare_deploy()
    update_code()
    update_base()
    restart()

def prepare_deploy():
    # commit
    pass

def update_code():
    with cd(PROJECT_ROOT):
        # Git update
        run("git pull")
    
    # Deploy static files
    with cd(DJANGO_ROOT):
        with settings(warn_only=True):
            virtualenv("python manage.py collectstatic --noinput")

def update_base():
    with cd(DJANGO_ROOT):
        with settings(warn_only=True):
            virtualenv("python manage.py schemamigration common --auto")
            virtualenv("python manage.py migrate common")

def restart():
    with cd(PROJECT_ROOT):
        with settings(warn_only=True):
            virtualenv("./restart.sh")

        
