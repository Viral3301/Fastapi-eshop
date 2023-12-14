import datetime
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime,Integer,String,Boolean,ForeignKey,Float, func,Date
from sqlalchemy.orm import mapped_column,Mapped,relationship



class Base(DeclarativeBase):
    pass

intpk = Annotated[int, mapped_column(primary_key=True)]
str_60 = Annotated[str, 30]


class Category(Base):
    __tablename__ = 'Category'

    id: Mapped[intpk]
    name: Mapped[str_60]


class Vehicles(Base):
    __tablename__ = 'Vehicles'

    id: Mapped[intpk]
    title: Mapped[str_60]
    product_code: Mapped[int] = mapped_column(default=111111)
    image: Mapped[str]
    price: Mapped[int]
    manufacturer: Mapped[str_60]
    seats: Mapped[int]
    engine: Mapped[int]
    engine_type: Mapped[str_60]
    year: Mapped[int]
    amount_in_stock: Mapped[int]
    sale: Mapped[bool] = mapped_column(default=False)
    category: Mapped[int] = mapped_column(ForeignKey('Category.id', ondelete="CASCADE"))
    rating: Mapped[float] = mapped_column(nullable=True)

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[intpk]   
    email: Mapped[str]
    username: Mapped[str_60]
    registered_at: Mapped[datetime.date] = mapped_column(server_default=func.now())
    hashed_password: Mapped[str]
    image: Mapped[str] = mapped_column(default="default.pfp")
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

class Accessories(Base):
    __tablename__ = 'Accessories'

    id: Mapped[intpk]
    title: Mapped[str_60]
    product_code: Mapped[int] = mapped_column(default=111111)
    image: Mapped[str]
    price: Mapped[int]
    manufacturer: Mapped[str_60]
    amount_in_stock: Mapped[int]
    sale: Mapped[bool] = mapped_column(default=False)
    category: Mapped[int] = mapped_column(ForeignKey('Category.id', ondelete="CASCADE"))
    material: Mapped[str]
    guarantee: Mapped[int]
    color: Mapped[str]
    company: Mapped[str]
    rating: Mapped[float]


class Cart(Base):
    __tablename__ = 'Cart'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id" , ondelete="CASCADE"))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("Vehicles.id" , ondelete="CASCADE"))
    accessory_id: Mapped[int] = mapped_column(ForeignKey("Accessories.id" , ondelete="CASCADE"))

class Orders(Base):
    __tablename__ = 'Orders'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id" , ondelete="CASCADE"))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("Vehicles.id" , ondelete="CASCADE"))
    accessory_id: Mapped[int] = mapped_column(ForeignKey("Accessories.id" , ondelete="CASCADE"))