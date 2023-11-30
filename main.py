from fastapi import FastAPI,Request,Depends,File,UploadFile,Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import starlette.status as status
from sqlalchemy.orm import Session, load_only
from database import get_async_session,AsyncSession,User,engine
from eshop.models import *
import shutil
import requests
from sqlalchemy import select,insert,update,and_
from fastapi_users import fastapi_users,FastAPIUsers
from auth import auth_backend
from manager import get_user_manager
from schemas import UserRead,UserCreate
from fastapi.responses import RedirectResponse
from fastapi_users.password import PasswordHelper
from sqladmin import Admin, ModelView
from admin_models import AccesoryAdmin,VehicleAdmin,CategoryAdmin
from typing import List,Annotated
from schemas import Operation,Product


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
    raw_backpacks = await session.execute(select(Accessories).where(Accessories.category == 1))
    raw_swimsuits = await session.execute(select(Accessories).where(Accessories.category == 2))
    backpacks = raw_backpacks.scalars().all()
    swimsuits = raw_swimsuits.scalars().all()
    return templates.TemplateResponse('home.html',{'request':request,'backpacks': backpacks,'swimsuits':swimsuits})

@app.get("/category/{category_id}/{page_num}/")
async def get_category(request: Request, category_id: int,page_num: int = 1,session: AsyncSession = Depends(get_async_session)):

    if category_id >2:
        stmt = select(Vehicles.id,Vehicles.title,Vehicles.category,Vehicles.image,Vehicles.price,Vehicles.product_code,Vehicles.seats,Vehicles.engine_type,Vehicles.manufacturer,Vehicles.engine,Vehicles.year,Vehicles.rating).where(Vehicles.category == category_id)
    else:
        stmt = select(Accessories.id,Accessories.title,Accessories.category,Accessories.image,Accessories.price,Accessories.product_code,Accessories.guarantee,Accessories.material,Accessories.color,Accessories.company,Accessories.manufacturer,Accessories.rating).where(Accessories.category == category_id)
    content_raw = await session.execute(stmt)
    data = content_raw.all()

    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12

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

    return templates.TemplateResponse('product-page.html',{'request':request,'product':product})

@app.get("/login")
async def login(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('login.html',{'request':request})

@app.get("/registration")
async def register(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse('registration.html',{'request':request})

@app.post("/create")
async def CreateAcessory(request: Request,title: str,price: int,manufacturer: str ,amount_in_stock: int,sale: bool,category:int,rating: float,image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_accesory = Accessories(title=title,image=image.filename,price=price,manufacturer=manufacturer,amount_in_stock=amount_in_stock,sale=sale,category=category,rating = rating)
    session.add(new_accesory)
    await session.commit()
    return {'response': "good"}

@app.post("/createcategory")
async def CreateCategory(request: Request,name: str,session: AsyncSession = Depends(get_async_session)):
    new_category = Category(name=name)
    session.add(new_category)
    await session.commit()
    return {'response': "good"}

@app.post("/createvehicle")
async def CreateVehicle(request: Request,title: str,price: int,manufacturer: str ,seats:int,engine:int,engine_type: str,year:int,amount_in_stock: int,sale: bool,category:int,image: UploadFile = File(...),session: AsyncSession = Depends(get_async_session)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_vehicle = Vehicles(title=title,image=image.filename,price=price,manufacturer=manufacturer,seats=seats,engine=engine,engine_type=engine_type,year=year,amount_in_stock=amount_in_stock,sale=sale,category=category)
    session.add(new_vehicle)
    await session.commit()
    return {'response': "good"}


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

@app.post("/search_by_name/" , response_model=List[Operation])
async def search_by_name(request: Request, name: str,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.title.like(f'{name.capitalize()}%'))
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.title.like(f'{name.capitalize()}%'))
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@app.post("/search_by_id/" , response_model=List[Operation])
async def search_by_id(request: Request, code: int,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.product_code == code)
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.product_code == code)
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@app.post("/search_by_manufacturer/", response_model=List[Operation])
async def search_by_manufacturer(request: Request, manufacturer: Annotated[str,Form()],page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    
    stmt_1 = select(Accessories.id,Accessories.title,Accessories.image,Accessories.price,Accessories.category).where(Accessories.manufacturer == manufacturer.capitalize())
    stmt_2 = select(Vehicles.id,Vehicles.title,Vehicles.image,Vehicles.price,Vehicles.category).where(Vehicles.manufacturer == manufacturer.capitalize())
    query = stmt_1.union(stmt_2)
    content_raw = await session.execute(query)
    data = content_raw.all()


    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)
