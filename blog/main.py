from fastapi import FastAPI, Depends, status, Response, HTTPException
from .database import engine,SessionLocal
from .  import schemas, models
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/')
def all( db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}",status_code=200)
def get_blog(id,response: Response ,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"blog with id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"blog with id {id} is not available"}
    return blog