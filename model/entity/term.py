from sqlalchemy import Column, Integer, ForeignKey, Table, DateTime, Enum
from sqlalchemy.orm import relationship
from model.entity.base import Base
from enum import Enum as PyEnum


# Association table for the many-to-many relationship between Term and Course
# term_course_table = Table('term_course_tbl', Base.metadata,
#                           Column('term_id', Integer, ForeignKey('term_tbl.id')),
#                           Column('course_id', Integer, ForeignKey('course_tbl.id'))
#                           )


class Term(Base):
    __tablename__ = 'term_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    def __init__(self, start_date, end_date=None):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.ended = self.end_date is not None
        self.educational_year = self.start_date.year
        self.educational_half_year = 1 if self.start_date.month < 7 else 2