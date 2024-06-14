from sqlalchemy import Column, Integer, ForeignKey, Table, Enum
from model.entity.base import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

enrollment_table = Table('enrollment_tbl', Base.metadata,
                         Column('term_id', Integer, ForeignKey('term_tbl.id')),
                         Column('course_id', Integer, ForeignKey('course_tbl.id')),
                         extend_existing=True
                         )

class CourseStatus(PyEnum):
    IN_PROGRESS = 1
    PASSED = 2
    FAILED = 3

class Enrollment(Base):
    __tablename__ = 'enrollment_tbl'
    __table_args__ = {'extend_existing': True}
    term_id = Column(Integer, ForeignKey('term_tbl.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course_tbl.id'), primary_key=True)
    term = relationship("Term", back_populates="courses")
    course = relationship("Course", back_populates="terms")
    status = Column(Enum(CourseStatus), nullable=False)
    score = Column(Integer, nullable=True)