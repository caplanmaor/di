"""robots table

Revision ID: dcc25a71bb6b
Revises: 1fda0daca808
Create Date: 2022-04-07 18:57:28.856952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc25a71bb6b'
down_revision = '1fda0daca808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('street', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('zipcode', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
