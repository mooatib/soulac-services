from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .soulacais_schemas import SoulacaisBase, SoulacaisDisplayBase, SoulacaisSimpleBase
from .alcohol_schemas import AlcoholDisplayBase


class DrinkDisplayBase(BaseModel):
    id: int
    soulacais: SoulacaisDisplayBase
    alcohol: AlcoholDisplayBase
    quantity: float
    date: datetime

    class Config:
        orm_mode = True


class DrinkList(BaseModel):
    id: int
    soulacais: SoulacaisSimpleBase
    alcohol: AlcoholDisplayBase
    quantity: float
    date: datetime

    class Config:
        orm_mode = True


class DrinkCreate(BaseModel):
    soulacais: SoulacaisBase
    alcohol: AlcoholDisplayBase
    quantity: float
    date: datetime

    class Config:
        orm_mode = True


class DrinkUpdate(BaseModel):
    id: int
    soulacais: SoulacaisBase
    alcohol: Optional[AlcoholDisplayBase] = None
    quantity: Optional[float] = None
    date: Optional[datetime] = None

    class Config:
        orm_mode = True
