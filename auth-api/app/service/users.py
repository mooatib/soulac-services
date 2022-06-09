from fastapi import HTTPException
from ..model import models, user_schemas
from requests import Session


def get_user(db: Session, email: str):
    stored_user = db.query(models.User).filter(models.User.email == email).first()
    if not stored_user:
        raise HTTPException(status_code=400, detail="This user doesn't exists")
    return stored_user


def create_user(db: Session, userSchema: user_schemas.UserEncrypted):
    stored_user = (
        db.query(models.User).filter(models.User.email == userSchema.email).first()
    )
    if stored_user:
        raise HTTPException(status_code=400, detail="This user already exists")
    user = models.User(
        username=userSchema.username,
        email=userSchema.email,
        password=userSchema.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
