#!/usr/bin/env bash

NAME="pergamum"                              #Name of the application (*)
DJANGODIR=/home/ubuntu/pergamum/            # Django project directory (*)
SOCKFILE=/home/ubuntu/pergamum/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=ubuntu                                      # the user to run as (*)
GROUP=www-data                                     # the group to run as (*)
NUM_WORKERS=3                                    # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=pergamum.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=pergamum.wsgi                     # WSGI module name (*)
VIRTUALENV=/home/ubuntu/virtualenv/webapp/bin
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ${VIRTUALENV}/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
