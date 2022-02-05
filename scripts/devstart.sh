#!/usr/bin/env bash

source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d
./manage.py makemigrations
./manage.py migrate
./manage.py runserver $1
