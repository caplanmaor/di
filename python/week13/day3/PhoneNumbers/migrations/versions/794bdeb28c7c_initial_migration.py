"""Initial migration.

Revision ID: 794bdeb28c7c
Revises: a222591931ae
Create Date: 2022-04-15 13:26:54.322123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '794bdeb28c7c'
down_revision = 'a222591931ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nationality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nationality', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nationality')
    )
    op.create_table('junction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('nationality_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['nationality_id'], ['nationality.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('junction')
    op.drop_table('nationality')
    # ### end Alembic commands ###
