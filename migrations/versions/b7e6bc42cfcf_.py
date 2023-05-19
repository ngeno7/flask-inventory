"""empty message

Revision ID: b7e6bc42cfcf
Revises: 5f3f09e21618
Create Date: 2023-05-19 08:29:37.627889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7e6bc42cfcf'
down_revision = '5f3f09e21618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_takes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_takes', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###
