"""Changes in shop.id column

Revision ID: 8d98dd4681c4
Revises: bd233b96ea0d
Create Date: 2021-01-27 18:39:39.015655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d98dd4681c4'
down_revision = 'bd233b96ea0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('SYS_CONSTRAINT_fffe0e11-ce94-41e6-96f9-1d1d7bfa428b', 'receipt', type_='foreignkey')
    op.drop_constraint('SYS_CONSTRAINT_a9f2916f-4fbd-46e4-8e0b-8fb8eef847fd', 'receipt', type_='foreignkey')
    op.create_foreign_key(None, 'receipt', 'shop', ['shop_id'], ['id'])
    op.create_foreign_key(None, 'receipt', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.create_foreign_key('SYS_CONSTRAINT_a9f2916f-4fbd-46e4-8e0b-8fb8eef847fd', 'receipt', 'shop', ['shop_id'], ['id'], referent_schema='develop')
    op.create_foreign_key('SYS_CONSTRAINT_fffe0e11-ce94-41e6-96f9-1d1d7bfa428b', 'receipt', 'product', ['product_id'], ['id'], referent_schema='develop')
    # ### end Alembic commands ###
