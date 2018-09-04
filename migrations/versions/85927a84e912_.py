"""empty message

Revision ID: 85927a84e912
Revises: 
Create Date: 2018-09-04 17:52:10.724948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85927a84e912'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first', sa.String(length=80), nullable=True),
    sa.Column('last', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('posted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote')
    op.drop_table('author')
    # ### end Alembic commands ###
