from enum import Enum
from controller.exceptions.my_exceptions import DuplicateUsernameError
from model.entity.admin import Admin
from model.entity.professor import Professor
from model.entity.student import Student
from model.entity.user import User
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess


class UserType(Enum):
    Student = 1,
    Professor = 2,
    Admin = 3


class UserController:
    @classmethod
    @exception_handling
    def save(cls, name, family, gender, national_code, birthday, address, phone_number, username, password, type):
        session = DataAccess().get_session()
        if not session.query(User).filter(User.username == username).first():
            if type == UserType.Student:
                user = Student(name, family, gender, national_code, birthday, address, phone_number, username, password)
                session.add(user)
            elif type == UserType.Professor:
                user = Professor(name, family, gender, national_code, birthday, address, phone_number, username, password)
                session.add(user)
            elif type == UserType.Admin:
                user = Admin(name, family, gender, national_code, birthday, address, phone_number, username, password)
                session.add(user)
            session.commit()
            return True, f"User saved successfully {user}"
        else:
            raise DuplicateUsernameError

    @classmethod
    @exception_handling
    def edit(cls, user_id, name, family, gender, national_code, address, phone_number, username, password):
        session = DataAccess().get_session()
        user = session.query(User).get(user_id)
        if user:
            user.name = name
            user.family = family
            user.gender = gender
            user.national_code = national_code
            user.address = address
            user.phone_number = phone_number
            user.username = username
            user.password = password
            session.commit()
            return True, f"User edited successfully {user}"
        else:
            return False, "User not found"

    @classmethod
    @exception_handling
    def remove(cls, user_id):
        session = DataAccess().get_session()
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True, f"User removed successfully {user}"
        else:
            return False, "User not found"

    @classmethod
    @exception_handling
    def find_all(cls):
        session = DataAccess().get_session()
        return True, session.query(User).all()

    @classmethod
    @exception_handling
    def find_by_user_id(cls, user_id):
        session = DataAccess().get_session()
        user = session.query(User).get(user_id)
        if user:
            return True, user
        else:
            return False, "User not found"

    @classmethod
    @exception_handling
    def login(cls, username, password):
        session = DataAccess().get_session()
        user = session.query(User).filter(User.username == username, User.password == password).first()
        
        if not user:
            return False, None
    
        for Model in [Student, Professor, Admin]:
            person = session.query(Model).filter(Model.id == user.id).first()
            if person:
                return True, person
    
        return False, None