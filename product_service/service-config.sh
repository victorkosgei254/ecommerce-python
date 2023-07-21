#!/bin/bash

BIULD_DIR="/build"
DIST_DIR="/dist"

#activate the virtual env
source venv/bin/activate

if [ "$1" = "build" ]
then
    python setup.py sdist
    python setup.py bdist
fi