from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.RankData47.rankdata47_model import RankDataBase, RankDataDisplayBase, ProductGroupDisplay

from routers.RankData47 import rankdata47_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/rankdata47", tags=["rankdata47"])


@router.get("/", response_model=List[RankDataDisplayBase])
def get_all_rankdata(db: Session = Depends(get_db)):
    return rankdata47_controller.read_rankdata47(db)



@router.get("/last_start{start}:end{end}", response_model=List[RankDataDisplayBase])
def get_last_rankdata(start: str, end: str, db: Session = Depends(get_db)):
    return rankdata47_controller.read_rankdata47_last(db, start, end)


@router.get("/{id}")
def rankdata_by_id(id: int, db:Session=Depends(get_db)):
    return rankdata47_controller.read_rankdata47_by_id(db, id)


@router.get("/rank_productgroup/", response_model=List[ProductGroupDisplay])
def productgroup(db: Session=Depends(get_db)):
    return rankdata47_controller.product_group(db)


@router.get("/rank_lotgroup/{product}")
def lotgroup(product:str, db: Session=Depends(get_db)):
    return rankdata47_controller.productlot_group(db, product)


@router.get("/rankdataby/{product},{lot}")
def rankdatabyproduct_lot(product:str, lot:str,speed:float, db:Session=Depends(get_db)):
    return rankdata47_controller.databygroup_lot(db, product, lot)


@router.get("/productivityHour/{product},{lot}")
def productivityperhour(product:str, lot:str, db: Session=Depends(get_db)):
    return rankdata47_controller.productPerHourbyLot(db, product, lot)

@router.get("/productivityMin/{product},{lot},{date},{hour}")
def productivitypermin(product:str, lot:str,date:str, hour:str, db: Session=Depends(get_db)):
    return rankdata47_controller.productPerMinbyLot(db, product, lot, date, hour)


@router.get("/dategroupbylot/{product},{lot}")
def dategroupbylot(product:str, lot:str, db: Session=Depends(get_db)):
    return rankdata47_controller.dateGroupbyLot(db, product, lot)

@router.post("/")
def create_rankdata(request: RankDataBase, db: Session = Depends(get_db)):
    return rankdata47_controller.create(db, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return rankdata47_controller.delete(db, id)


