"""Add field users.login

Revision ID: f99b4c3b6438
Revises: 08d71d9fde30
Create Date: 2023-01-24 03:06:26.516095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99b4c3b6438'
down_revision = '08d71d9fde30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('login', sa.String(length=32), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('login')

    # ### end Alembic commands ###