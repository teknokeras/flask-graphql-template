#!/bin/bash

set -e

cd /app/flask_app
rm database.db
python database_setup.py

cd ../

python setup-db.sh
waitress-serve --call 'flask_app:create_app'