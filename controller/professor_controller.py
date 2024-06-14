from sqlalchemy.orm.exc import NoResultFound
from controller.exceptions.my_exceptions import DuplicateUsernameError, ProfessorNotFoundError
from model.entity.professor import Professor
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess

class ProfessorController:
    @classmethod
    @exception_handling
    def save(cls, name, family, gender, national_code, birthday, address, phone_number, username, password):
        session = DataAccess().get_session()
        if not session.query(Professor).filter(Professor.username == username).first():
            professor = Professor(name, family, gender, national_code, birthday, address, phone_number, username, password)
            session.add(professor)
            session.commit()
            return True, f"Professor saved successfully {professor}"
        else:
            raise DuplicateUsernameError

    @classmethod
    @exception_handling
    def edit(cls, professor_id, name, family, gender, national_code, address, phone_number, username, password):
        session = DataAccess().get_session()
        professor = session.query(Professor).get(professor_id)
        if professor:
            professor.name = name
            professor.family = family
            professor.gender = gender
            professor.national_code = national_code
            professor.address = address
            professor.phone_number = phone_number
            professor.username = username
            professor.password = password
            session.commit()
            return True, f"Professor edited successfully {professor}"
        else:
            return False, "Professor not found"

    @classmethod
    @exception_handling
    def remove(cls, professor_id):
        session = DataAccess().get_session()
        professor = session.query(Professor).get(professor_id)
        if professor:
            session.delete(professor)
            session.commit()
            return True, f"Professor removed successfully {professor}"
        else:
            return False, "Professor not found"

    @classmethod
    @exception_handling
    def find_all(cls):
        session = DataAccess().get_session()
        return True, session.query(Professor).all()

    @classmethod
    @exception_handling
    def find_by_professor_id(cls, professor_id):
        session = DataAccess().get_session()
        professor = session.query(Professor).get(professor_id)
        if professor:
            return True, professor
        else:
            return False, "Professor not found"