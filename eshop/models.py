from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float,Date
from database import Base
from datetime import datetime


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)


class Vehicles(Base):
    __tablename__ = 'Vehicles'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    product_code = Column(Integer,default=11111)
    image = Column(String)
    price = Column(Integer,default=100000)
    manufacturer = Column(String(100))
    seats = Column(Integer)
    engine = Column(Integer)
    engine_type = Column(String)
    year = Column(Integer)
    amount_in_stock = Column(Integer)
    sale = Column(Boolean,default=False)
    category = Column(ForeignKey('Category.id'))
    rating = Column(Float)



class Accessories(Base):
    __tablename__ = 'Accessories'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    product_code = Column(Integer,default=111111)
    image = Column(String)
    price = Column(Integer,default=100000)
    manufacturer = Column(String(100))
    amount_in_stock = Column(Integer)
    sale = Column(Boolean,default=False)
    category = Column(ForeignKey('Category.id'))
    rating = Column(Float)


class Users(Base):
    __tablename__ = 'Users'

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at",Date, default=datetime.now())
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified = Column("is_verified", Boolean, default=False, nullable=False)