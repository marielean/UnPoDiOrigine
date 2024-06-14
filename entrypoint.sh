#!/bin/bash

if [ ! -f /usr/src/app/data/db.sqlite3 ]; then
    .venv/bin/python manage.py makemigrations
    .venv/bin/python manage.py migrate
    .venv/bin/python manage.py createsuperuser --noinput --email admin@email.com --password admin --first_name Admin --last_name Default --phone 0000000000
else
    .venv/bin/python manage.py makemigrations
    .venv/bin/python manage.py migrate
fi

.venv/bin/python manage.py runserver 0.0.0.0:8000