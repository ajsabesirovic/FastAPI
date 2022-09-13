from fastapi import APIRouter,Depends,status, HTTPException
from .. import schemas,models,database 
from sqlalchemy.orm import Session
from ..repo import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show_user(id,db)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)
