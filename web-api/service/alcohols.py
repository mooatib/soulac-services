from http.client import HTTPException
from sqlalchemy.orm import Session
from model import models, alcohol_schemas

def get_alcohol(db : Session, id : int):
    stored_alcohol = db.query(models.Alcohol).filter(models.Alcohol.id == id).first()
    if not stored_alcohol:
        raise HTTPException(
            status_code=400,
            detail="This Alcohol doesn't exist"
        )
    return stored_alcohol

def get_alcohols(db : Session):
    return db.query(models.Alcohol).all()

def create_alcohol(db : Session, alcoholSchema: alcohol_schemas.AlcoholCreate):
    stored_alcohol = db.query(models.Alcohol).filter(models.Alcohol.id == alcoholSchema.id).first()
    if stored_alcohol:
        raise HTTPException(
            status_code=400,
            detail="This Alcohol already exists"
        )
    Alcohol = models.Alcohol(name = alcoholSchema.name, type = alcoholSchema.type, percentage = alcoholSchema.percentage)
    db.add(Alcohol)
    db.commit()
    db.refresh(Alcohol)
    return Alcohol

def update_alcohol(db : Session, alcoholSchema: alcohol_schemas.AlcoholUpdate):
    stored_alcohol = db.query(models.Alcohol).filter(models.Alcohol.name == alcoholSchema.name, models.Alcohol.percentage == alcoholSchema.percentage).first()
    if not stored_alcohol:
        raise HTTPException(
            status_code=400,
            detail="This Alcohol doesn't exist"
        )
    update_data = alcoholSchema.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_alcohol, key, value)
    db.add(stored_alcohol)    
    db.commit()
    db.refresh(stored_alcohol)
    return stored_alcohol

def delete_alcohol(db : Session, id : int):
    stored_alcohol = db.query(models.Alcohol).filter(models.Alcohol.id == id).first()
    if not stored_alcohol:
        raise HTTPException(
            status_code=400,
            detail="This Alcohol doesn't exist"
        )
    db.delete(stored_alcohol)
    db.commit()
    return stored_alcohol

