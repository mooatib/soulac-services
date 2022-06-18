from ..database import engine, get_db
from fastapi import APIRouter, Depends
from ..model import models, drink_schemas, page_schemas
from ..service import drinks
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

drinks_router = APIRouter(prefix="/drinks", tags=["drinks"])


@drinks_router.get("/", response_model=list[drink_schemas.DrinkDisplayBase])
def read_drinks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return drinks.get_drinks(db, skip, limit)


@drinks_router.get("/user/{id}", response_model=list[drink_schemas.DrinkList])
def read_user_drinks(
    id: int,
    nbr: int,
    limit: int,
    orderBy: str,
    orderByAsc: bool,
    search: str,
    db: Session = Depends(get_db),
):
    return drinks.get_user_drinks(
        db, id, page_schemas.Page(nbr, limit, orderBy, orderByAsc, search)
    )


@drinks_router.get("/{id}", response_model=drink_schemas.DrinkDisplayBase)
def read_drink(id: int, db: Session = Depends(get_db)):
    return drinks.get_drink(db, id)


@drinks_router.post("/", response_model=drink_schemas.DrinkCreate)
def create_drink(drinkSchema: drink_schemas.DrinkCreate, db: Session = Depends(get_db)):
    return drinks.create_drink(db, drinkSchema)


@drinks_router.patch("/", response_model=drink_schemas.DrinkUpdate)
def update_drink(drinkSchema: drink_schemas.DrinkUpdate, db: Session = Depends(get_db)):
    return drinks.update_drink(db, drinkSchema)


@drinks_router.delete("/{id}", response_model=drink_schemas.DrinkDisplayBase)
def delete_drink(id: int, db: Session = Depends(get_db)):
    return drinks.delete_drink(db, id)
