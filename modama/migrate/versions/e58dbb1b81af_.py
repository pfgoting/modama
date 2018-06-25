"""empty message

Revision ID: e58dbb1b81af
Revises: 810275fb090c
Create Date: 2018-06-23 23:47:35.958393

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'e58dbb1b81af'
down_revision = '810275fb090c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('base_observation', 'observer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('pawikan_encounter', sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), nullable=True))
    op.alter_column('pawikan_encounter', 'encounter_type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pawikan_encounter', 'species_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pawikan_encounter', 'species_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pawikan_encounter', 'encounter_type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('pawikan_encounter', 'location')
    op.alter_column('base_observation', 'observer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###