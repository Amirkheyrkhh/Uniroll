import mysql.connector


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model.entity.base import Base
from model.entity.user import User
from model.entity.student import Student
from model.entity.admin import Admin
from model.entity.professor import Professor
from model.entity.course import Course
from model.entity.enrollment import Enrollment


class DataAccess:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:root123@localhost/university_db')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)