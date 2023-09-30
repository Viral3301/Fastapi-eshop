from fastapi import FastAPI,Request,Depends,File,UploadFile,Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import starlette.status as status
from sqlalchemy.orm import Session
from database import get_async_session,AsyncSession,User,engine
from eshop.models import *
import shutil
import requests
from sqlalchemy import select,insert,update
from fastapi_users import fastapi_users,FastAPIUsers
from auth import auth_backend
from manager import get_user_manager
from schemas import UserRead,UserCreate
from fastapi.responses import RedirectResponse
from fastapi_users.password import PasswordHelper
from sqladmin import Admin, ModelView
from admin_models import AccesoryAdmin,VehicleAdmin


app = FastAPI()

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


admin.add_view(UserAdmin)
admin.add_view(VehicleAdmin)
admin.add_view(AccesoryAdmin)


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


@app.post('/register')
async def reg(request:Request,session: AsyncSession = Depends(get_async_session),userdata = Depends(UserCreate.as_form)):
    hashed_password = PasswordHelper().context.hash(str(userdata.password))
    new_user = User(username=userdata.username,email=userdata.email,hashed_password=hashed_password,is_active=userdata.is_active,is_superuser=userdata.is_superuser,is_verified=userdata.is_verified)
    session.add(new_user)
    await session.commit()
    return RedirectResponse(url='login',status_code=status.HTTP_303_SEE_OTHER)

@app.get("/")
async def home(request: Request,session: AsyncSession = Depends(get_async_session)):
    raw_backpacks = await session.execute(select(Accessories).where(Accessories.category == 1))
    raw_swimsuits = await session.execute(select(Accessories).where(Accessories.category == 2))
    backpacks = raw_backpacks.scalars().all()
    swimsuits = raw_swimsuits.scalars().all()
    return templates.TemplateResponse('home.html',{'request':request,'backpacks': backpacks,'swimsuits':swimsuits})

@app.get("/category/{category_id}/{page_num}/")
async def get_category(request: Request, category_id: int,page_num: int = 1,session: AsyncSession = Depends(get_async_session)):
    raw_data = await session.execute(select(Vehicles).where(Vehicles.category == category_id))
    data = raw_data.scalars().all()

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

@app.get("/product/{product_id}")
async def product_detail(request: Request,product_id: int,session: AsyncSession = Depends(get_async_session)):
    raw_product = await session.execute(select(Vehicles).where(Vehicles.id == product_id))
    product = raw_product.scalars().all()
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

@app.get("/search_by_name/")
async def Search_By_Name(request: Request, name: str,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    content_raw = await session.execute(select(Accessories).where(Accessories.title.like(f'{name}%')))
    data = content_raw.scalars().all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@app.get("/search_by_id/")
async def Search_By_Id(request: Request, code: int,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    content_raw = await session.execute(select(Accessories).where(Accessories.product_code == code))
    data = content_raw.scalars().all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)

@app.get("/search_by_manufacturer/")
async def Search_By_Id(request: Request, manufacturer: str,page_num: int = 1, session: AsyncSession = Depends(get_async_session)):
    content_raw = await session.execute(select(Accessories).where(Accessories.manufacturer.like(f'{manufacturer}%')))
    data = content_raw.scalars().all()
    data_length = len(data)
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"page_num": page_num},)