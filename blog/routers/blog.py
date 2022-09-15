from fastapi import APIRouter,Depends,status, HTTPException
from typing import List
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session
from ..repo import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,current_user: schemas.User = Depends(oauth2.get_current_user),  db: Session = Depends(get_db)):
    return blog.delete(id,db)

@router.get("/{id}",status_code=200, response_model=schemas.ShowBlog)
def get_blog(id,current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.show_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,  request:schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user),db: Session = Depends(get_db)):
    return blog.update(id,request,db)

