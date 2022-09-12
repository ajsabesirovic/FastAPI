from typing import List
from fastapi import FastAPI, Depends, status, HTTPException

from blog.routers import user
from .database import engine
from . import models
from .routers import blog

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)
