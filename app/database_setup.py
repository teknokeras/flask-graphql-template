import os

from werkzeug.security import generate_password_hash

from database import base
from module.user.model import User 
from module.role.model import Role 

from applog import log

if __name__ == '__main__':
    log.info('Create database {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)

    # add default role
    log.info('Create default admin role')
    role_name = os.environ.get('DEFAULT_ADMINISTRATOR_ROLE', 'ADMINISTRATOR')
    role = Role(name=role_name)
    base.db_session.add(role)
    base.db_session.commit()

    # add default admin
    log.info('Create default admin user')
    email = os.environ.get('DEFAULT_ADMIN_EMAIL', 'root@flask.com')
    name = os.environ.get('DEFAULT_ADMIN_FULL_NAME', 'root')
    nick_name = os.environ.get('DEFAULT_ADMIN_NICK_NAME', 'root')
    password = generate_password_hash(os.environ.get('DEFAULT_ADMIN_PASSWORD', 'flaskiscool'), method='pbkdf2:sha256', salt_length=8)
    role = Role.query.filter_by(name=role_name).first()
    role_id = role.id    

    user = User(email=email, name=name, nick_name=nick_name, password=password, role_id=role_id, role=role)
    base.db_session.add(user)
    base.db_session.commit()

    log.info('Default admin creation completed')

