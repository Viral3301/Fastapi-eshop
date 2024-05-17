import datetime
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime,Integer,String,Boolean,ForeignKey,Float, func,Date
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import datetime



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


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column("id", Integer,autoincrement=True, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at",Date, default=datetime.now())
    hashed_password = Column("hashed_password", String, nullable=False)
    image = Column("image",String,default='default_pfp.png')
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified = Column("is_verified", Boolean, default=False, nullable=False)
