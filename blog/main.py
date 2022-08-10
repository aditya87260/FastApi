from fastapi import FastAPI
from .database import engine
from .routers import blog,user
from .import models

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)



    
