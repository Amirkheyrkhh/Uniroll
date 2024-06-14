from sqlalchemy import Column, Integer, ForeignKey, Table, Enum, UniqueConstraint
from model.entity.base import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

student_term_table = Table('professor_term_tbl', Base.metadata,
                         Column('professor_id', Integer, ForeignKey('professor_tbl.id')),
                         Column('term_id', Integer, ForeignKey('term_tbl.id')),
                         extend_existing=True
                         )

class ProfessorTerm(Base):
    __tablename__ = 'professor_term_tbl'
    __table_args__ = (
        UniqueConstraint('professor_id', 'term_id', name='uix_student_term'),
        {'extend_existing': True}
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey('professor_tbl.id'))
    term_id = Column(Integer, ForeignKey('term_tbl.id'))
    professor = relationship("Professor", back_populates="terms")
    term = relationship("Term", back_populates="courses")
    average_score = Column(Integer, nullable=True)