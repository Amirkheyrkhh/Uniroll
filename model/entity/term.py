from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from model.entity.base import Base

# Association table for the many-to-many relationship between Term and Course
term_course_table = Table('term_course_tbl', Base.metadata,
                          Column('term_id', Integer, ForeignKey('term_tbl.id')),
                          Column('course_id', Integer, ForeignKey('course_tbl.id'))
                          )

class Term(Base):
    __tablename__ = 'term_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('user_tbl.id'))
    term_number = Column(Integer, nullable=False)
    average_score = Column(Integer, nullable=True)
    courses = relationship("Course",
                           secondary=term_course_table,
                           back_populates="terms")
    student = relationship("Student", back_populates="terms")

    def __init__(self, student_id, term_number, average_score, courses):
        super().__init__()
        self.student_id = student_id
        self.term_number = term_number
        self.average_score = average_score
        self.courses = courses