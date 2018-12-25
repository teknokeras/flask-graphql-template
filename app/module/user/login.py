from flask import jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token
)
from werkzeug.security import check_password_hash
from flask import abort

from .model import User


def process(user):

	email = user.get("email")
	password = user.get("password")

	existingUser = User.query.filter_by(email=email).first()

	if existingUser is None:
		abort(
			404, "Incorrect email and/or password 1"
		)

	if not check_password_hash(existingUser.password, password):
		abort(
			404, "Incorrect email and/or password 2"
		)

	access_token = create_access_token(identity=email)
	refresh_token = create_refresh_token(identity=email)
	return {'access_token':access_token, 'refresh_token': refresh_token}



