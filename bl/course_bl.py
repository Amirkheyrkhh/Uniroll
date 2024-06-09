from controller.exceptions.my_exceptions import CourseNotFoundError
from model.da.da import DataAccess
from model.entity import course

corse_da = DataAccess(course)

class CourseBl:
    @staticmethod
    def save(course):
        return corse_da.save(course)

    @staticmethod
    def edit(course):
        if corse_da.find_by_id(course.course_id):
            return corse_da.edit(course)
        else:
            raise CourseNotFoundError()

    @staticmethod
    def remove(course_id):
        user = corse_da.find_by_id(course_id)
        if user:
            return corse_da.remove(course)
        else:
            raise CourseNotFoundError()

    @staticmethod
    def find_all():
        course_list = corse_da.find_all()
        if course_list:
            return course_list
        else:
            raise CourseNotFoundError()

    @staticmethod
    def find_by_id(course_id):
        user = course_id.find_by_id(course_id)
        if user:
            return user
        else:
            raise CourseNotFoundError()