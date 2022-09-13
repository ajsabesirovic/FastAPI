from sqlalchemy.orm import Session
from blog import schemas
from .. import models
from fastapi import HTTPException, status
from ..hashing import Hash

def show_user(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"User with id {id} does not exist")
    return user

def create_user(request:schemas.User,db:Session):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user