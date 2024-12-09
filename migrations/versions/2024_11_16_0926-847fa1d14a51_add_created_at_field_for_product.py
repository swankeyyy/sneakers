"""add created_at field for Product

Revision ID: 847fa1d14a51
Revises: e572f5b99a78
Create Date: 2024-11-16 09:26:18.835971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '847fa1d14a51'
down_revision: Union[str, None] = 'e572f5b99a78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'created_at')
    # ### end Alembic commands ###
