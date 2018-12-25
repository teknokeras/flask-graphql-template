from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager

from flask_graphql import GraphQLView

from flask_jwt_extended import (
    JWTManager
)

from schema import schema
from base import db_session

from module.user.model import User

from applog import log

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@jwt.user_loader_callback_loader
def user_loader_callback(identity):

	user = User.query.filter_by(email=identity).first()

	if user is None:
		return None

	return user

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')