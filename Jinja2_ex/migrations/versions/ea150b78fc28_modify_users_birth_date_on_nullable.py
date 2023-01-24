"""Modify users.birth_date on Nullable

Revision ID: ea150b78fc28
Revises: f99b4c3b6438
Create Date: 2023-01-24 03:54:33.974378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea150b78fc28'
down_revision = 'f99b4c3b6438'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('birth_date',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('birth_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###