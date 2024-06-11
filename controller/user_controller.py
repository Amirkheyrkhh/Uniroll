from sqlalchemy.orm.exc import NoResultFound

from controller.exceptions.my_exceptions import DuplicateUsernameError, ProfessorNotFoundError
from model.entity.user import User
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess


class UserController:
    @classmethod
    @exception_handling
    def save(cls, name, family, gender, national_code, birthday, address, phone_number, username, password, type):
        session = DataAccess().get_session()
        if not session.query(User).filter(User.username == username).first():
            user = User(name, family, gender, national_code, birthday, address, phone_number, username, password, type)
            session.add(user)
            session.commit()
            return True, f"User saved successfully {user}"
        else:
            raise DuplicateUsernameError

    @classmethod
    @exception_handling
    def edit(cls, user_id, name, family, gender, national_code, address, phone_number, username, password, type):
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
            user.type = type
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
    def find_by_family(cls, family):
        session = DataAccess().get_session()
        users = session.query(User).filter(User.family == family).all()
        return True, users

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        session = DataAccess().get_session()
        user = session.query(User).filter(User.username == username).first()
        if user:
            return True, user
        else:
            return False, "User not found"

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        session = DataAccess().get_session()
        user = session.query(User).filter(User.username == username, User.password == password).first()
        if user:
            return True, user
        else:
            return False, "User not found"


class ProfessorController:
    @classmethod
    @exception_handling
    def get_courses(cls, professor_id):
        session = DataAccess().get_session()
        professor = session.query(User).get(professor_id)
        if professor:
            return professor.courses
        raise ProfessorNotFoundError
