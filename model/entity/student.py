from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from model.entity.user import User
from model.entity.term import Term

class Student(User):
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }
    terms = relationship("Term", back_populates="student")

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password, terms):
        super().__init__(name, family, gender, national_code, birthday, address, phone_number, username, password, "student")
        self.terms = terms