from fastapi import FastAPI,Request,Depends,File,UploadFile,Form,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from database import get_async_session,AsyncSession,User,engine
from eshop.models import *
from eshop.handlers import not_found_error
import shutil
from eshop.router import pagination
from sqlalchemy import select,insert,update,and_
from fastapi_users import fastapi_users,FastAPIUsers
from eshop.auth.auth import auth_backend
from eshop.auth.manager import get_user_manager
from eshop.schemas import UserRead,UserCreate,Operation,Product
from sqladmin import Admin, ModelView
from admin_models import AccesoryAdmin,VehicleAdmin,CategoryAdmin
from typing import List,Annotated
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from eshop.router import create_router
from redis import asyncio as aioredis
import redis



app = FastAPI()

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


admin.add_view(UserAdmin)
admin.add_view(VehicleAdmin)
admin.add_view(AccesoryAdmin)
admin.add_view(CategoryAdmin)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/content_img", StaticFiles(directory='content_img'),name='content_img')

templates = Jinja2Templates(directory="templates")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(create_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/")
async def home(request: Request,session: AsyncSession = Depends(get_async_session)):
    raw_backpacks = await session.execute(select(Accessories).where(Accessories.category == 1).order_by(Accessories.id))
    raw_swimsuits = await session.execute(select(Accessories).where(Accessories.category == 2).order_by(Accessories.id))
    backpacks = raw_backpacks.scalars().all()
    swimsuits = raw_swimsuits.scalars().all()
    return templates.TemplateResponse('home.html',{'request':request,'backpacks': backpacks,'swimsuits':swimsuits})

@app.get("/category/{category_id}/page={page_num}/")
async def get_category(request: Request, category_id: int,page_num: int = 1,session: AsyncSession = Depends(get_async_session)):

    if category_id >2:
        stmt = select(Vehicles.id,Vehicles.title,Vehicles.category,Vehicles.image,Vehicles.price,Vehicles.product_code,Vehicles.seats,Vehicles.engine_type,Vehicles.manufacturer,Vehicles.engine,Vehicles.year,Vehicles.rating).where(Vehicles.category == category_id)
    else:
        stmt = select(Accessories.id,Accessories.title,Accessories.category,Accessories.image,Accessories.price,Accessories.product_code,Accessories.guarantee,Accessories.material,Accessories.color,Accessories.company,Accessories.manufacturer,Accessories.rating).where(Accessories.category == category_id)
    content_raw = await session.execute(stmt)
    data = content_raw.all()

    start,end,page_num,pages_total = pagination(data,page_num)

    raw_category_name = await session.execute(select(Category).where(Category.id == category_id))
    category_name = raw_category_name.scalars().all()

    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"category_id":category_id,"page_num": page_num,"category_name":category_name},)

@app.get("/product/{category_id}/{product_id}" , response_model=List[Product])
async def product_detail(request: Request,category_id : int,product_id: int,session: AsyncSession = Depends(get_async_session)):
    if category_id >2:
        stmt = select(Vehicles.title,Vehicles.category,Vehicles.image,Vehicles.price,Vehicles.product_code,Vehicles.seats,Vehicles.engine_type,Vehicles.manufacturer,Vehicles.engine,Vehicles.year,Vehicles.rating).where(Vehicles.id == product_id, Vehicles.category == category_id)
    else:
        stmt = select(Accessories.title,Accessories.category,Accessories.image,Accessories.price,Accessories.product_code,Accessories.guarantee,Accessories.material,Accessories.color,Accessories.company,Accessories.manufacturer,Accessories.rating).where(Accessories.id == product_id, Accessories.category == category_id)
    content_raw = await session.execute(stmt)
    product = content_raw.all()
    if product == []:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('product-page.html',{'request':request,'product':product})

@app.get("/login")
async def login(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('login.html',{'request':request})

@app.get("/registration")
async def register(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('registration.html',{'request':request})


@app.get("/profile")
def protected_route(request: Request,session: AsyncSession = Depends(get_async_session),user: User = Depends(current_user)):
    return templates.TemplateResponse('profile.html',{'request':request,'user': user})

@app.post("/changepfp")
async def ChangePfp(request: Request,image: UploadFile = File(...),user: User = Depends(current_user),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_image = await session.execute(update(User).where(User.id == user.id).values(image=image.filename))
    await session.commit()
    return image

@app.post("/search_by_name" , response_model=List[Operation])
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

@app.post("/search_by_code" , response_model=List[Operation])
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

@app.post("/search_by_manufacturer", response_model=List[Operation])
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


@app.exception_handler(404)
def not_found_exception_handler(request: Request, exc: HTTPException):
    return not_found_error(request, exc)
