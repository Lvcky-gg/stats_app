#!/usr/bin/env bash

set -o errexit


pipenv install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

