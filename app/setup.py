from setuptools import setup, find_packages

setup(name="flask_app", packages=find_packages())

setup(
    name='flask_app',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'psycopg2',
        'Flask-Migrate',
        'Flask-JWT-Extended',
        'Flask-GraphQL',
        'Flask-Script',
        'Flask-SQLAlchemy',
    ],
)