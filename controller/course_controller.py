from sqlalchemy.orm.exc import NoResultFound
from controller.exceptions.my_exceptions import CourseNotFoundError
from model.entity.course import Course
from model.entity.enrollment import Enrollment, CourseStatus
from model.entity.teaching import Teaching
from model.entity.student_term import StudentTerm
from model.entity.professor_term import ProfessorTerm
from model.entity.student import Student
from model.entity.professor import Professor
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess

class CourseController:
    @classmethod
    @exception_handling
    def save(cls, name, prerequisites, professor_id, capacity, unit_count):
        session = DataAccess().get_session()
        course = Course(name, prerequisites, professor_id, capacity, unit_count)
        session.add(course)
        session.commit()
        return True, f"Course saved successfully {course}"

    @classmethod
    @exception_handling
    def edit(cls, course_id, name, prerequisites, professor_id, capacity, unit_count):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        if course:
            course.name = name
            course.prerequisites = prerequisites
            course.professor_id = professor_id
            course.capacity = capacity
            course.unit_count = unit_count
            session.commit()
            return True, f"Course edited successfully {course}"
        else:
            raise CourseNotFoundError

    @classmethod
    @exception_handling
    def remove(cls, course_id):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        if course:
            session.delete(course)
            session.commit()
            return True, f"Course removed successfully {course}"
        else:
            raise CourseNotFoundError

    @classmethod
    @exception_handling
    def find_all(cls):
        session = DataAccess().get_session()
        return True, session.query(Course).all()

    @classmethod
    @exception_handling
    def find_by_course_id(cls, course_id):
        session = DataAccess().get_session()
        course = session.query(Course).get(course_id)
        if course:
            return True, course
        else:
            raise CourseNotFoundError

    @classmethod
    @exception_handling
    def find_by_professor_id(cls, professor_id):
        session = DataAccess().get_session()
        courses = session.query(Course).filter(Course.professor_id == professor_id).all()
        return True, courses

    @classmethod
    @exception_handling
    def find_by_name(cls, name):
        session = DataAccess().get_session()
        courses = session.query(Course).filter(Course.name == name).all()
        return True, courses

    @classmethod
    @exception_handling
    def enroll_student(cls, student_term_id, course_id, status=CourseStatus.IN_PROGRESS, score=None):
        session = DataAccess().get_session()
        enrollment = Enrollment(student_term_id=student_term_id, course_id=course_id, status=status, score=score)
        session.add(enrollment)
        session.commit()
        return True, f"Student term {student_term_id} enrolled in course {course_id} successfully"

    @classmethod
    @exception_handling
    def remove_student_from_course(cls, student_term_id, course_id):
        session = DataAccess().get_session()
        enrollment = session.query(Enrollment).filter_by(student_term_id=student_term_id, course_id=course_id).first()
        if enrollment:
            session.delete(enrollment)
            session.commit()
            return True, f"Student term {student_term_id} removed from course {course_id} successfully"
        else:
            return False, "Student term not found in the specified course"

    @classmethod
    @exception_handling
    def assign_professor(cls, professor_term_id, course_id):
        session = DataAccess().get_session()
        teaching = Teaching(professor_term_id=professor_term_id, course_id=course_id)
        session.add(teaching)
        session.commit()
        return True, f"Professor term {professor_term_id} assigned to course {course_id} successfully"

    @classmethod
    @exception_handling
    def remove_professor_from_course(cls, professor_term_id, course_id):
        session = DataAccess().get_session()
        teaching = session.query(Teaching).filter_by(professor_term_id=professor_term_id, course_id=course_id).first()
        if teaching:
            session.delete(teaching)
            session.commit()
            return True, f"Professor term {professor_term_id} removed from course {course_id} successfully"
        else:
            return False, "Professor term not found in the specified course"

    @classmethod
    @exception_handling
    def find_students_by_course_id(cls, course_id):
        session = DataAccess().get_session()
        students = session.query(Student).join(StudentTerm).join(Enrollment).filter(Enrollment.course_id == course_id).all()
        return True, students if students else "No students found for the given course"

    @classmethod
    @exception_handling
    def find_professors_by_course_id(cls, course_id):
        session = DataAccess().get_session()
        professors = session.query(Professor).join(ProfessorTerm).join(Teaching).filter(Teaching.course_id == course_id).all()
        return True, professors if professors else "No professors found for the given course"