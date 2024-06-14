from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.user import User
from model.entity.term import Term

class Student(User):
    __tablename__ = 'student_tbl'
    id = Column(Integer, ForeignKey('user_tbl.id'), primary_key=True)

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password):
        super().__init__(name, family, gender, national_code, birthday, address, phone_number, username, password)