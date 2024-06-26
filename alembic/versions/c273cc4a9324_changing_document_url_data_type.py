"""changing document url data type

Revision ID: c273cc4a9324
Revises: 0ba635463948
Create Date: 2024-05-01 16:40:26.933205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c273cc4a9324'
down_revision: Union[str, None] = '0ba635463948'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('document_url', sa.String(), nullable=False))
    op.drop_constraint('projects_category_id_fkey', 'projects', type_='foreignkey')
    op.create_foreign_key(None, 'projects', 'category', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_column('projects', 'document_urls')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('document_urls', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.create_foreign_key('projects_category_id_fkey', 'projects', 'users', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_column('projects', 'document_url')
    # ### end Alembic commands ###
