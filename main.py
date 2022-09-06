from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


# @app.get('/blog')
# def published (limit:int,published: bool) :
#     if published:
#         return {'data':f'{limit} blogs'}
#     else:
#         return {'data':f'{limit+1992039} blogs'}


@app.get('/blog/unpublished')
def unpublished () :
    return {'data':'all unpublished blogs'}

@app.get("/blog/{id}")
def about(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {'data': {'1','2'}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {'data':f'blog {request.title}'}
