import uuid
from typing import Optional
from fastapi import File, Form, UploadFile
from fastapi_users import schemas
from pydantic import BaseModel,ConfigDict

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    
    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        is_active: Optional[bool] = True,
        is_superuser: Optional[bool] = False,
        is_verified: Optional[bool] = False,
    ):
        return cls(username=username,email=email,password=password,is_active=is_active,is_superuser=is_superuser,is_verified=is_verified)

class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    image : str = 'default_pfp.png'
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        is_active: Optional[bool] = True,
        is_superuser: Optional[bool] = False,
        is_verified: Optional[bool] = False,
    ):
        return cls(username=username,email=email,password=password,is_active=is_active,is_superuser=is_superuser,is_verified=is_verified)
    
class Create_product(BaseModel):
    title : str
    category: int
    product_code: int
    price: int
    sale: bool

    @classmethod
    def as_form(
        cls,
        title : str = Form(...),
        category: int = Form(...),
        product_code: int = Form(...),
        price: int = Form(...),
        sale: bool = Form(...),
    ):
        return cls(title=title,category=category,product_code=product_code,price=price,sale=sale)
    

class ProductDTO(BaseModel):
    id : int
    title: str
    category: int
    product_code: int
    image: str
    price: int
    sale: bool