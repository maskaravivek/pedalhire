"""empty message

Revision ID: 454b8c28b684
Revises: 
Create Date: 2020-04-24 11:18:52.997428

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '454b8c28b684'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('login', sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False))
    op.add_column('login', sa.Column('role_type', sa.Enum('USER', 'MERCHANT', name='role'), nullable=True))
    op.create_unique_constraint(None, 'login', ['id'])
    op.drop_constraint('login_login_id_fkey1', 'login', type_='foreignkey')
    op.drop_constraint('login_login_id_fkey', 'login', type_='foreignkey')
    op.drop_column('login', 'login_id')
    op.add_column('merchants', sa.Column('phone_extension', sa.String(length=10), nullable=False))
    op.add_column('merchants', sa.Column('phone_number', sa.String(length=20), nullable=False))
    op.add_column('merchants', sa.Column('state', sa.String(length=200), nullable=False))
    op.add_column('merchants', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('merchants', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_constraint('merchants_first_name_key', 'merchants', type_='unique')
    op.create_unique_constraint(None, 'merchants', ['login_id'])
    op.create_foreign_key(None, 'merchants', 'login', ['login_id'], ['id'])
    op.drop_column('merchants', 'modified_at')
    op.add_column('orders', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('orders', 'modified_at')
    op.add_column('products', sa.Column('updated_at', sa.Date(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('products', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('products', 'modified_at')
    op.add_column('users', sa.Column('latitude', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('longitude', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('phone_extension', sa.String(length=10), nullable=False))
    op.add_column('users', sa.Column('phone_number', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('state', sa.String(length=200), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_constraint('users_first_name_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['login_id'])
    op.create_foreign_key(None, 'users', 'login', ['login_id'], ['id'])
    op.drop_column('users', 'modified_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_first_name_key', 'users', ['first_name'])
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'state')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'phone_extension')
    op.drop_column('users', 'longitude')
    op.drop_column('users', 'latitude')
    op.add_column('products', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.alter_column('products', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('products', 'updated_at')
    op.add_column('orders', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('orders', 'updated_at')
    op.add_column('merchants', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'merchants', type_='foreignkey')
    op.drop_constraint(None, 'merchants', type_='unique')
    op.create_unique_constraint('merchants_first_name_key', 'merchants', ['first_name'])
    op.alter_column('merchants', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('merchants', 'updated_at')
    op.drop_column('merchants', 'state')
    op.drop_column('merchants', 'phone_number')
    op.drop_column('merchants', 'phone_extension')
    op.add_column('login', sa.Column('login_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.create_foreign_key('login_login_id_fkey', 'login', 'merchants', ['login_id'], ['id'])
    op.create_foreign_key('login_login_id_fkey1', 'login', 'users', ['login_id'], ['id'])
    op.drop_constraint(None, 'login', type_='unique')
    op.drop_column('login', 'role_type')
    op.drop_column('login', 'id')
    # ### end Alembic commands ###