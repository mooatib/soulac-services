from database import engine, get_db
from fastapi import APIRouter, Depends
from model import models, user_schemas
from service import users
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/", response_model=list[user_schemas.UserList])
def read_users(db: Session = Depends(get_db)):
    return users.get_users(db)

@users_router.get("/{id}", response_model=user_schemas.UserInfo)
def read_user(id : int, db: Session = Depends(get_db)):
    return users.get_user(db)

@users_router.post("/", response_model=user_schemas.UserCreate)
def create_user(userSchema : user_schemas.UserCreate, db: Session = Depends(get_db)):
    return users.create_user(db, userSchema)

@users_router.patch("/", response_model=user_schemas.UserUpdate)
def update_user(userSchema: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(db, userSchema)

@users_router.delete("/{id}", response_model=user_schemas.UserInfo)
def delete_user(id : int, db: Session = Depends(get_db)):
    return users.delete_user(db, id)
