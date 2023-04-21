from cProfile import label
from tkinter.tix import COLUMN
from turtle import speed
from unittest import result
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

from models.Hole.hole_models import DbRankData47Hole, HoleDataBase


def create(db: Session, request: HoleDataBase):
    new_holedata = DbRankData47Hole(
        product=request.product, 
        lot=request.lot,
        holecount=request.holecount,
        angleAv=request.angleAv,
        angleSD=request.angleSD,
        angle25=request.angle25,
        angle75=request.angle75,
        angleMax=request.angleMax,
        angleMin=request.angleMin,
        angleNGMax=request.angleNGMax,
        NGpositionX=request.NGpositionX,
        NGpositionY=request.NGpositionY,
        NGfilename=request.NGfilename,
        OK=request.OK,
        NG=request.NG,
        speed=request.speed
    )
    db.add(new_holedata)
    db.commit()
    db.refresh(new_holedata)
    return new_holedata


def delete(db: Session, id: int):
    sensor = db.query(DbRankData47Hole).filter(DbRankData47Hole.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})



def read_holedata47(db: Session):
    return db.query(DbRankData47Hole).all()



def read_holedata47_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbRankData47Hole).filter(DbRankData47Hole.created_date.between(start, end)).all()

 
def read_holedata47_by_id(db: Session, id: int):
    return db.query(DbRankData47Hole).filter(DbRankData47Hole.id == id).first()



def product_holedata_group(db:Session):
    return db.execute(text("select product from RankData47Hole group by product")).all()


def lot_groupby_product(db:Session, product:str):
    return db.execute(text("select lot from RankData47Hole where product='{}' group by lot".format(product))).all()


def holedata_bylot(db:Session, lot:str):
    return db.execute(text("select * from RankData47Hole where lot='{}'".format(lot))).all()


def holedata_bylot_summary(db:Session, lot:str):
    sql = "select strftime('%Y-%m-%d %H', created_date) as dateHour, \
            count(id) as count, sum(IIf(OK=1 and NG=0,1,0)) as OK, \
                sum(IIf(OK=0 and NG=1,1,0)) as NG, \
                    sum(IIf(OK=1 and NG=1,1,0)) as Re \
                        from RankData47Hole \
                            where lot='{}'\
                                GROUP BY dateHour\
                                    ".format(lot)
    return db.execute(text(sql)).all()