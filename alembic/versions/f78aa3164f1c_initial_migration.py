"""Initial Migration

Revision ID: f78aa3164f1c
Revises: 
Create Date: 2024-06-14 08:22:05.780810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f78aa3164f1c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('term_tbl',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tbl',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('family', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.Enum('Male', 'Female', name='gender'), nullable=True),
    sa.Column('national_code', sa.String(length=20), nullable=False),
    sa.Column('birthday', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('national_code'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('username')
    )
    op.create_table('admin_tbl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_tbl.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course_tbl',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('unit_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['user_tbl.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor_tbl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_tbl.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_tbl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_tbl.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prerequisite_tbl',
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('prerequisite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course_tbl.id'], ),
    sa.ForeignKeyConstraint(['prerequisite_id'], ['course_tbl.id'], )
    )
    op.create_table('professor_term_tbl',
    sa.Column('professor_id', sa.Integer(), nullable=True),
    sa.Column('term_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('average_score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professor_tbl.id'], ),
    sa.ForeignKeyConstraint(['term_id'], ['term_tbl.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('professor_id', 'term_id', name='uix_student_term')
    )
    op.create_table('student_term_tbl',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('term_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Enum('IN_PROGRESS', 'PASSED', 'FAILED', name='termstatus'), nullable=False),
    sa.Column('average_score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student_tbl.id'], ),
    sa.ForeignKeyConstraint(['term_id'], ['term_tbl.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id', 'term_id', name='uix_student_term')
    )
    op.create_table('enrollment_tbl',
    sa.Column('student_term_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('IN_PROGRESS', 'PASSED', 'FAILED', name='coursestatus'), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course_tbl.id'], ),
    sa.ForeignKeyConstraint(['student_term_id'], ['student_term_tbl.id'], ),
    sa.PrimaryKeyConstraint('student_term_id', 'course_id')
    )
    op.create_table('teaching_tbl',
    sa.Column('professor_term_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course_tbl.id'], ),
    sa.ForeignKeyConstraint(['professor_term_id'], ['professor_term_tbl.id'], ),
    sa.PrimaryKeyConstraint('professor_term_id', 'course_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teaching_tbl')
    op.drop_table('enrollment_tbl')
    op.drop_table('student_term_tbl')
    op.drop_table('professor_term_tbl')
    op.drop_table('prerequisite_tbl')
    op.drop_table('student_tbl')
    op.drop_table('professor_tbl')
    op.drop_table('course_tbl')
    op.drop_table('admin_tbl')
    op.drop_table('user_tbl')
    op.drop_table('term_tbl')
    # ### end Alembic commands ###