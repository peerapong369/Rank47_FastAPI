from audioop import lin2adpcm
from turtle import st
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbVerifyData(Base):
    __tablename__ = "VerifyData"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, unique=False)
    lot = Column(String, unique=False)
    sheet = Column(Integer, unique=False)
    repW1 = Column(FLOAT, unique=False)
    repW2 = Column(FLOAT, unique=False)
    repL1 = Column(FLOAT, unique=False)
    repL2 = Column(FLOAT, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )


class VerifyDataBase(BaseModel):
    product: str
    lot: str
    sheet: int
    repW1: float
    repW2: float
    repL1: float
    repL2: float


class VerifyDataDisplayBase(BaseModel):
    id: int
    product: str
    lot: str
    sheet: int
    repW1: float
    repW2: float
    repL1: float
    repL2: float
    created_date:datetime
    update_date:datetime

    class Config:
        orm_mode = True

