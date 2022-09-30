from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.RankData47.verify_model import VerifyDataBase, VerifyDataDisplayBase

from routers.RankData47 import verify_controller

router = APIRouter(prefix="/verfyrank47", tags=["verifyrank47"])


@router.get("/", response_model=List[VerifyDataDisplayBase])
def get_all_verifydata(db: Session = Depends(get_db)):
    return verify_controller.read_verifydata(db)



@router.get("/last_start{start}:end{end}", response_model=List[VerifyDataDisplayBase])
def get_last_verifydata(start: str, end: str, db: Session = Depends(get_db)):
    return verify_controller.read_verifydata_last(db, start, end)


@router.get("/{id}")
def rankdata_by_id(id: int, db:Session=Depends(get_db)):
    return verify_controller.read_verifydata_by_id(db, id)


@router.get("/productgroup/")
def productgroup(db: Session=Depends(get_db)):
    return verify_controller.product_group(db)


@router.get("/lotgroup/{product}")
def lotgroup(product:str, db: Session=Depends(get_db)):
    return verify_controller.lot_group(db, product)


@router.get("/databylot/{product},{lot}", response_model=List[VerifyDataDisplayBase])
def verifydataproduct_lot(product:str, lot:str, db:Session=Depends(get_db)):
    return verify_controller.readby_lot(db, product, lot)


@router.post("/")
def create_rankdata(request: VerifyDataBase, db: Session = Depends(get_db)):
    return verify_controller.create(db, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return verify_controller.delete(db, id)
