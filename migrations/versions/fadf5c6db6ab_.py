"""empty message

Revision ID: fadf5c6db6ab
Revises: 224f81f0be75
Create Date: 2024-09-10 00:12:16.867057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fadf5c6db6ab'
down_revision = '224f81f0be75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brewery_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brewer_name', sa.String(), nullable=False),
    sa.Column('overall_rating', sa.Float(), nullable=False),
    sa.Column('review_text', sa.String(length=500), nullable=True),
    sa.Column('is_favorite_brewery', sa.Boolean(), nullable=True),
    sa.Column('visit_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beer_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brewery_review_id', sa.Integer(), nullable=False),
    sa.Column('beer_name', sa.String(length=100), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('notes', sa.String(length=500), nullable=True),
    sa.Column('is_favorite', sa.Boolean(), nullable=True),
    sa.Column('date_tried', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['brewery_review_id'], ['brewery_review.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('journey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('active_route_index', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('journey_reviews',
    sa.Column('journey_id', sa.Integer(), nullable=False),
    sa.Column('brewery_review_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brewery_review_id'], ['brewery_review.id'], ),
    sa.ForeignKeyConstraint(['journey_id'], ['journey.id'], ),
    sa.PrimaryKeyConstraint('journey_id', 'brewery_review_id')
    )
    op.create_table('route',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('journey_id', sa.Integer(), nullable=False),
    sa.Column('brewery_destination', sa.String(length=100), nullable=False),
    sa.Column('travel_time', sa.Float(), nullable=False),
    sa.Column('miles', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['journey_id'], ['journey.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('route')
    op.drop_table('journey_reviews')
    op.drop_table('journey')
    op.drop_table('beer_review')
    op.drop_table('brewery_review')
    # ### end Alembic commands ###