"""empty message

Revision ID: 0ee330ab6f91
Revises: 
Create Date: 2018-09-19 12:12:49.103507

"""
from alembic import op
import sqlalchemy as sa
from flask_appbuilder.models.mixins import ImageColumn
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = '0ee330ab6f91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pawikan_encounter_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pawikan_encounter_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('species_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('encounter_type_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('ccl', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('sex_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('location', Geometry(geometry_type='POINT', srid=4326), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(op.f('ix_pawikan_encounter_version_end_transaction_id'), 'pawikan_encounter_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_pawikan_encounter_version_operation_type'), 'pawikan_encounter_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_pawikan_encounter_version_transaction_id'), 'pawikan_encounter_version', ['transaction_id'], unique=False)
    op.create_table('pawikan_species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genus', sa.String(length=255), nullable=False),
    sa.Column('species', sa.String(length=255), nullable=False),
    sa.Column('common_name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('picture', ImageColumn(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('base_observation',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.Column('observation_datetime', sa.DateTime(timezone=True), nullable=False),
    sa.Column('observer_id', sa.Integer(), nullable=False),
    sa.Column('dataset', sa.String(length=50), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=False),
    sa.Column('changed_by_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['observer_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_encounter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.Column('encounter_type_id', sa.Integer(), nullable=False),
    sa.Column('ccl', sa.Integer(), nullable=True),
    sa.Column('sex_id', sa.Integer(), nullable=True),
    sa.Column('location', Geometry(geometry_type='POINT', srid=4326), nullable=True),
    sa.ForeignKeyConstraint(['encounter_type_id'], ['pawikan_encounter_type.id'], ),
    sa.ForeignKeyConstraint(['id'], ['base_observation.id'], ),
    sa.ForeignKeyConstraint(['sex_id'], ['sex.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['pawikan_species.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_encounter_picture',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture', ImageColumn(), nullable=True),
    sa.Column('encounter_id', sa.Integer(), nullable=False),
    sa.Column('created_by_fk', sa.Integer(), nullable=False),
    sa.Column('changed_by_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['encounter_id'], ['pawikan_encounter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pawikan_encounter_picture')
    op.drop_table('pawikan_encounter')
    op.drop_table('base_observation')
    op.drop_table('transaction')
    op.drop_table('sex')
    op.drop_table('pawikan_species')
    op.drop_index(op.f('ix_pawikan_encounter_version_transaction_id'), table_name='pawikan_encounter_version')
    op.drop_index(op.f('ix_pawikan_encounter_version_operation_type'), table_name='pawikan_encounter_version')
    op.drop_index(op.f('ix_pawikan_encounter_version_end_transaction_id'), table_name='pawikan_encounter_version')
    op.drop_table('pawikan_encounter_version')
    op.drop_table('pawikan_encounter_type')
    # ### end Alembic commands ###