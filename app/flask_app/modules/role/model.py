from flask_app.ext.database import db

from flask_app.modules.user.model import User

class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role', lazy='dynamic')