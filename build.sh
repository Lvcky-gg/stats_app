#!/usr/bin/env bash

set -o errexit


poetry install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

