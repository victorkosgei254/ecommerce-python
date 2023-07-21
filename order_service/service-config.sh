#!/bin/bash
if [ "$1" = "build" ]
then
    python setup.py sdist
    python setup.py bdist
elif [ "$1" = "migrate" ]
then 
    ./manage.py makemigrations
    ./manage.py migrate
elif [ "$1" = "start" ]
then
    ./manage.py runserver
fi