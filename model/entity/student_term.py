from sqlalchemy import Column, Integer, ForeignKey, Table, Enum, UniqueConstraint
from model.entity.base import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

student_term_table = Table('student_term_tbl', Base.metadata,
                         Column('student_id', Integer, ForeignKey('student_tbl.id')),
                         Column('term_id', Integer, ForeignKey('term_tbl.id')),
                         extend_existing=True
                         )

class TermStatus(PyEnum):
    IN_PROGRESS = 1
    PASSED = 2
    FAILED = 3

class StudentTerm(Base):
    __tablename__ = 'student_term_tbl'
    __table_args__ = (
        UniqueConstraint('student_id', 'term_id', name='uix_student_term'),
        {'extend_existing': True}
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student_tbl.id'))
    term_id = Column(Integer, ForeignKey('term_tbl.id'))
    # student = relationship("Student", back_populates="terms")
    # term = relationship("Term", back_populates="courses")
    status = Column(Enum(TermStatus), nullable=False)
    average_score = Column(Integer, nullable=True)