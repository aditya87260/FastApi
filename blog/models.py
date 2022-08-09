from sqlalchemy import Column, Integer, String
from .database import Base

class Blog(Base):
    __tablename__ = 'blogs'  #give any table name you want 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    #published = Column(String(50), nullable=False)

    