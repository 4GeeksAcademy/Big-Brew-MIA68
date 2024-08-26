"""empty message

Revision ID: 75787a03be0f
Revises: 65b5d26f989a
Create Date: 2024-08-24 23:38:41.842100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75787a03be0f'
down_revision = '65b5d26f989a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
