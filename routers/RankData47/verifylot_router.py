from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.RankData47.verifylot_model import VerifyLotDataBase, VerifyLotDataDisplayBase

from routers.RankData47 import verifylot_controller

router = APIRouter(prefix="/verfylotdata", tags=["verfylotdata"])



@router.post("/")
def create_rankdata(request: VerifyLotDataBase, db: Session = Depends(get_db)):
    return verifylot_controller.createverifylot(db, request)

@router.get("/{id}")
def verifylotdata_by_id(id: int, db:Session=Depends(get_db)):
    return verifylot_controller.read_verifylotdata_by_id(db, id)