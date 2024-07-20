from typing import Annotated, List
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database import get_async_session
from eshop.routers.create_router import pagination
from sqlalchemy import select, and_
from eshop.models import Products,AttributeValue
from database import get_async_session,AsyncSession


search_router = APIRouter(prefix="/search",tags=["search"])

templates = Jinja2Templates(directory="templates")

@search_router.get("/search_by_name/")
async def search_by_name(request: Request, name: str,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    query = select(Products).where(Products.title.like(f'{name.capitalize()}%'))

    content_raw = await session.execute(query)
    data = content_raw.scalars().all()

    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('search_catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@search_router.get("/search_by_code/")
async def search_by_id(request: Request, code: int,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    query = select(Products).where(Products.product_code == code)
    content_raw = await session.execute(query)
    data = content_raw.scalars().all()

    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('search_catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num, 'search_type': 'search_by_code','code': code},)

@search_router.get("/search_by_manufacturer/")
async def search_by_manufacturer(request: Request, manufacturer: str,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    
    query = select(Products).join(AttributeValue, AttributeValue.product_id == Products.id ).where(and_(AttributeValue.attribute_id == 1 ,AttributeValue.value == manufacturer.capitalize()))
    content_raw = await session.execute(query)
    data = content_raw.scalars().all()


    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)


    return templates.TemplateResponse('search_catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)