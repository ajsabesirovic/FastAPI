from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World AJSAAA"}


@app.get("/about")
def about():
    return {'about': "this is about"}