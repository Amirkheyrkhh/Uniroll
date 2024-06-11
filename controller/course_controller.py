from controller.exceptions.my_exceptions import ProfessorNotFoundError
from controller.user_controller import UserController
from model.da.dataaccess import DataAccess
from model.entity.course import Course
from model.tools.decorator.decorators import exception_handling


class CourseController:
    @classmethod
    @exception_handling
    def save(cls, name, prerequisites, professor_id, capacity):
        result, professor = UserController.find_by_user_id(professor_id)
        if result:
            session = DataAccess().get_session()
            course = Course(name, prerequisites, professor_id, capacity)
            session.add(course)
            session.commit()
            return True, f"Course saved successfully {course}"
        else:
            raise ProfessorNotFoundError

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.course_da.find_all()

    @classmethod
    @exception_handling
    def find_by_user_id(cls, user_id):
        return True, cls.course_da.find_by_user_id(user_id)
