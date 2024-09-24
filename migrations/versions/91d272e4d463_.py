"""empty message

Revision ID: 91d272e4d463
Revises: e1ff09d4d8aa
Create Date: 2024-09-24 00:17:30.560023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91d272e4d463'
down_revision = 'e1ff09d4d8aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('brewery_review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['owner_id'], ['id'])
        batch_op.drop_column('image_url')

    with op.batch_alter_table('user_image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'brewery_review', ['review_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_image', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('review_id')

    with op.batch_alter_table('brewery_review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('owner_id')

    # ### end Alembic commands ###
