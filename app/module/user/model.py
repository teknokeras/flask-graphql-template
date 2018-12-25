from database.base import Base, db_session
from module.role.model import Role

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, backref


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nick_name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship(
        Role,
        backref=backref('users',
                        uselist=True,
                        cascade='delete,all'))