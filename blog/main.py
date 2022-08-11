import re
from fastapi import FastAPI

from blog import oauth2
from .database import engine
from .routers import blog,user,authentication
from .import models


app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





    
