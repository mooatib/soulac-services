from http.client import HTTPException
from sqlalchemy.orm import Session
from model import models, user_schemas

def get_user(db : Session, id : int):
    stored_user = db.query(models.User).filter(models.User.id == id).first()
    if not stored_user:
        raise HTTPException(
            status_code=400,
            detail="This user doesn't exist"
        )
    return stored_user

def get_users(db : Session):
    return db.query(models.User).all()

def create_user(db : Session, userSchema: user_schemas.UserCreate):
    stored_user = db.query(models.User).filter(models.User.email == userSchema.email).first()
    if stored_user:
        raise HTTPException(
            status_code=400,
            detail="This user already exists"
        )
    user = models.User(username = userSchema.username, email = userSchema.email, password = userSchema.password, weight = userSchema.weight, resistance = userSchema.resistance)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db : Session, userSchema: user_schemas.UserUpdate):
    stored_user = db.query(models.User).filter(models.User.id == userSchema.id).first()
    if not stored_user:
        raise HTTPException(
            status_code=400,
            detail="This user doesn't exist"
        )
    update_data = userSchema.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_user, key, value)
    db.add(stored_user)    
    db.commit()
    db.refresh(stored_user)
    return stored_user

def delete_user(db : Session, id : int):
    stored_user = db.query(models.User).filter(models.User.id == id).first()
    if not stored_user:
        raise HTTPException(
            status_code=400,
            detail="This user doesn't exist"
        )
    db.delete(stored_user)
    db.commit()
    return stored_user

