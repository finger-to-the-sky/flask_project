"""empty message

Revision ID: 17e0a2964d4d
Revises: 0d969c99d48f
Create Date: 2023-03-26 13:36:21.322673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e0a2964d4d'
down_revision = '0d969c99d48f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authors')
    # ### end Alembic commands ###
