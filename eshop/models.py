from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float,Date
from sqlalchemy.orm import mapped_column,Mapped,relationship
from typing import List
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
    material = Column(String)
    guarantee = Column(Integer)
    color = Column(String)
    company = Column(String)
    rating = Column(Float)


class Users(Base):
    __tablename__ = 'Users'

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at",Date, default=datetime.now())
    cart = mapped_column(Integer,ForeignKey("Cart.id"))
    orders : Mapped[List["Orders"]] = relationship()
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified = Column("is_verified", Boolean, default=False, nullable=False)


class Cart(Base):
    __tablename__ = 'Cart'

    id = Column("id", Integer, primary_key=True)
    user_id = mapped_column(Integer,ForeignKey("Users.id"))
    vehicle_id = mapped_column(Integer,ForeignKey("Vehicles.id"))
    accessory_id = mapped_column(Integer,ForeignKey("Accessories.id"))

class Orders(Base):
    __tablename__ = 'Orders'

    id = Column("id", Integer, primary_key=True)
    user_id = mapped_column(Integer,ForeignKey("Users.id"))
    vehicle_id = mapped_column(Integer,ForeignKey("Vehicles.id"))
    accessory_id = mapped_column(Integer,ForeignKey("Accessories.id"))