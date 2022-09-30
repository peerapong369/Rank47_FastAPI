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

class DbVerifyLotData(Base):
    __tablename__ = "VerifyLotData"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, unique=False)
    lot = Column(String, unique=False)
    lotdataid = Column(String, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class VerifyLotDataBase(BaseModel):
    product: str
    lot: str
    lotdataid: str


class VerifyLotDataDisplayBase(BaseModel):
    id: int
    product: str
    lot: str
    lotdataid: str
    created_date:datetime
    update_date:datetime

    class Config:
        orm_mode = True