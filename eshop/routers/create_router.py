import shutil
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi import FastAPI,Request

from eshop.models import Accessories, Category, Vehicles
from database import get_async_session

create_router = APIRouter(prefix='/create',tags=["create"])

@create_router.post("/accessory")
async def Create_acessory(request: Request,title: str,price: int,manufacturer: str ,amount_in_stock: int,sale: bool,category:int,material: str,guarantee: int,color: str,company:str,rating: float,image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_accesory = Accessories(title=title,image=image.filename,price=price,manufacturer=manufacturer,amount_in_stock=amount_in_stock,sale=sale,category=category,rating = rating,material=material,guarantee=guarantee,color=color,company=company)
    session.add(new_accesory)
    await session.commit()
    return {'response': "good"}

@create_router.post("/category")
async def Create_category(request: Request,name: str,session: AsyncSession = Depends(get_async_session)):
    new_category = Category(name=name)
    session.add(new_category)
    await session.commit()
    return {'response': "good"}

@create_router.post("/vehicle")
async def Create_vehicle(request: Request,title: str,price: int,manufacturer: str ,seats:int,engine:int,engine_type: str,year:int,amount_in_stock: int,sale: bool,category:int,image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_vehicle = Vehicles(title=title,image=image.filename,price=price,manufacturer=manufacturer,seats=seats,engine=engine,engine_type=engine_type,year=year,amount_in_stock=amount_in_stock,sale=sale,category=category)
    session.add(new_vehicle)
    await session.commit()
    return {'response': "good"}








def pagination(data,page):
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page - 1) * 12
    end = start + 12
    return start,end,page,pages_total