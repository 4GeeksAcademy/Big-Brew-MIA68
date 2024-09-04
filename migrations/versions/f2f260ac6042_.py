"""empty message

Revision ID: f2f260ac6042
Revises: 13019692b99d
Create Date: 2024-08-31 00:48:22.718607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f260ac6042'
down_revision = '13019692b99d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('beer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brewery_Id', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('beer', schema=None) as batch_op:
        batch_op.drop_column('brewery_Id')

    # ### end Alembic commands ###
