from enum import Enum
from model.entity.base import Base
from model.tools.validator.validator import Validator
from sqlalchemy import Column, Integer, String, Enum


class Gender(Enum):
    Male = "male"
    Female = "female"


class Role(Enum):
    Admin = "admin"
    Student = "student"
    Professor = "professor"


class User(Base):
    __tablename__ = 'user_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    national_code = Column(Integer, unique=True, nullable=False)
    birthday = Column(String(20), nullable=False)
    adress = Column(String(100), nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    term = Column(Integer)
    courses = Column(String(20))
    role = Column(String(20), nullable=False)

    def __init__(self, name, family, gender, national_code, birthday, adress, phone_number, username, password,
                 term, courses, role):
        self.user_id = None
        self.name = name
        self.family = family
        self.gender = gender
        self.national_code = national_code
        self.birthday = birthday
        self.adress = adress
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.term = term
        self.courses = courses
        self.role = role

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    def get_family(self):
        return self._family

    def set_family(self, family):
        self._family = Validator.name_validator(family, "Invalid Family")

    def get_national_code(self):
        return self._national_code

    def set_national_code(self, national_code):
        self._national_code = Validator.national_code_validator(national_code, "Invalid National Code")

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = Validator.username_validator(username, "Invalid Username")

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = Validator.phone_number_validator(phone_number, "Invalid Phone Number")

    def get_term(self):
        return self._term

    def set_terms(self, term):
        self._term = Validator.term_validator(term, "Invalid Term")
