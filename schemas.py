import uuid
from typing import Optional
from fastapi import Form
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
    
# class Operation(BaseModel):
#   model_config: ConfigDict(from_attributes=True)

#   id: int
#   image: str
#   title: str
#   image: str
#   price: int
#   category: int


# class Product(BaseModel):
#   model_config: ConfigDict(from_attributes=True)

#   title: str
#   image: str
#   price: int
#   product_code: int
#   material: Optional[str] = None
#   color: Optional[str] = None
#   guarantee: Optional[int] = None
#   company: Optional[str] = None
#   seats: Optional[int] = None
#   engine: Optional[int] = None
#   engine_type: Optional[str] = None
#   year: Optional[int] = None
