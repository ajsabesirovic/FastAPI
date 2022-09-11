from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from .database import engine, SessionLocal
from . import schemas, models
from sqlalchemy.orm import Session
from .hashing import Hash

app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/',response_model=List[schemas.ShowBlog])
def all( db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blogs/{id}",status_code=200, response_model=schemas.ShowBlog)
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"Blog with id {id} not available")
    return blog

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return 'updated'

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog                  

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}

@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user