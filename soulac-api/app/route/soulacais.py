from http.client import HTTPException
from ..database import engine, get_db
from fastapi import APIRouter, Depends
from ..model import models, soulacais_schemas, group_schemas
from ..service import soulacais
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

soulacais_router = APIRouter(prefix="/soulacais", tags=["soulacais"])


@soulacais_router.get("/", response_model=list[soulacais_schemas.SoulacaisList])
def read_soulacais(db: Session = Depends(get_db)):
    return soulacais.get_all_soulacais(db)


@soulacais_router.get("/{id}", response_model=soulacais_schemas.SoulacaisInfo)
def read_soulacais(id: int, db: Session = Depends(get_db)):
    return soulacais.get_soulacais(db, id)


@soulacais_router.get("/{id}/groups", response_model=list[group_schemas.GroupBase])
def read_soulacais_groups(id: int, db: Session = Depends(get_db)):
    return soulacais.get_soulacais_groups(db, id)


@soulacais_router.post("/", response_model=soulacais_schemas.SoulacaisCreate)
def create_soulacais(
    soulacaisSchema: soulacais_schemas.SoulacaisCreate, db: Session = Depends(get_db)
):
    return soulacais.create_soulacais(db, soulacaisSchema)


@soulacais_router.patch("/", response_model=soulacais_schemas.SoulacaisUpdate)
def update_soulacais(
    soulacaisSchema: soulacais_schemas.SoulacaisUpdate, db: Session = Depends(get_db)
):
    return soulacais.update_soulacais(db, soulacaisSchema)


@soulacais_router.delete("/{id}", response_model=soulacais_schemas.SoulacaisInfo)
def delete_soulacais(id: int, db: Session = Depends(get_db)):
    return soulacais.delete_soulacais(db, id)
