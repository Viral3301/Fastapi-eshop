from typing import List
from fastapi import FastAPI,Request,Depends,File,UploadFile,Form,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from database import get_async_session,AsyncSession,User,engine
from eshop.models import *
from eshop.exceptions import Unauthorized_redirect, not_found_error
import shutil
import math
from eshop.routers.create_router import pagination
from sqlalchemy import select,update
from fastapi_users import fastapi_users,FastAPIUsers
from eshop.auth.auth import auth_backend
from eshop.auth.manager import get_user_manager
from eshop.schemas import UserRead,UserCreate,ProductDTO
from sqladmin import Admin, ModelView
import pandas as pd
from admin_models import *
from redis import asyncio as aioredis
import json
from fastapi.encoders import jsonable_encoder
from pydantic.json import pydantic_encoder
from config import REDIS_HOST
# from admin_models import AccesoryAdmin,VehicleAdmin,CategoryAdmin
from eshop.routers.create_router import create_router
from eshop.routers.search_router import search_router

async def lifespan(app):
    global redis
    redis = await aioredis.from_url(f'redis://{REDIS_HOST}')
    yield
    await redis.close()

app = FastAPI(title='Drive-moto',lifespan=lifespan)

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


admin.add_view(UserAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(AttributesAdmin)
admin.add_view(ValuesAdmin)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/content_img", StaticFiles(directory='content_img'),name='content_img')

templates = Jinja2Templates(directory="templates")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(create_router)
app.include_router(search_router)

current_user = fastapi_users.current_user()


favicon_path = 'static/img/favicon.svg'



@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.get("/",tags=['nav'])
async def home(request: Request,session: AsyncSession = Depends(get_async_session)):
    
    cache = await redis.get('accessories')
    
    if cache is not None:
        print('cache')
        return templates.TemplateResponse('home.html',{'request':request,'accessories': json.loads(cache)})
    else:
        Accessories = await session.execute(select(Products).where(Products.category.in_([1,2])).order_by(Products.id))
        Accessories_scalars = Accessories.scalars().all()
        resultDTO = [ProductDTO.model_validate(row, from_attributes=True) for row in Accessories_scalars]
        print('not_cache')
        await redis.set('accessories',json.dumps(resultDTO,default=pydantic_encoder),ex=120)
        return templates.TemplateResponse('home.html',{'request':request,'accessories': resultDTO})


@app.get("/category/{category_id}/",tags=['nav'])
async def get_category(request: Request, category_id: int,page: int = 1,session: AsyncSession = Depends(get_async_session)):
    
    
    
    content_raw = await session.execute(select(Products).where(Products.category == category_id))
    data = content_raw.scalars().all()
    
    start,end,page,pages_total = pagination(data,page)

    raw_category_name = await session.execute(select(Category).where(Category.id == category_id))
    category_name = raw_category_name.scalars().all()

    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"category_id":category_id,"page_num": page,"category_name":category_name},)


@app.get("/product/{category_id}/{product_id}" ,tags=['nav'])
async def product_detail(request: Request,category_id : int,product_id: int,session: AsyncSession = Depends(get_async_session)):

    stmt = select(Products.id,Products.title,Products.image,Products.product_code,Products.price,ProductAttributes.title,AttributeValue.value).join(ProductAttributes, ProductAttributes.id == AttributeValue.attribute_id).join(Products).where(Products.id == product_id).order_by(ProductAttributes.id)
    content_raw = await session.execute(stmt)

    df = pd.DataFrame(content_raw)
    
    if df.empty:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('product-page.html',{'request':request,'product':df.to_dict()})

@app.get("/login",tags=['nav'])
async def login(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('login.html',{'request':request})

@app.get("/registration",tags=['nav'])
async def register(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('registration.html',{'request':request})


@app.get("/profile",tags=['nav'])
def protected_route(request: Request,session: AsyncSession = Depends(get_async_session),user: User = Depends(current_user)):
    return templates.TemplateResponse('profile.html',{'request':request,'user': user})

@app.get('/cart',tags=['nav'])
async def shopping_cart(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('cart.html',{"request":request})

@app.post("/changepfp",tags=['nav'])
async def ChangePfp(request: Request,image: UploadFile = File(...),user: User = Depends(current_user),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_image = await session.execute(update(User).where(User.id == user.id).values(image=image.filename))
    await session.commit()
    return image


@app.exception_handler(404)
def Not_found_exception_handler(request: Request, exc: HTTPException):
    return not_found_error(request, exc)

@app.exception_handler(401)
def Unauthorized_exception_handler(request: Request, exc: HTTPException):
    return Unauthorized_redirect(request, exc)
