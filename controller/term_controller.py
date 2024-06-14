import datetime
from controller.exceptions.my_exceptions import TermNotFoundError, StudentNotFoundError
from controller.user_controller import UserController
from model.da.dataaccess import DataAccess
from model.entity.enrollment import CourseStatus, Enrollment
from model.entity.term import Term, TermStatus
from model.entity.course import Course
from model.entity.user import User
from model.tools.decorator.decorators import exception_handling

class TermController:
    @classmethod
    @exception_handling
    def save(cls, student_id, term_number, average_score, courses, start_date, end_date=None):
        result, student = UserController.find_by_user_id(student_id)
        if result:
            session = DataAccess().get_session()
            
            # Query courses from the current session
            course_objects = []
            for course in courses:
                course_obj = session.query(Course).get(course.id)
                if course_obj:
                    course_objects.append(course_obj)
            
            term = Term(student_id, term_number, average_score, course_objects)
            term.start_date = start_date
            term.end_date = end_date
            session.add(term)
            session.commit()
            session.refresh(term)
            session.close()
            return True, term
        else:
            raise StudentNotFoundError

    @classmethod
    @exception_handling
    def edit(cls, term_id, student_id=None, term_number=None, average_score=None, courses=None, start_date=None, end_date=None):
        session = DataAccess().get_session()
        term = session.query(Term).get(term_id)
        if not term:
            raise TermNotFoundError

        if student_id:
            result, student = UserController.find_by_user_id(student_id)
            if result:
                term.student_id = student_id
            else:
                raise StudentNotFoundError
        if term_number:
            term.term_number = term_number
        if average_score:
            term.average_score = average_score
        if courses is not None:
            course_objects = []
            for course in courses:
                course_obj = session.query(Course).get(course.id)
                if course_obj:
                    course_objects.append(course_obj)
            term.courses = course_objects
        if start_date:
            term.start_date = start_date
        if end_date:
            term.end_date = end_date

        session.commit()
        session.refresh(term)
        session.close()
        return True, term

    @classmethod
    @exception_handling
    def remove(cls, term_id):
        session = DataAccess().get_session()
        term = session.query(Term).get(term_id)
        if not term:
            raise TermNotFoundError

        session.delete(term)
        session.commit()
        session.close()
        return True, term

    @classmethod
    @exception_handling
    def load(cls, term_id):
        session = DataAccess().get_session()
        term = session.query(Term).get(term_id)
        session.close()
        if not term:
            raise TermNotFoundError
        return term
    
    @classmethod
    @exception_handling
    def query_terms(cls, student_id=None, term_number=None, start_date=None, end_date=None):
        session = DataAccess().get_session()
        query = session.query(Term)
        
        if student_id is not None:
            query = query.filter(Term.student_id == student_id)
        if term_number is not None:
            query = query.filter(Term.term_number == term_number)
        if start_date is not None:
            query = query.filter(Term.start_date >= start_date)
        if end_date is not None:
            query = query.filter(Term.end_date <= end_date)
        
        terms = query.all()
        session.close()
        return terms
    
    
    @classmethod
    @exception_handling
    def update_term_status(cls):
        session = DataAccess().get_session()
        terms = session.query(Term).filter(Term.status == TermStatus.IN_PROGRESS).all()
        
        for term in terms:
            if term.average_score is not None:
                new_status = CourseStatus.PASSED if term.average_score > 10 else CourseStatus.FAILED
                enrollments = session.query(Enrollment).filter(Enrollment.term_id == term.id).all()
                for enrollment in enrollments:
                    enrollment.status = new_status
        
        session.commit()
        session.close()
        return True
    
    @classmethod
    @exception_handling
    def create_new_term_for_each_student(cls):
        session = DataAccess().get_session()
        students = session.query(User).filter(User.role == 'student').all()
        
        for student in students:
            last_term = session.query(Term).filter(Term.student_id == student.id).order_by(Term.term_number.desc()).first()
            new_term_number = last_term.term_number + 1 if last_term else 1
            new_term = Term(student_id=student.id, term_number=new_term_number, average_score=None, courses=[])
            new_term.start_date = datetime.now()
            session.add(new_term)
        
        session.commit()
        session.close()
        return True