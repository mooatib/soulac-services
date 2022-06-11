from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..model import models

def get_users(db : Session, id : int):
    stored_user = db.query(models.User).filter(models.User.id == id).first()
    if not stored_user:
        raise HTTPException(
            status_code=400,
            detail="This user doesn't exist"
        )
    return stored_user