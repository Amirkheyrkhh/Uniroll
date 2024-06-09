from model.entity import *
from model.tools.validator.validator import Validator


class Course(Base):
    __tablename__ = 'course_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    prerequisites = Column(String(20))
    professor = Column(String(20), nullable=False)
    capacity = Column(Integer, nullable=False)


    def __init__(self, name, prerequisites, professor, capacity):
        self.course_id = None
        self.name = name
        self.prerequisites = prerequisites
        self.professor = professor
        self.capacity = capacity

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    def get_professor(self):
        return self._professor

    def set_professor(self, professor):
        self._professor = Validator.family_validator(professor, "Invalid Professor")

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = Validator.capacity_validator(capacity, "Invalid Capacity")