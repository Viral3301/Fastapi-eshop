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
async def CreateAcessory(request: Request,name: str,db: SessionLocal = Depends(get_db)):
    new_category = models.Category(name=name)
    db.add(new_category)
    db.commit()
    return {'response': "good"}