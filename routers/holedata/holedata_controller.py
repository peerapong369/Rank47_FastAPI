from cProfile import label
from tkinter.tix import COLUMN
from turtle import speed
from unittest import result
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
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

