from fastapi import HTTPException
from requests import Session

from ..model import models, group_schemas, page_schemas


def get_group(db: Session, id: int):
    stored_group = db.query(models.Group).filter(models.Group.id == id).first()
    if not stored_group:
        raise HTTPException(status_code=400, detail="This group doesn't exist")
    return stored_group


def get_group_users(db: Session, id: int, page: page_schemas.Page):
    skip = page.nbr * page.limit
    stored_group_users = (
        db.query(models.Soulacais)
        .filter(models.Soulacais.groups.any(id=id))
        .offset(skip)
        .limit(page.limit)
        .all()
    )
    if not stored_group_users:
        raise HTTPException(status_code=400, detail="This group doesn't exist")
    print(stored_group_users)
    return stored_group_users


def get_group_drinks(db: Session, id: int, page: page_schemas.Page):
    skip = page.nbr * page.limit
    stored_group_drinks = (
        db.query(models.Drink)
        .filter(models.Drink.sid == id)
        .offset(skip)
        .limit(page.limit)
        .all()
    )

    if not stored_group_drinks:
        raise HTTPException(status_code=400, detail="This group doesn't exist")
    return stored_group_drinks


def get_groups(db: Session, filter: str):
    search_filter = ("%{}%").format(filter)
    return db.query(models.Group).filter(models.Group.name.like(search_filter))


def create_group(db: Session, groupSchema: group_schemas.GroupCreate):
    stored_group = db.query(models.Group).filter(models.Group.id == id).first()
    if stored_group:
        raise HTTPException(status_code=400, detail="This group already exist")
    group = models.Group(
        name=groupSchema.name,
        img=groupSchema.img,
        descrition=groupSchema.description,
        private=groupSchema.private,
    )
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


def update_group(db: Session, groupSchema: group_schemas.GroupUpdate):
    stored_group = get_group(db, groupSchema.id)
    group_data = groupSchema.dict(exclude_unset=True)
    for key, value in group_data.items():
        setattr(stored_group, key, value)
    db.commit()
    return stored_group


def delete_group(db: Session, id: int):
    stored_group = get_group(db, id)
    db.delete(stored_group)
    db.commit()
    return stored_group
