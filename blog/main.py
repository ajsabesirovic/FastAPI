from pydantic import BaseModel
from fastapi import FastAPI
from . import schemas
from enum import Enum

class ModelName(str, Enum):
    alexnet = "ajsa"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {'modelname':model_name, 'value':model_name.value}
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

@app.post('/blog')
def create(request: schemas.Blog):
    return request

