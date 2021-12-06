#!/bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec gunicorn kavKev_Site.wsgi:application --bind 0.0.0.0:8000 --reload -v 4