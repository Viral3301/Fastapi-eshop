from eshop.models import *
from database import User
from sqladmin import Admin, ModelView

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

class AccesoryAdmin(ModelView, model=Accessories):
    column_list = [Accessories.id, Accessories.title, Accessories.price,Accessories.category,Accessories.amount_in_stock,Accessories.image,Accessories.rating,Accessories.manufacturer,Accessories.product_code,Accessories.sale]

class VehicleAdmin(ModelView, model=Vehicles):
    column_list = [Vehicles.id,Vehicles.title,Vehicles.year,Vehicles.category,Vehicles.engine,Vehicles.engine_type,Vehicles.image,Vehicles.manufacturer,Vehicles.price,Vehicles.product_code,Vehicles.rating,Vehicles.sale,Vehicles.seats,Vehicles.amount_in_stock,]