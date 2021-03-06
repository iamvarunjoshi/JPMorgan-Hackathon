"""empty message

Revision ID: 537d2854c096
Revises: 1ab214edfde6
Create Date: 2015-11-08 02:05:45.969208

"""

# revision identifiers, used by Alembic.
revision = '537d2854c096'
down_revision = '1ab214edfde6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.Column('kind', sa.String(length=80), nullable=True),
    sa.Column('image', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('issues')
    ### end Alembic commands ###
