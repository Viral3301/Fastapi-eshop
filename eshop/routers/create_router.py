import shutil
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi import FastAPI,Request

from eshop.models import Products, Category ,ProductAttributes, AttributeValue
from eshop.schemas import Create_product
from database import get_async_session

create_router = APIRouter(prefix='/create',tags=["create"])

@create_router.post("/product")
async def Create_product(request: Request,product: Create_product = Depends(Create_product.as_form),image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_product = Products(title=product.title,image=image.filename,price=product.price,category=product.category,product_code=product.product_code,sale=product.sale)
    session.add(new_product)
    await session.commit()
    return {'response': "good"}

@create_router.post("/category")
async def Create_category(request: Request,name: str,session: AsyncSession = Depends(get_async_session)):
    new_category = Category(name=name)
    session.add(new_category)
    await session.commit()
    return {'response': "good"}

@create_router.post("/attribute")
async def Create_product_attribute(request: Request,title: str,session: AsyncSession = Depends(get_async_session)):
    new_attribute = ProductAttributes(title=title)
    session.add(new_attribute)
    await session.commit()
    return {'response': "good"}

@create_router.post("/value")
async def Create_attribute_value(request: Request,product_id: int,attribute_id: int,value: str,session: AsyncSession = Depends(get_async_session)):
    new_attribute_value = AttributeValue(product_id=product_id,attribute_id=attribute_id,value=value)
    session.add(new_attribute_value)
    await session.commit()
    return {'response': "good"}

# @create_router.post("/vehicle")
# async def Create_vehicle(request: Request,title: str,price: int,manufacturer: str ,seats:int,engine:int,engine_type: str,year:int,amount_in_stock: int,sale: bool,category:int,image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
#     with open (f'content_img/{image.filename}',"wb") as buffer:
#         shutil.copyfileobj(image.file,buffer)
#     new_vehicle = Vehicles(title=title,image=image.filename,price=price,manufacturer=manufacturer,seats=seats,engine=engine,engine_type=engine_type,year=year,amount_in_stock=amount_in_stock,sale=sale,category=category)
#     session.add(new_vehicle)
#     await session.commit()
#     return {'response': "good"}








def pagination(data,page):
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page - 1) * 12
    end = start + 12
    return start,end,page,pages_total