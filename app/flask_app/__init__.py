import os

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager

from flask_graphql import GraphQLView

from flask_jwt_extended import (
    JWTManager
)

from .ext.database import db
from .schema import schema

def register_db(app):
	db_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
	    dbuser=os.environ.get('POSTGRES_USER'),
	    dbpass=os.environ.get('POSTGRES_PASSWORD'),
	    dbhost=os.environ.get('POSTGRES_HOST'),
	    dbname=os.environ.get('POSTGRES_DB')
	)

	app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	db.init_app(app)

def register_jwt(app):
	app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret')
	jwt = JWTManager(app)
	
	@jwt.user_loader_callback_loader
	def user_loader_callback(identity):
		user = User.query.filter_by(email=identity).first()

		if user is None:
			return None

		return user	

def create_app(test_config=None):
	#create and configure app

	app = Flask(__name__)

	register_db(app)

	register_jwt(app)

	app.add_url_rule(
		'/graphql', 
		view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

	@app.teardown_appcontext
	def shutdown_session(exception=None):
		db.session.remove()

	return app
