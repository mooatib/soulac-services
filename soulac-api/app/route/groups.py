from http.client import HTTPException
from ..database import engine, get_db
from fastapi import APIRouter, Depends
from ..model import models, group_schemas
from ..service import groups
from sqlalchemy.orm import Session

models.db.metadata.create_all(bind=engine)

groups_router = APIRouter(prefix="/groups", tags=["groups"])


@groups_router.get("/{filter}", response_model=list[group_schemas.GroupBase])
def read_groups(filter: str, db: Session = Depends(get_db)):
    return groups.get_groups(db, filter)


@groups_router.get("/{id}", response_model=group_schemas.GroupInfo)
def read_group(id: int, db: Session = Depends(get_db)):
    return groups.get_group(db, id)


@groups_router.post("/", response_model=group_schemas.GroupCreate)
def create_group(
    groupsSchema: group_schemas.GroupCreate, db: Session = Depends(get_db)
):
    return groups.create_group(db, groupsSchema)


@groups_router.patch("/", response_model=group_schemas.GroupUpdate)
def update_group(
    groupsSchema: group_schemas.GroupUpdate, db: Session = Depends(get_db)
):
    return groups.update_group(db, groupsSchema)


@groups_router.delete("/{id}", response_model=group_schemas.GroupInfo)
def delete_group(id: int, db: Session = Depends(get_db)):
    return groups.delete_group(db, id)
