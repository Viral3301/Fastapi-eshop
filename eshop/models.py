from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from database import Base



class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)


class Vehicles(Base):
    __tablename__ = 'Vehicles'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
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



class Accessories(Base):
    __tablename__ = 'Accessories'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    image = Column(String)
    price = Column(Integer,default=100000)
    manufacturer = Column(String(100))
    amount_in_stock = Column(Integer)
    sale = Column(Boolean,default=False)
    category = Column(ForeignKey('Category.id'))

