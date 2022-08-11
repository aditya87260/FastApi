from fastapi import APIRouter,Depends
from blog import database,schemas,models
from sqlalchemy.orm import Session
from blog.repository import user

router=APIRouter(tags=['Users'],prefix="/user")
get_db=database.get_db

@router.post('/',response_model=schemas.showUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schemas.showUser)

def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)