from datetime import datetime
from this import d
from model import models, drink_schemas
from http.client import HTTPException
from requests import Session


def get_drink(db : Session, id : int):
    stored_drink = db.query(models.Drink).filter(models.Drink.id == id)
    if not stored_drink:
        raise HTTPException(
            status_code = 400,
            detail = "This user doesn't exist"
        )
    return stored_drink

def get_drinks(db : Session, skip: int = 0, limit: int = 10):
    return db.query(models.Drink).offset(skip).limit(limit).all()

def create_drinks(db : Session, drinkSchema: drink_schemas.DrinkCreate):
    drink = models.Drink(uid = drinkSchema.uid, aid = drinkSchema.aid, quantity = drinkSchema.quantity, date = datetime.now())
    db.add(drink)
    db.commit()
    db.refresh(drink)
    return drink

def create_drinks(db : Session, drinkSchema: drink_schemas.DrinkUpdate):
    stored_drink = db.query(models.Drink).filter(models.Drink.id == drinkSchema.id).first()
    if not stored_drink:
        raise HTTPException(
            status_code=400,
            detail="This drink doesn't exist"
        )
    update_data = drinkSchema.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_drink, key, value)
    
    db.add(stored_drink)
    db.commit()
    db.refresh(stored_drink)
    return stored_drink