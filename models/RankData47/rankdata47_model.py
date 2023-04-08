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

class DbRankData47(Base):
    __tablename__ = "RankData47"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, unique=False)
    lot = Column(String, unique=False)
    W1 = Column(FLOAT, unique=False)
    W2 = Column(FLOAT, unique=False)
    L1 = Column(FLOAT, unique=False)
    L2 = Column(FLOAT, unique=False)
    SQR1 = Column(FLOAT, unique=False)
    SQR2 = Column(FLOAT, unique=False)
    SQR3 = Column(FLOAT, unique=False)
    SQR4 = Column(FLOAT, unique=False)
    SQR5 = Column(FLOAT, unique=False)
    SQR6 = Column(FLOAT, unique=False)
    SQR7 = Column(FLOAT, unique=False)
    SQR8 = Column(FLOAT, unique=False)
    ST1 = Column(FLOAT, unique=False)
    ST2 = Column(FLOAT, unique=False)
    ST3 = Column(FLOAT, unique=False)
    ST4 = Column(FLOAT, unique=False)
    result = Column(String, unique=False)
    stage = Column(Integer, unique=False)
    speed = Column(FLOAT, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class RankDataBase(BaseModel):
    product: str
    lot: str
    W1: float
    W2: float
    L1: float
    L2: float
    SQR1: float
    SQR2: float
    SQR3: float
    SQR4: float
    SQR5: float
    SQR6: float
    SQR7: float
    SQR8: float
    ST1: float
    ST2: float
    ST3: float
    ST4: float
    result: str
    stage: int
    speed: float


class RankDataDisplayBase(BaseModel):
    id: int
    product: str
    lot: str
    W1: float
    W2: float
    L1: float
    L2: float
    SQR1: float
    SQR2: float
    SQR3: float
    SQR4: float
    SQR5: float
    SQR6: float
    SQR7: float
    SQR8: float
    ST1: float
    ST2: float
    ST3: float
    ST4: float
    result: str
    stage:int
    speed: float
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True


class ProductGroupDisplay(BaseModel):
    product: str

    class Config:
        orm_mode = True

class ProductLotDisplay(BaseModel):
    lot: str

    class Config:
        orm_mode = True

