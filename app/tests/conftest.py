import pytest
import os

from werkzeug.security import generate_password_hash

from flask_app import create_app
from flask_app.modules.user.model import User
from flask_app.modules.role.model import Role

@pytest.fixture(scope='module')
def create_admin():
	role = Role(name=os.environ.get('DEFAULT_ADMINISTRATOR_ROLE', 'ADMINISTRATOR'))

	hashed_password = generate_password_hash(os.environ.get('DEFAULT_ADMIN_PASSWORD', 'flaskiscool'), method='pbkdf2:sha256', salt_length=8)

	user = User(
		email=os.environ.get('DEFAULT_ADMIN_EMAIL'), 
		name=os.environ.get('DEFAULT_ADMIN_FULL_NAME'), 
		nick_name=os.environ.get('DEFAULT_ADMIN_NICK_NAME'), 
		password=hashed_password, 
		role_id=role.id, 
		role=role)

	return user

@pytest.fixture(scope='module')
def client():
    flask_app = create_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

