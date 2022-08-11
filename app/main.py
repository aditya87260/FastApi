import re
from fastapi import FastAPI

from blog import oauth2
from blog.database import engine
from blog.routers import blog,user,authentication
from  blog import models


app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





    
