import enum
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from database import db

class trendEnum(enum.Enum):
    EQU = 'EQU'
    DSC = 'DSC'
    ASC = 'ASC'
    BIGASC = 'BIGASC'

class User(db):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    img = Column(String)
    sex = Column(Boolean)
    weight = Column(Integer)
    resistance = Column(Integer)
    alcohol = Column(Float, default=0.00)
    trend = Column(Enum(trendEnum), default='EQU')
    drinks = relationship(  "Drink")

class Group(db):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    img = Column(String)
    description = Column(String)
    private = Column(Boolean)

class Drink(db):
    __tablename__ = "drink"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    uid = Column(Integer, ForeignKey("user.id"))
    aid = Column(Integer, ForeignKey("alcohol.id"))
    quantity = Column(Float)
    date = Column(DateTime)
    alcohol = relationship("Alcohol")

class Alcohol(db):
    __tablename__ = "alcohol"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    type = Column(Boolean)
    percentage = Column(Float)
    hidden = Column(Boolean, default=0)

class Trophy(db):
    __tablename__ = "trophy"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    type = Column(Boolean)
