from fastapi import FastAPI,Request,Depends,File,UploadFile
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import AsyncSession, engine,async_session
from eshop.models import *
import shutil
from sqlalchemy import select

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/content_img", StaticFiles(directory='content_img'),name='content_img')

templates = Jinja2Templates(directory="templates")


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@app.get("/")
async def home(request: Request,session: AsyncSession = Depends(get_session)):
    raw_backpacks = await session.execute(select(Accessories))
    raw_swimsuits = await session.execute(select(Accessories).where(Accessories.category == 2))
    backpacks = raw_backpacks.scalars().all()
    swimsuits = raw_swimsuits.scalars().all()
    return templates.TemplateResponse('home.html',{'request':request,'backpacks': backpacks,'swimsuits':swimsuits})

@app.get("/category/{category_id}/{page_num}/")
async def home(request: Request, category_id: int,page_num: int = 1,session: AsyncSession = Depends(get_session)):
    raw_data = await session.execute(select(Vehicles).where(Vehicles.category == category_id))
    data = raw_data.scalars().all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"category_id":category_id,"page_num": page_num},)

@app.get("/product/{product_id}")
async def home(request: Request,product_id: int,session: AsyncSession = Depends(get_session)):
    raw_product = await session.execute(select(Vehicles).where(Vehicles.id == product_id))
    product = raw_product.scalars().all()
    return templates.TemplateResponse('product-page.html',{'request':request,'product':product})

@app.get("/login")
async def home(request: Request,session: AsyncSession = Depends(get_session)):
    return templates.TemplateResponse('login.html',{'request':request})

@app.get("/registration")
async def home(request: Request,session: AsyncSession = Depends(get_session)):
    return templates.TemplateResponse('registration.html',{'request':request})