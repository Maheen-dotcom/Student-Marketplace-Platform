from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name:str
    email:str
    password:str
    phone:str
    role:str

class LoginSchema(BaseModel):
    email:str
    password:str

class ProductCreate(BaseModel):
    title:str
    description:str
    category:str
    price:float
    seller_name:str