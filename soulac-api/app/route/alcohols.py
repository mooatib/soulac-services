from ..database import engine, get_db
from fastapi import APIRouter, Depends
from ..model import models, alcohol_schemas
from ..service import alcohols
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

alcohols_router = APIRouter(prefix="/alcohols", tags=["alcohols"])

@alcohols_router.get("/", response_model=list[alcohol_schemas.AlcoholList])
def read_alcohols(db: Session = Depends(get_db)):
    return alcohols.get_alcohols(db)

@alcohols_router.get("/{id}", response_model=alcohol_schemas.AlcoholList)
def read_alcohol(id : int, db: Session = Depends(get_db)):
    return alcohols.get_alcohol(db, id)

@alcohols_router.post("/", response_model=alcohol_schemas.AlcoholCreate)
def create_alcohol(userSchema : alcohol_schemas.AlcoholCreate, db: Session = Depends(get_db)):
    return alcohols.create_alcohol(db, userSchema)

@alcohols_router.patch("/", response_model=alcohol_schemas.AlcoholUpdate)
def update_alcohol(userSchema: alcohol_schemas.AlcoholUpdate, db: Session = Depends(get_db)):
    return alcohols.update_alcohol(db, userSchema)

@alcohols_router.delete("/{id}", response_model=alcohol_schemas.AlcoholList)
def delete_alcohol(id : int, db: Session = Depends(get_db)):
    return alcohols.delete_alcohol(db, id)