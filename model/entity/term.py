from sqlalchemy import Column, Integer, ForeignKey, Table, DateTime, Enum
from sqlalchemy.orm import relationship
from model.entity.base import Base
from enum import Enum as PyEnum


# Association table for the many-to-many relationship between Term and Course
term_course_table = Table('term_course_tbl', Base.metadata,
                          Column('term_id', Integer, ForeignKey('term_tbl.id')),
                          Column('course_id', Integer, ForeignKey('course_tbl.id'))
                          )


class Term(Base):
    __tablename__ = 'term_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # student_id = Column(Integer, ForeignKey('user_tbl.id'))
    # term_number = Column(Integer, nullable=False)
    # average_score = Column(Integer, nullable=True)
    # courses = relationship("Course",
    #                        secondary=term_course_table,
    #                        back_populates="terms")
    # status = Column(Enum(TermStatus), nullable=False, default=TermStatus.IN_PROGRESS)
    # student = relationship("Student", back_populates="terms")
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)
    ended = end_date is not None

    def __init__(self, start_date, end_date=None):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date