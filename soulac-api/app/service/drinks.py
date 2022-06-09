from datetime import datetime

from fastapi import HTTPException
from requests import Session

from ..model import drink_schemas, models
from .alcohols import get_alcohol
from .soulacais import get_soulacais


def get_drink(db : Session, id : int):
    stored_drink = db.query(models.Drink).filter(models.Drink.id == id).first()
    if not stored_drink:
        raise HTTPException(
            status_code = 400,
            detail = "This drink doesn't exist"
        )
    return stored_drink

def get_drinks(db : Session, skip: int = 0, limit: int = 10):
    return db.query(models.Drink).offset(skip).limit(limit).all()

def get_user_drinks(db : Session, id : int, skip: int = 0, limit: int = 10):
    return db.query(models.Drink).filter(models.Drink.sid == id).offset(skip).limit(limit).all()

def create_drink(db : Session, drinkSchema: drink_schemas.DrinkCreate):
    drink = models.Drink(sid = drinkSchema.soulacais.id, aid = drinkSchema.alcohol.id, quantity = drinkSchema.quantity, date = datetime.now())
    db.add(drink)
    db.commit()
    db.refresh(drink)
    return drink

def update_drink(db : Session, drinkSchema: drink_schemas.DrinkUpdate):
    stored_drink = get_drink(db, drinkSchema.id)
    get_soulacais(db, drinkSchema.soulacais.id)
    get_alcohol(db, drinkSchema.alcohol.id)
    drink_data = drinkSchema.dict(exclude_unset=True)
    alcohol_data = drinkSchema.alcohol.dict(exclude_unset=True)
    for key, value in drink_data.items():
        if key == "alcohol":
            for alcoholkey, alcoholvalue in alcohol_data.items():
                setattr(stored_drink.alcohol, alcoholkey, alcoholvalue)
        else:
            setattr(stored_drink, key, value)
    db.commit()
    return stored_drink

def delete_drink(db: Session, id: int):
    stored_drink = get_drink(db, id)
    db.delete(stored_drink)
    db.commit()
    return stored_drink
