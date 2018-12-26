cd flask_app
rm database.db
python database_setup.py

flask run --host=0.0.0.0 --port=8080
