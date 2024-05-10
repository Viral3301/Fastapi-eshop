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


class Products(Base):
    __tablename__ = 'Products'

    id: Mapped[intpk]
    title: Mapped[str_60]
    category: Mapped[int] = mapped_column(ForeignKey('Category.id', ondelete="CASCADE"))
    product_code: Mapped[int] = mapped_column(default=111111)
    image: Mapped[str]
    price: Mapped[int]
    sale: Mapped[bool] = mapped_column(default=False)


class ProductAttributes(Base):
    __tablename__ = 'ProductAttributes'

    id: Mapped[intpk]
    title: Mapped[str_60]

class AttributeValue(Base):
    __tablename__ = 'AttributeValue'

    id: Mapped[intpk]
    product_id: Mapped[int] = mapped_column(ForeignKey('Products.id', ondelete="CASCADE"))
    attribute_id: Mapped[int] = mapped_column(ForeignKey('ProductAttributes.id', ondelete="CASCADE"))
    value: Mapped[str]


class Orders(Base):
    __tablename__ = 'Orders'

    id: Mapped[intpk]
    user_id: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey("Products.id" , ondelete="CASCADE"))
