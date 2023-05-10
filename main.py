from fastapi import FastAPI,Request,Depends,Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from eshop import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@app.get("/")
async def home(request: Request,db: SessionLocal = Depends(get_db)):
    return templates.TemplateResponse('home.html',{'request':request})