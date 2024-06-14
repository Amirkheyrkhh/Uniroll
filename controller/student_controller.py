from sqlalchemy.orm.exc import NoResultFound
from controller.exceptions.my_exceptions import DuplicateUsernameError, StudentNotFoundError
from model.entity.student import Student
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess

class StudentController:
    @classmethod
    @exception_handling
    def save(cls, name, family, gender, national_code, birthday, address, phone_number, username, password):
        session = DataAccess().get_session()
        if not session.query(Student).filter(Student.username == username).first():
            student = Student(name, family, gender, national_code, birthday, address, phone_number, username, password)
            session.add(student)
            session.commit()
            return True, f"Student saved successfully {student}"
        else:
            raise DuplicateUsernameError

    @classmethod
    @exception_handling
    def edit(cls, student_id, name, family, gender, national_code, address, phone_number, username, password):
        session = DataAccess().get_session()
        student = session.query(Student).get(student_id)
        if student:
            student.name = name
            student.family = family
            student.gender = gender
            student.national_code = national_code
            student.address = address
            student.phone_number = phone_number
            student.username = username
            student.password = password
            session.commit()
            return True, f"Student edited successfully {student}"
        else:
            return False, "Student not found"

    @classmethod
    @exception_handling
    def remove(cls, student_id):
        session = DataAccess().get_session()
        student = session.query(Student).get(student_id)
        if student:
            session.delete(student)
            session.commit()
            return True, f"Student removed successfully {student}"
        else:
            return False, "Student not found"

    @classmethod
    @exception_handling
    def find_all(cls):
        session = DataAccess().get_session()
        return True, session.query(Student).all()

    @classmethod
    @exception_handling
    def find_by_student_id(cls, student_id):
        session = DataAccess().get_session()
        student = session.query(Student).get(student_id)
        if student:
            return True, student
        else:
            return False, "Student not found"