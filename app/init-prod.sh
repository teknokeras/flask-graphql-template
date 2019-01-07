#!/bin/bash

set -e

#python setup.py bdist_wheel

#pip install dist/flask_app-0.0.0-py3-none-any.whl

#python manage.py db migrate
python manage.py db upgrade
python manage.py create_superuser

waitress-serve --port=80 --call 'flask_app:create_app'