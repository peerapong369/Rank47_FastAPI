from tkinter.tix import COLUMN
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.RankData47.counter_model import DbRankCounter, CounterBase


def create(db: Session, request: CounterBase):
    new_rankcounter = DbRankCounter(
        belt_name1=request.belt_name1,
        belt_name2=request.belt_name2,
        belt_name3=request.belt_name3,
        belt_name4=request.belt_name4,
        belt_name5=request.belt_name5,
        belt_name6=request.belt_name6,
        belt_name7=request.belt_name7,
        belt_name8=request.belt_name8,
        belt_name9=request.belt_name9,
        belt_name10=request.belt_name10,
        belt_name11=request.belt_name11,
        belt_name12=request.belt_name12,
        belt_name13=request.belt_name13, 
        belt_name14=request.belt_name14,
        belt_name15=request.belt_name15,
        belt_name16=request.belt_name16,
        belt_count1=request.belt_count1,
        belt_count2=request.belt_count2,
        belt_count3=request.belt_count3,
        belt_count4=request.belt_count4,
        belt_count5=request.belt_count5,
        belt_count6=request.belt_count6,
        belt_count7=request.belt_count7,
        belt_count8=request.belt_count8,
        belt_count9=request.belt_count9,
        belt_count10=request.belt_count10,
        belt_count11=request.belt_count11,
        belt_count12=request.belt_count12,
        belt_count13=request.belt_count13,
        belt_count14=request.belt_count14,
        belt_count15=request.belt_count15,
        belt_count16=request.belt_count16,
        ProductName=request.ProductName,
        Customer=request.Customer,
        GroupID=request.GroupID,
        LotNumber=request.LotNumber,
        Operator=request.Operator,
        Start=request.Start,
        Finish=request.Finish,
    )
    db.add(new_rankcounter)
    db.commit()
    db.refresh(new_rankcounter)
    return new_rankcounter



def read_rankcounter(db: Session):
    return db.query(DbRankCounter).all()


def update(db: Session, id: int, request: CounterBase):
    counter = db.query(DbRankCounter).filter(DbRankCounter.id == id).first()
    counter.belt_name1 = request.belt_name1
    counter.belt_name2 = request.belt_name2
    counter.belt_name3 = request.belt_name3
    counter.belt_name4 = request.belt_name4
    counter.belt_name5 = request.belt_name5
    counter.belt_name6 = request.belt_name6
    counter.belt_name7 = request.belt_name7
    counter.belt_name8 = request.belt_name8
    counter.belt_name9 = request.belt_name9
    counter.belt_name10 = request.belt_name10
    counter.belt_name11 = request.belt_name11
    counter.belt_name12 = request.belt_name12
    counter.belt_name13 = request.belt_name13
    counter.belt_name14 = request.belt_name14
    counter.belt_name15 = request.belt_name15
    counter.belt_name16 = request.belt_name16
    counter.belt_count1 = request.belt_count1
    counter.belt_count2 = request.belt_count2
    counter.belt_count3 = request.belt_count3
    counter.belt_count4 = request.belt_count4
    counter.belt_count5 = request.belt_count5
    counter.belt_count6 = request.belt_count6
    counter.belt_count7 = request.belt_count7
    counter.belt_count8 = request.belt_count8
    counter.belt_count9 = request.belt_count9
    counter.belt_count10 = request.belt_count10
    counter.belt_count11 = request.belt_count11
    counter.belt_count12 = request.belt_count12
    counter.belt_count13 = request.belt_count13
    counter.belt_count14 = request.belt_count14
    counter.belt_count15 = request.belt_count15
    counter.belt_count16 = request.belt_count16
    counter.ProductName=request.ProductName
    counter.Customer=request.Customer
    counter.GroupID=request.GroupID
    counter.LotNumber=request.LotNumber
    counter.Operator=request.Operator
    counter.Start=request.Start
    counter.Finish=request.Finish
    db.commit()
    db.refresh(counter)
    return counter