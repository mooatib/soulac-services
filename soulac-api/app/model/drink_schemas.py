from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .soulacais_schemas import SoulacaisBase, SoulacaisDisplayBase, SoulacaisSimpleBase
from .alcohol_schemas import AlcoholDisplayBase


class DrinkBase(BaseModel):
    id: int
    quantity: float
    date: datetime

    class Config:
        orm_mode = True


class DrinkDisplayBase(DrinkBase):
    soulacais: SoulacaisDisplayBase
    alcohol: AlcoholDisplayBase


class DrinkSimpleBase(DrinkBase):
    soulacais: SoulacaisSimpleBase
    alcohol: AlcoholDisplayBase


class UserDrinkSimpleBase(DrinkBase):
    alcohol: AlcoholDisplayBase


class DrinkCreate(BaseModel):
    alcohol: AlcoholDisplayBase
    quantity: float
    date: datetime

    class Config:
        orm_mode = True


class DrinkUpdate(BaseModel):
    alcohol: Optional[AlcoholDisplayBase] = None
    quantity: Optional[float] = None
    date: Optional[datetime] = None

    class Config:
        orm_mode = True
