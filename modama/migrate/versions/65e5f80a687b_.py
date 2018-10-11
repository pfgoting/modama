"""empty message

Revision ID: 65e5f80a687b
Revises: 6c118747dd6a
Create Date: 2018-10-11 22:57:47.121015

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '65e5f80a687b'
down_revision = '6c118747dd6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('base_observation', 'reporter_contact')
    op.drop_column('base_observation', 'reporter')
    op.drop_index('idx_pawikan_general_location', table_name='pawikan_general')
    op.drop_index('idx_pawikan_general_version_location', table_name='pawikan_general_version')
    op.drop_index('idx_pawikan_nest_with_egg_location', table_name='pawikan_nest_with_egg')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_pawikan_nest_with_egg_location', 'pawikan_nest_with_egg', ['location'], unique=False)
    op.create_index('idx_pawikan_general_version_location', 'pawikan_general_version', ['location'], unique=False)
    op.create_index('idx_pawikan_general_location', 'pawikan_general', ['location'], unique=False)
    op.add_column('base_observation', sa.Column('reporter', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('base_observation', sa.Column('reporter_contact', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
