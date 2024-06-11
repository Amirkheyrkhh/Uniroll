from sqlalchemy import *
from sqlalchemy.orm import relationship

from model.entity.enrollment import enrollment_table
from model.entity.user import User


class Student(User):
    __mapper_args__ = {
        'polymorphic_identity':'student',
    }
    term = Column(Integer, nullable=True)
    average_score = Column(Integer, nullable=True)