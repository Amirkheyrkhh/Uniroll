from sqlalchemy import Column, Integer, ForeignKey, Table, Enum
from model.entity.base import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

student_term_table = Table('student_term_tbl', Base.metadata,
                         Column('user_id', Integer, ForeignKey('user_tbl.id')),
                         Column('term_id', Integer, ForeignKey('term_tbl.id')),
                         extend_existing=True
                         )

class CourseStatus(PyEnum):
    IN_PROGRESS = 1
    PASSED = 2
    FAILED = 3

class StudentTerm(Base):
    __tablename__ = 'enrollment_tbl'
    __table_args__ = {'extend_existing': True}
    student_id = Column(Integer, ForeignKey('user_tbl.id'), primary_key=True)
    term_id = Column(Integer, ForeignKey('term_tbl.id'), primary_key=True)
    student = relationship("Student", back_populates="terms")
    term = relationship("Term", back_populates="courses")
    status = Column(Enum(CourseStatus), nullable=False)
    score = Column(Integer, nullable=True)