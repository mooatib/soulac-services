import enum
from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Enum,
    Table,
)
from sqlalchemy.orm import relationship
from ..database import db


class trendEnum(enum.Enum):
    EQU = "EQU"
    DSC = "DSC"
    ASC = "ASC"
    BIGASC = "BIGASC"


class User(db):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    soulacais = relationship("Soulacais", back_populates="user")


class SoulacaisGroups(db):
    __tablename__ = "soulacais_groups"
    soulacais_id = Column(ForeignKey("soulacais.id"), primary_key=True)
    group_id = Column(ForeignKey("group.id"), primary_key=True)
    role = Column(String, nullable=False, default="user")


class Soulacais(db):
    __tablename__ = "soulacais"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    uid = Column(Integer, ForeignKey("user.id"))
    img = Column(String)
    sex = Column(Boolean)
    weight = Column(Integer)
    resistance = Column(Integer)
    alcohol = Column(Float, default=0.00)
    trend = Column(Enum(trendEnum), default="EQU")
    user = relationship(
        "User",
        back_populates="soulacais",
        single_parent=True,
        cascade="save-update, delete, delete-orphan",
    )
    drinks = relationship("Drink", back_populates="soulacais")
    groups = relationship(
        "Group", secondary="soulacais_groups", back_populates="soulacais"
    )


class Group(db):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    img = Column(String)
    description = Column(String)
    private = Column(Boolean)
    soulacais = relationship(
        "Soulacais", secondary="soulacais_groups", back_populates="groups"
    )


class Drink(db):
    __tablename__ = "drink"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    sid = Column(Integer, ForeignKey("soulacais.id"))
    aid = Column(Integer, ForeignKey("alcohol.id"))
    quantity = Column(Float)
    date = Column(DateTime)
    soulacais = relationship("Soulacais", back_populates="drinks")
    alcohol = relationship("Alcohol", cascade="delete")


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
