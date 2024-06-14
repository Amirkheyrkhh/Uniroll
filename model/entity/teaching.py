from sqlalchemy import Column, Integer, ForeignKey, Table, Enum
from model.entity.base import Base
from enum import Enum as PyEnum

teaching_table = Table('teaching_tbl', Base.metadata,
                         Column('professor_term_id', Integer, ForeignKey('professor_term_tbl.id')),
                         Column('course_id', Integer, ForeignKey('course_tbl.id')),
                         extend_existing=True
                         )


class Teaching(Base):
    __tablename__ = 'teaching_tbl'
    __table_args__ = {'extend_existing': True}
    professor_term_id = Column(Integer, ForeignKey('professor_term_tbl.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course_tbl.id'), primary_key=True)