from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.Hole.hole_models import HoleDataBase, HoleDataDisplayBase, ProductGroupDisplay, ProductLotDisplay

from routers.holedata import holedata_controller
from fastapi.responses import FileResponse
from PIL import Image
from numpy import asarray



router = APIRouter(prefix="/holedata47", tags=["holedata47"])


@router.get("/", response_model=List[HoleDataDisplayBase])
def get_all_rankdata(db: Session = Depends(get_db)):
    return holedata_controller.read_holedata47(db)



@router.get("/last_start{start}:end{end}", response_model=List[HoleDataDisplayBase])
def get_last_rankdata(start: str, end: str, db: Session = Depends(get_db)):
    return holedata_controller.read_holedata47_last(db, start, end)


@router.get("/{id}")
def rankdata_by_id(id: int, db:Session=Depends(get_db)):
    return holedata_controller.read_holedata47_by_id(db, id)




@router.post("/")
def create_rankdata(request: HoleDataBase, db: Session = Depends(get_db)):
    return holedata_controller.create(db, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return holedata_controller.delete(db, id)



@router.get("/productgroupbyproduct/")
def product_group_byProduct(db:Session=Depends(get_db)):
    product = holedata_controller.product_holedata_group(db)
    return {"ProductGroup":product}


@router.get("/lotgroupbyproduct/{product}")
def lot_group_byProduct(product:str, db:Session=Depends(get_db)):
    Lot = holedata_controller.lot_groupby_product(db, product)
    return {"LotGroup":Lot}


@router.get("/holedatabylot/{lot}")
def holedata_bylot(lot:str, db:Session=Depends(get_db)):
    data = holedata_controller.holedata_bylot_summary(db, lot)
    return {"HoleData":data}



@router.get("/sampleimagefromfile/")
def show_img_fromfile():
    imgfile = r'C:\Users\peerapong\Desktop\Hole_Angle_NG\ABCD-5555\EFG9883437850930\NG94.943728.bmp'
    image = asarray(Image.open(imgfile))
    image = image.tolist()
    return FileResponse(imgfile)
    #return {"image":image[0]}