from typing import Annotated, List
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database import get_async_session
from eshop.models import Accessories, Vehicles
from eshop.routers.create_router import pagination
from sqlalchemy import select
from database import get_async_session,AsyncSession

from eshop.schemas import Operation

search_router = APIRouter(prefix="/search",tags=["search"])

templates = Jinja2Templates(directory="templates")

@search_router.post("/search_by_name" , response_model=List[Operation])
async def search_by_name(request: Request, name: Annotated[str,Form()],page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.title.like(f'{name.capitalize()}%'))
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.title.like(f'{name.capitalize()}%'))
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()

    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@search_router.post("/search_by_code" , response_model=List[Operation])
async def search_by_id(request: Request, code: Annotated[int,Form()],page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.product_code == code)
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.product_code == code)
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()

    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@search_router.post("/search_by_manufacturer", response_model=List[Operation])
async def search_by_manufacturer(request: Request, manufacturer: Annotated[str,Form()],page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.manufacturer == manufacturer.capitalize())
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.manufacturer == manufacturer.capitalize())
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()


    start,end,page_num,pages_total = pagination(data,page_num)

    if data ==[]:
        raise HTTPException(status_code=404)


    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)