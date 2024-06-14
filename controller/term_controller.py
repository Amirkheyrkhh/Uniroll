from sqlalchemy.orm.exc import NoResultFound
from model.entity.term import Term
from model.entity.student_term import StudentTerm, TermStatus
from model.entity.professor_term import ProfessorTerm
from model.entity.student import Student
from model.entity.professor import Professor
from model.tools.decorator.decorators import exception_handling
from model.da.dataaccess import DataAccess

class TermController:
    @classmethod
    @exception_handling
    def save(cls, start_date, end_date=None):
        session = DataAccess().get_session()
        term = Term(start_date, end_date)
        session.add(term)
        session.commit()
        return True, f"Term saved successfully {term}"

    @classmethod
    @exception_handling
    def edit(cls, term_id, start_date, end_date=None):
        session = DataAccess().get_session()
        term = session.query(Term).get(term_id)
        if term:
            term.start_date = start_date
            term.end_date = end_date
            term.ended = end_date is not None
            term.educational_year = start_date.year
            term.educational_half_year = 1 if start_date.month < 7 else 2
            session.commit()
            return True, f"Term edited successfully {term}"
        else:
            return False, "Term not found"

    @classmethod
    @exception_handling
    def remove(cls, term_id):
        session = DataAccess().get_session()
        term = session.query(TTerm).get(term_id)
        if term:
            session.delete(term)
            session.commit()
            return True, f"Term removed successfully {term}"
        else:
            return False, "Term not found"

    @classmethod
    @exception_handling
    def find_all(cls):
        session = DataAccess().get_session()
        return True, session.query(Term).all()

    @classmethod
    @exception_handling
    def find_by_term_id(cls, term_id):
        session = DataAccess().get_session()
        term = session.query(Term).get(term_id)
        if term:
            return True, term
        else:
            return False, "Term not found"

    @classmethod
    @exception_handling
    def find_by_year(cls, year):
        session = DataAccess().get_session()
        terms = session.query(Term).filter(Term.educational_year == year).all()
        return True, terms if terms else "No terms found for the given year"

    @classmethod
    @exception_handling
    def find_by_half_year(cls, half_year):
        session = DataAccess().get_session()
        terms = session.query(Term).filter(Term.educational_half_year == half_year).all()
        return True, terms if terms else "No terms found for the given half year"

    @classmethod
    @exception_handling
    def add_student_to_term(cls, student_id, term_id, status=TermStatus.IN_PROGRESS, average_score=None):
        session = DataAccess().get_session()
        student_term = StudentTerm(student_id=student_id, term_id=term_id, status=status, average_score=average_score)
        session.add(student_term)
        session.commit()
        return True, f"Student {student_id} added to term {term_id} successfully"

    @classmethod
    @exception_handling
    def remove_student_from_term(cls, student_id, term_id):
        session = DataAccess().get_session()
        student_term = session.query(StudentTerm).filter_by(student_id=student_id, term_id=term_id).first()
        if student_term:
            session.delete(student_term)
            session.commit()
            return True, f"Student {student_id} removed from term {term_id} successfully"
        else:
            return False, "Student not found in the specified term"

    @classmethod
    @exception_handling
    def add_professor_to_term(cls, professor_id, term_id, average_score=None):
        session = DataAccess().get_session()
        professor_term = ProfessorTerm(professor_id=professor_id, term_id=term_id, average_score=average_score)
        session.add(professor_term)
        session.commit()
        return True, f"Professor {professor_id} added to term {term_id} successfully"

    @classmethod
    @exception_handling
    def remove_professor_from_term(cls, professor_id, term_id):
        session = DataAccess().get_session()
        professor_term = session.query(ProfessorTerm).filter_by(professor_id=professor_id, term_id=term_id).first()
        if professor_term:
            session.delete(professor_term)
            session.commit()
            return True, f"Professor {professor_id} removed from term {term_id} successfully"
        else:
            return False, "Professor not found in the specified term"

    @classmethod
    @exception_handling
    def find_students_by_term_id(cls, term_id):
        session = DataAccess().get_session()
        students = session.query(Student).join(StudentTerm).filter(StudentTerm.term_id == term_id).all()
        return True, students if students else "No students found for the given term"

    @classmethod
    @exception_handling
    def find_professors_by_term_id(cls, term_id):
        session = DataAccess().get_session()
        professors = session.query(Professor).join(ProfessorTerm).filter(ProfessorTerm.term_id == term_id).all()
        return True, professors if professors else "No professors found for the given term"