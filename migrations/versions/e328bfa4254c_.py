"""empty message

Revision ID: e328bfa4254c
Revises: 123ca14a3f09
Create Date: 2025-02-25 21:19:11.262081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e328bfa4254c'
down_revision = '123ca14a3f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_identification_number', sa.String(length=15), nullable=False))
        batch_op.add_column(sa.Column('accommodation', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('programing_language', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('resume', sa.String(length=30), nullable=False))
        batch_op.drop_column('publication')
        batch_op.drop_column('address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('publication', sa.VARCHAR(length=30), nullable=False))
        batch_op.drop_column('resume')
        batch_op.drop_column('programing_language')
        batch_op.drop_column('accommodation')
        batch_op.drop_column('student_identification_number')

    # ### end Alembic commands ###
