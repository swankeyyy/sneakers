"""add orders

Revision ID: 8e0812138c6e
Revises: cda7bcc2f8fa
Create Date: 2024-12-16 13:21:12.535289

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa

import fastapi_storages
from app.src.models.product import storage



from typing import Any






# revision identifiers, used by Alembic.
revision: str = '8e0812138c6e'
down_revision: Union[str, None] = 'cda7bcc2f8fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('order_user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['order_user_id'], ['user.id'], name=op.f('fk_orders_order_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    op.create_table('order_product_association',
    sa.Column('order_id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_product_association_order_id_orders')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_order_product_association_product_id_products')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_product_association')),
    sa.UniqueConstraint('order_id', 'product_id', name='idx_unique_order_product')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_product_association')
    op.drop_table('orders')
    # ### end Alembic commands ###
