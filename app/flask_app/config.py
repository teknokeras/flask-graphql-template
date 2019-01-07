import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this-really-needs-to-be-changed')
    db_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
	    dbuser=os.environ.get('POSTGRES_USER'),
	    dbpass=os.environ.get('POSTGRES_PASSWORD'),
	    dbhost=os.environ.get('POSTGRES_HOST'),
	    dbname=os.environ.get('POSTGRES_DB')
	)

    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = SECRET_KEY

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = SECRET_KEY

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
