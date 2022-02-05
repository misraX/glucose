#!/usr/bin/env bash

python ./manage.py makemigrations
python ./manage.py migrate
mkdir -pv /var/www/static
python ./manage.py collectstatic --noinput
uwsgi --py-autoreload 2 --http-socket :8000 --module una.wsgi # TO BE REPLACED WITH uwsgi.in
