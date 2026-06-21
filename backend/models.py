from sqlalchemy import Column,Integer,String,Text,Numeric,DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    phone = Column(String)
    role = Column(String)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    price = Column(Numeric)
    seller_name = Column(String)
    created_at = Column(DateTime(timezone=True),server_default=func.now())