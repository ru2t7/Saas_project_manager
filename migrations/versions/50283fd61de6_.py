"""empty message

Revision ID: 50283fd61de6
Revises: 05e9b731b095
Create Date: 2024-12-30 15:40:06.038711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50283fd61de6'
down_revision = '05e9b731b095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('importance')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('importance', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###