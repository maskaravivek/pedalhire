"""empty message

Revision ID: 1344169972ef
Revises: 
Create Date: 2020-04-30 12:53:46.513256

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1344169972ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'login', ['id'])
    op.alter_column('orders', 'days',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=5)),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'days',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=5)),
               nullable=False)
    op.drop_constraint(None, 'login', type_='unique')
    # ### end Alembic commands ###
