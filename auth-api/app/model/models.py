from ..database import db
from sqlalchemy import Column, Integer, String


class User(db):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
