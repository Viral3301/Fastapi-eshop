from eshop.models import *
from database import User
from sqladmin import Admin, ModelView

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

class ProductsAdmin(ModelView, model=Products):
    column_list = [Products.id,Products.image,Products.title,Products.price,Products.product_code,Products.sale]

class AttributesAdmin(ModelView, model=ProductAttributes):
    column_list = [ProductAttributes.id,ProductAttributes.title]

class ValuesAdmin(ModelView, model=AttributeValue):
    column_list = [AttributeValue.id,AttributeValue.attribute_id,AttributeValue.product_id,AttributeValue.value]

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id,Category.name]