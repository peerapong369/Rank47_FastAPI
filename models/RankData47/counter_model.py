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

class DbRankCounter(Base):
    __tablename__ = "counter"
    id = Column(Integer, primary_key=True, index=True)
    belt_name1 = Column(String, unique=False)
    belt_name2 = Column(String, unique=False)
    belt_name3 = Column(String, unique=False)
    belt_name4 = Column(String, unique=False)
    belt_name5 = Column(String, unique=False)
    belt_name6 = Column(String, unique=False)
    belt_name7 = Column(String, unique=False)
    belt_name8 = Column(String, unique=False)
    belt_name9 = Column(String, unique=False)
    belt_name10 = Column(String, unique=False)
    belt_name11 = Column(String, unique=False)
    belt_name12 = Column(String, unique=False)
    belt_name13 = Column(String, unique=False)
    belt_name14 = Column(String, unique=False)
    belt_name15 = Column(String, unique=False)
    belt_name16 = Column(String, unique=False)
    belt_count1 = Column(Integer, unique=False)
    belt_count2 = Column(Integer, unique=False)
    belt_count3 = Column(Integer, unique=False)
    belt_count4 = Column(Integer, unique=False)
    belt_count5 = Column(Integer, unique=False)
    belt_count6 = Column(Integer, unique=False)
    belt_count7 = Column(Integer, unique=False)
    belt_count8 = Column(Integer, unique=False)
    belt_count9 = Column(Integer, unique=False)
    belt_count10 = Column(Integer, unique=False)
    belt_count11 = Column(Integer, unique=False)
    belt_count12 = Column(Integer, unique=False)
    belt_count13 = Column(Integer, unique=False)
    belt_count14 = Column(Integer, unique=False)
    belt_count15 = Column(Integer, unique=False)
    belt_count16 = Column(Integer, unique=False)
    ProductName = Column(String, unique=False)
    Customer = Column(String, unique=False)
    GroupID = Column(String, unique=False)
    LotNumber = Column(String, unique=False)
    Operator = Column(String, unique=False)
    Start = Column(String, unique=False)
    Finish = Column(String, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class CounterBase(BaseModel):
    belt_name1: str
    belt_name2: str
    belt_name3: str
    belt_name4: str
    belt_name5: str
    belt_name6: str
    belt_name7: str
    belt_name8: str
    belt_name9: str
    belt_name10: str
    belt_name11: str
    belt_name12: str
    belt_name13: str
    belt_name14: str
    belt_name15: str
    belt_name16: str
    belt_count1: int
    belt_count2: int
    belt_count3: int
    belt_count4: int
    belt_count5: int
    belt_count6: int
    belt_count7: int
    belt_count8: int
    belt_count9: int
    belt_count10: int
    belt_count11: int
    belt_count12: int
    belt_count13: int
    belt_count14: int
    belt_count15: int
    belt_count16: int
    ProductName: str
    Customer: str
    GroupID: str
    LotNumber: str
    Operator: str
    Start: str
    Finish: str




class CounterDisplayBase(BaseModel):
    id: int
    belt_name1: str
    belt_name2: str
    belt_name3: str
    belt_name4: str
    belt_name5: str
    belt_name6: str
    belt_name7: str
    belt_name8: str
    belt_name9: str
    belt_name10: str
    belt_name11: str
    belt_name12: str
    belt_name13: str
    belt_name14: str
    belt_name15: str
    belt_name16: str
    belt_count1: int
    belt_count2: int
    belt_count3: int
    belt_count4: int
    belt_count5: int
    belt_count6: int
    belt_count7: int
    belt_count8: int
    belt_count9: int
    belt_count10: int
    belt_count11: int
    belt_count12: int
    belt_count13: int
    belt_count14: int
    belt_count15: int
    belt_count16: int
    ProductName: str
    Customer: str
    GroupID: str
    LotNumber: str
    Operator: str
    Start: str
    Finish: str
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True


