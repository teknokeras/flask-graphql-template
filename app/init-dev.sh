#!/bin/bash

python manage.py db migrate
python manage.py db upgrade
python manage.py create_superuser

flask run --host=0.0.0.0 --port=80
