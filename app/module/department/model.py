from database.base import Base
from sqlalchemy import Column, Integer, String

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String)