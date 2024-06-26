"""Remove average_score from professor_term table

Revision ID: 929e37b87a19
Revises: f78aa3164f1c
Create Date: 2024-06-14 09:46:32.947357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '929e37b87a19'
down_revision: Union[str, None] = 'f78aa3164f1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professor_term_tbl', 'average_score')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor_term_tbl', sa.Column('average_score', mysql.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
