#!/bin/bash

set -e

cd /app
waitress-serve --call 'flask_app:create_app'