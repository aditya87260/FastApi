from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

# creating router  # Optional is used to give optional parameters
@app.get('/blog')      # Here ('/blog') is the path and get is a operation and @app is a path operation decorator
def index(limit=10,published:bool=True,sort:Optional[str]=None): 
    if published:   # it is path operation function beacuse it is a function which we are going to perform on ('/') path with get operation
        return {"data": f"{limit} published blogs from the db"}  #limit is a query parameter
    else:
        return {"data": f"{limit} blogs from the db"}
       



@app.get('/blog/unpublished')     # Here ('/about') is the path 
def unpublished():
    return {"data":"all unpublished blogs"}



@app.get('/blog/{id}')    # Here {id} is a path parameter snd here we are taking id value as int and dynamically i.e. we can give any ids as we want
def show(id:int):
    return {"data": id} # fetch blog with id=id


@app.get('/blog/{id}/comments')    
#fetch comments of blog with id=id
def comments(id):
    return {"data":{'1','2'}}


#Creating Request Body using pydantic BaseModel
class Blog(BaseModel):
    title:str
    body:str    
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {"data":f"Blog is created with title {blog.title}"} # it is a response body so it will return as response
    





