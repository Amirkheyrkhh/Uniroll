from sqlalchemy import *
from sqlalchemy.orm import relationship
from model.entity.base import Base

enrollment_table = Table('enrollment_tbl', Base.metadata,
                         Column('user_id', Integer, ForeignKey('user_tbl.id')),
                         Column('course_id', Integer, ForeignKey('course_tbl.id')),
                         extend_existing=True
                         )


class Enrollment(Base):
    __tablename__ = 'enrollment_tbl'
    __table_args__ = {'extend_existing': True}
    student_id = Column(Integer, ForeignKey('user_tbl.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course_tbl.id'), primary_key=True)
