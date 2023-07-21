#!/bin/bash

BIULD_DIR="/build"
DIST_DIR="/dist"

#activate the virtual env
source venv/bin/activate

if [ "$1" = "build" ]
then
    python setup.py sdist
    python setup.py bdist
elif [ "$1" = "start" ]
then
    ./manage.py runserver
elif [ "$1" = "create-tables" ]
then 
    ./manage.py makemigrations
    ./manage.py migrate
fi
