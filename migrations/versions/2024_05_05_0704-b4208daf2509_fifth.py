"""fifth

Revision ID: b4208daf2509
Revises: 05b859e0eb12
Create Date: 2024-05-05 07:04:54.033131

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'b4208daf2509'
down_revision = '05b859e0eb12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ProductAttributes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.Column('product_code', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('sale', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['category'], ['Category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('AttributeValue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('attribute_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_id'], ['ProductAttributes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['Products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Cart')
    op.drop_table('Accessories')
    op.drop_table('Users')
    op.drop_table('user')
    op.drop_table('Vehicles')
    op.add_column('Orders', sa.Column('product_id', sa.Integer(), nullable=False))
    op.alter_column('Orders', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'Orders', 'Products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_column('Orders', 'vehicle_id')
    op.drop_column('Orders', 'accessory_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('accessory_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Orders', sa.Column('vehicle_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.create_foreign_key('Orders_vehicle_id_fkey', 'Orders', 'Vehicles', ['vehicle_id'], ['id'])
    op.create_foreign_key('Orders_user_id_fkey', 'Orders', 'Users', ['user_id'], ['id'])
    op.create_foreign_key('Orders_accessory_id_fkey', 'Orders', 'Accessories', ['accessory_id'], ['id'])
    op.alter_column('Orders', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('Orders', 'product_id')
    op.create_table('Vehicles',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Vehicles_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('product_code', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('manufacturer', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('seats', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('engine', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('engine_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount_in_stock', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sale', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category'], ['Category.id'], name='Vehicles_category_fkey'),
    sa.PrimaryKeyConstraint('id', name='Vehicles_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('registered_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('registered_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('cart', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cart'], ['Cart.id'], name='Users_cart_fkey'),
    sa.PrimaryKeyConstraint('id', name='Users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Accessories',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Accessories_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('product_code', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('manufacturer', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('amount_in_stock', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sale', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('material', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('guarantee', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('color', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('company', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category'], ['Category.id'], name='Accessories_category_fkey'),
    sa.PrimaryKeyConstraint('id', name='Accessories_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Cart',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Cart_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vehicle_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('accessory_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['accessory_id'], ['Accessories.id'], name='Cart_accessory_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], name='Cart_user_id_fkey'),
    sa.ForeignKeyConstraint(['vehicle_id'], ['Vehicles.id'], name='Cart_vehicle_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Cart_pkey')
    )
    op.drop_table('AttributeValue')
    op.drop_table('Products')
    op.drop_table('ProductAttributes')
    # ### end Alembic commands ###