"""empty message

Revision ID: 44a23660661d
Revises: 51800f89f283
Create Date: 2024-09-16 03:49:43.198787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a23660661d'
down_revision = '51800f89f283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_image', schema=None) as batch_op:
        batch_op.drop_constraint('unique_img_title_user', type_='unique')
        batch_op.create_unique_constraint('unique_profile_image_per_user', ['owner_id', 'is_profile_image'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_image', schema=None) as batch_op:
        batch_op.drop_constraint('unique_profile_image_per_user', type_='unique')
        batch_op.create_unique_constraint('unique_img_title_user', ['owner_id'])

    # ### end Alembic commands ###