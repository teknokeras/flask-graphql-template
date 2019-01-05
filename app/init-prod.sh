#!/bin/bash

set -e

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py create_superuser

waitress-serve --call 'flask_app:create_app' --port=80