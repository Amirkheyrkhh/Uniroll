from controller.user_controller import UserController
from model.entity import Course
from model.tools import exception_handling
from model.da import CourseDa



class CourseController:
    course_da = CourseDa()

    @classmethod
    @exception_handling
    def save(cls, name, prerequisites, professor, capacity, user_id):
        user = UserController.find_by_id(user_id)
        course = Course(name, prerequisites, professor, capacity)
        course.user = user[1]
        cls.course_da.save(course)
        return True, f"Course saved successfully {user}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.course_da.find_all()

    @classmethod
    @exception_handling
    def find_by_user_id(cls, user_id):
        return True, cls.course_da.find_by_user_id(user_id)
