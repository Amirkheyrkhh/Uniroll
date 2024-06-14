from controller.exceptions.my_exceptions import ProfessorNotFoundError, CourseNotFoundError
from controller.user_controller import UserController
from model.da.dataaccess import DataAccess
from model.entity.course import Course
from model.tools.decorator.decorators import exception_handling
from sqlalchemy.orm.session import make_transient

class CourseController:
    @classmethod
    @exception_handling
    def save(cls, name, prerequisites, professor_id, capacity, unit_count):
        result, professor = UserController.find_by_user_id(professor_id)
        if result:
            session = DataAccess().get_session()
            
            # Query prerequisites from the current session
            prerequisite_objects = []
            for prereq in prerequisites:
                prereq_obj = session.query(Course).get(prereq.id)
                if prereq_obj:
                    prerequisite_objects.append(prereq_obj)
            
            course = Course(name, prerequisite_objects, professor_id, capacity, unit_count)
            session.add(course)
            session.commit()
            session.refresh(course)
            session.close()
            return True, course
        else:
            raise ProfessorNotFoundError

    @classmethod
    @exception_handling
    def edit(cls, course_id, name=None, prerequisites=None, professor_id=None, capacity=None, unit_count=None):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        if not course:
            raise CourseNotFoundError

        if name:
            course.name = name
        if prerequisites is not None:
            prerequisite_objects = []
            for prereq in prerequisites:
                prereq_obj = session.query(Course).get(prereq.id)
                if prereq_obj:
                    prerequisite_objects.append(prereq_obj)
            course.prerequisites = prerequisite_objects
        if professor_id:
            result, professor = UserController.find_by_user_id(professor_id)
            if result:
                course.professor_id = professor_id
            else:
                raise ProfessorNotFoundError
        if capacity:
            course.capacity = capacity
        if unit_count:
            course.unit_count = unit_count

        session.commit()
        session.refresh(course)
        session.close()
        return True, course

    @classmethod
    @exception_handling
    def remove(cls, course_id):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        if not course:
            raise CourseNotFoundError

        # Remove the course from the prerequisites of other courses
        for other_course in session.query(Course).all():
            if course in other_course.prerequisites:
                other_course.prerequisites.remove(course)

        session.delete(course)
        session.commit()
        session.close()
        return True, course

    @classmethod
    @exception_handling
    def load(cls, course_id):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        session.close()
        if not course:
            raise CourseNotFoundError
        return course