import os

from werkzeug.security import generate_password_hash

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_app import create_app
from flask_app.ext.database import db

from flask_app.modules.user.model import User
from flask_app.modules.role.model import Role

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_superuser():
	role_count = Role.query.count()

	if role_count > 0:
		print("Role already exist. This operation cannot proceed")
		return

	user_count = User.query.count()

	if user_count > 0:
		print("User already exist. This operation cannot proceed")
		return

	role = Role(name=os.environ.get('DEFAULT_ADMINISTRATOR_ROLE', 'ADMINISTRATOR'))
	db.session.add(role)
	db.session.commit()

	role = Role.query.first()

	hashed_password = generate_password_hash(os.environ.get('DEFAULT_ADMIN_PASSWORD', 'flaskiscool'), method='pbkdf2:sha256', salt_length=8)

	user = User(
		email=os.environ.get('DEFAULT_ADMIN_EMAIL'), 
		name=os.environ.get('DEFAULT_ADMIN_FULL_NAME'), 
		nick_name=os.environ.get('DEFAULT_ADMIN_NICK_NAME'), 
		password=hashed_password, 
		role_id=role.id)
	
	db.session.add(user)
	db.session.commit()

	print('inital admin has been set. It is recommended to change the password')


if __name__ == '__main__':
    manager.run()