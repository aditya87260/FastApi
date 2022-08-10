from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True
    

class User(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name: str
    email: str
    blogs:List[Blog]=[]
    
    class Config:
        orm_mode = True

class ShowBlog(Blog):
    title: str
    body: str
    creator: showUser
    class Config:
        orm_mode = True   # we are telling that we are using sqlalchemy orm

class Login(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True