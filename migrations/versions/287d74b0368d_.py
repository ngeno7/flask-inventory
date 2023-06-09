"""empty message

Revision ID: 287d74b0368d
Revises: 3121b5b587ba
Create Date: 2023-05-12 11:29:09.536111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '287d74b0368d'
down_revision = '3121b5b587ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
