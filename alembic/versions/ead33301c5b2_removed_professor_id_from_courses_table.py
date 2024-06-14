"""Removed professor_id from courses table

Revision ID: ead33301c5b2
Revises: 929e37b87a19
Create Date: 2024-06-14 10:10:57.029072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ead33301c5b2'
down_revision: Union[str, None] = '929e37b87a19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('course_tbl_ibfk_1', 'course_tbl', type_='foreignkey')
    op.drop_column('course_tbl', 'professor_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course_tbl', sa.Column('professor_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('course_tbl_ibfk_1', 'course_tbl', 'user_tbl', ['professor_id'], ['id'])
    # ### end Alembic commands ###
