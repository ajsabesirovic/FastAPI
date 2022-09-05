from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get('/blog/unpublished')
def unpublished () :
    return {'data':'all unpublished blogs'}

@app.get("/blog/{id}")
def about(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {'data': {'1','2'}}
