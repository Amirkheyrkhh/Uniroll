from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.teaching import Teaching
from model.entity.user import User

class Professor(User):
    __tablename__ = 'professor_tbl'
    id = Column(Integer, ForeignKey('user_tbl.id'), primary_key=True)
    courses = relationship(
        "Course",
        secondary=Teaching.__table__,
        primaryjoin="Professor.id == Teaching.professor_term_id",
        secondaryjoin="Course.id == Teaching.course_id",
        backref="professors"
    )

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password):
        super().__init__(name, family, gender, national_code, birthday, address, phone_number, username, password)