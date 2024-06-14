from enum import Enum
from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Enum as SAEnum

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
    gender = Column(SAEnum(Gender))
    national_code = Column(String(20), unique=True, nullable=False)
    birthday = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(30), nullable=False)

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password):
        super().__init__()
        self.id = None
        self.name = name
        self.family = family
        self.gender = gender
        self.national_code = national_code
        self.birthday = birthday
        self.address = address
        self.phone_number = phone_number
        self.username = username
        self.password = password