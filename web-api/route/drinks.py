from database import engine, get_db
from fastapi import APIRouter, Depends
from model import models, drink_schemas
from service import drinks
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

drinks_router = APIRouter(prefix="/drinks", tags=["drinks"])

@drinks_router.get("/", response_model=list[drink_schemas.UserList])
def read_drinks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return drinks.get_drinks(db, skip, limit)

@drinks_router.get("/{id}", response_model=drink_schemas.UserInfo)
def read_drink(id : int, db: Session = Depends(get_db)):
    return drinks.get_drink(db, id)

@drinks_router.post("/", response_model=drink_schemas.UserCreate)
def create_drink(drinkSchema : drink_schemas.UserCreate, db: Session = Depends(get_db)):
    return drinks.create_drink(db, drinkSchema)

@drinks_router.patch("/", response_model=drink_schemas.UserUpdate)
def update_drink(drinkSchema: drink_schemas.UserUpdate, db: Session = Depends(get_db)):
    return drinks.update_drink(db, drinkSchema)

@drinks_router.delete("/{id}", response_model=drink_schemas.UserInfo)
def delete_drink(id : int, db: Session = Depends(get_db)):
    return drinks.delete_drink(db, id)