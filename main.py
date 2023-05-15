from fastapi import FastAPI,Request,Depends,File,UploadFile
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from eshop import models
import shutil

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/content_img", StaticFiles(directory='content_img'),name='content_img')

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@app.get("/")
async def home(request: Request,db: SessionLocal = Depends(get_db)):
    backpacks = db.query(models.Accessories).filter(models.Accessories.category == 1)
    swimsuits = db.query(models.Accessories).filter(models.Accessories.category == 2)
    return templates.TemplateResponse('home.html',{'request':request,'backpacks': backpacks,'swimsuits':swimsuits})

@app.post("/create")
async def CreateAcessory(request: Request,title: str,price: int,manufacturer: str ,amount_in_stock: int,sale: bool,category:int,image: UploadFile = File(...),db: SessionLocal = Depends(get_db)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_accesory = models.Accessories(title=title,image=image.filename,price=price,manufacturer=manufacturer,amount_in_stock=amount_in_stock,sale=sale,category=category)
    db.add(new_accesory)
    db.commit()
    return {'response': "good"}

@app.post("/createcategory")
async def CreateCategory(request: Request,name: str,db: SessionLocal = Depends(get_db)):
    new_category = models.Category(name=name)
    db.add(new_category)
    db.commit()
    return {'response': "good"}

@app.post("/createvehicle")
async def CreateVehicle(request: Request,title: str,price: int,manufacturer: str ,seats:int,engine:int,engine_type: str,year:int,amount_in_stock: int,sale: bool,category:int,image: UploadFile = File(...),db: SessionLocal = Depends(get_db)):
    with open (f'content_img/{image.filename}',"wb") as buffer:
        shutil.copyfileobj(image.file,buffer)
    new_vehicle = models.Vehicles(title=title,image=image.filename,price=price,manufacturer=manufacturer,seats=seats,engine=engine,engine_type=engine_type,year=year,amount_in_stock=amount_in_stock,sale=sale,category=category)
    db.add(new_vehicle)
    db.commit()
    return {'response': "good"}

@app.get("/category/{category_id}/{page_num}/")
async def home(request: Request, category_id: int,page_num: int = 1,db: SessionLocal = Depends(get_db)):
    data = db.query(models.Vehicles).filter(models.Vehicles.category == category_id)
    data_length = data.count()
    if data_length % 12 == 0:
        pages_total = data_length // 12
    else:
        pages_total = data_length // 12 + 1 
    start = (page_num - 1) * 12
    end = start + 12
    return templates.TemplateResponse('catalog.html',{'request':request,'data': data[start:end],'pages_total':pages_total+1,"category_id":category_id,"page_num": page_num},)