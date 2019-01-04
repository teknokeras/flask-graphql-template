from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Create database engine

##Postgresql
db_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ.get('POSTGRES_USER'),
    dbpass=os.environ.get('POSTGRES_PASS'),
    dbhost=os.environ.get('POSTGRES_HOST'),
    dbname=os.environ.get('POSTGRES_DB_NAME')
)


engine = create_engine(db_uri, convert_unicode=True)

# Declarative base model to create database tables and classes
Base = declarative_base()
Base.metadata.bind = engine  # Bind engine to metadata of the base class

# Create database session object
db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
Base.query = db_session.query_property()  # Used by graphql to execute queries