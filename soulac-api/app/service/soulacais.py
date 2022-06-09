from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..model import models, soulacais_schemas
from .users import get_users


def get_soulacais(db: Session, id: int):
    stored_soulacais = (
        db.query(models.Soulacais).filter(models.Soulacais.id == id).first()
    )
    if not stored_soulacais:
        raise HTTPException(status_code=400, detail="This soulacais doesn't exist")
    get_users(db, stored_soulacais.user.id)
    return stored_soulacais


def get_all_soulacais(db: Session):
    return db.query(models.Soulacais).all()


def create_soulacais(db: Session, soulacaisSchema: soulacais_schemas.SoulacaisCreate):
    stored_soulacais = (
        db.query(models.Soulacais).filter(models.Soulacais.id == id).first()
    )
    if stored_soulacais:
        raise HTTPException(status_code=400, detail="This soulacais already exist")
    get_users(db, soulacaisSchema.user.id)
    soulacais = models.Soulacais(
        uid=soulacaisSchema.user.id,
        weight=soulacaisSchema.weight,
        resistance=soulacaisSchema.resistance,
    )
    db.add(soulacais)
    db.commit()
    db.refresh(soulacais)
    return soulacais


def update_soulacais(db: Session, soulacaisSchema: soulacais_schemas.SoulacaisUpdate):
    stored_soulacais = get_soulacais(db, soulacaisSchema.id)
    soulacais_data = soulacaisSchema.dict(exclude_unset=True)
    user_data = soulacaisSchema.user.dict(exclude_unset=True)
    for key, value in soulacais_data.items():
        if key == "user":
            for userkey, uservalue in user_data.items():
                setattr(stored_soulacais.user, userkey, uservalue)
        else:
            setattr(stored_soulacais, key, value)
    db.commit()
    return stored_soulacais


def delete_soulacais(db: Session, id: int):
    stored_soulacais = get_soulacais(db, id)
    db.delete(stored_soulacais)
    db.commit()
    return stored_soulacais
