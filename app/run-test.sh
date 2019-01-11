#!/bin/bash

python manage.py db migrate
python manage.py db upgrade
python manage.py create_superuser

pip install -e .
pytest