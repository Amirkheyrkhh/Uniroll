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

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password, term, average_score):
        super().__init__(name, family, gender,national_code, birthday, address, phone_number, username, password, "student")
        self.term = term
        self.average_score = average_score