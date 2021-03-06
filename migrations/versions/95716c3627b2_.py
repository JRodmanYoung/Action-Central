"""empty message

Revision ID: 95716c3627b2
Revises: 
Create Date: 2020-01-11 19:13:53.942706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95716c3627b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_ID', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('user_email', sa.String(length=256), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('assignment_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_ID'], ['user.user_ID'], ),
    sa.PrimaryKeyConstraint('user_ID'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
