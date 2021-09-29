import os

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager

from flask_graphql import GraphQLView

from .ext.database import db
from .schema import schema

from .modules.user.model import User

def register_db(app):
	db.init_app(app)

def register_jwt(app):
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
	app.config.from_object(os.environ['APP_SETTINGS'])

	register_db(app)
	register_jwt(app)

	app.add_url_rule(
		'/graphql', 
		view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

	@app.teardown_appcontext
	def shutdown_session(exception=None):
		db.session.remove()

	@app.route('/rania/')
	def hello():
	    return "Hello World!"

	@app.route('/oko/')
	def d():
	    return "Cantik World!"

	return app
