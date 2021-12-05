#!/bin/bash

python manage.py makemigrations

python manage.py migrate

exec gunicorn kavKev_Site.wsgi:application -b 0.0.0.0:8000 --reload