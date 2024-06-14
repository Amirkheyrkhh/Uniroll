from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QMessageBox, QListWidget, QListWidgetItem
from controller.term_controller import TermController
from controller.course_controller import CourseController
from model.entity.course import Course
from model.entity.professor_term import ProfessorTerm

class ProfessorView(QMainWindow):
    def __init__(self, professor):
        super().__init__()
        self.professor = professor
        self.setWindowTitle(f"Welcome Professor {professor.name} {professor.family}")
        self.setGeometry(100, 100, 800, 600)
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        self.term_label = QLabel("Select Term:")
        self.layout.addWidget(self.term_label)
        
        self.term_combo_box = QComboBox()
        self.term_combo_box.currentIndexChanged.connect(self.load_courses)
        self.layout.addWidget(self.term_combo_box)
        
        self.course_list_label = QLabel("Courses in Selected Term:")
        self.layout.addWidget(self.course_list_label)
        
        self.course_list_widget = QListWidget()
        self.layout.addWidget(self.course_list_widget)
        
        self.course_name_label = QLabel("Course Name:")
        self.layout.addWidget(self.course_name_label)
        
        self.course_name_input = QLineEdit()
        self.layout.addWidget(self.course_name_input)
        
        self.course_capacity_label = QLabel("Course Capacity:")
        self.layout.addWidget(self.course_capacity_label)
        
        self.course_capacity_input = QLineEdit()
        self.layout.addWidget(self.course_capacity_input)
        
        self.course_unit_count_label = QLabel("Course Unit Count:")
        self.layout.addWidget(self.course_unit_count_label)
        
        self.course_unit_count_input = QLineEdit()
        self.layout.addWidget(self.course_unit_count_input)
        
        self.prerequisites_label = QLabel("Select Prerequisites:")
        self.layout.addWidget(self.prerequisites_label)
        
        self.prerequisites_list_widget = QListWidget()
        self.prerequisites_list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.layout.addWidget(self.prerequisites_list_widget)
        
        self.add_course_button = QPushButton("Add Course")
        self.add_course_button.clicked.connect(self.add_course)
        self.layout.addWidget(self.add_course_button)
        
        self.load_terms()
        self.load_all_courses()
    
    def load_terms(self):
        success, terms = TermController.find_all()
        if success:
            for term in terms:
                self.term_combo_box.addItem(f"{term.educational_full_year} - Term {term.educational_half_year}", term.id)
        else:
            QMessageBox.critical(self, "Error", "Failed to load terms")
    
    def load_all_courses(self):
        success, courses = CourseController.find_all()
        if success:
            for course in courses:
                item = QListWidgetItem(course.name)
                item.setData(1, course.id)
                self.prerequisites_list_widget.addItem(item)
        else:
            QMessageBox.critical(self, "Error", "Failed to load courses")
    
    def load_courses(self):
        self.course_list_widget.clear()
        term_id = self.term_combo_box.currentData()
        success, courses = CourseController.find_by_term_id(term_id)
        if success:
            for course in courses:
                if isinstance(course, Course):
                    item = QListWidgetItem(course.name)
                    item.setData(1, course.id)
                    self.course_list_widget.addItem(item)
                else:
                    QMessageBox.critical(self, "Error", "Invalid course data")
                    break
        else:
            QMessageBox.critical(self, "Error", "Failed to load courses for the selected term")
        
    def add_course(self):
        term_id = self.term_combo_box.currentData()
        course_name = self.course_name_input.text()
        course_capacity = self.course_capacity_input.text()
        course_unit_count = self.course_unit_count_input.text()
        
        if not course_name or not course_capacity or not course_unit_count:
            QMessageBox.warning(self, "Input Error", "All fields are required")
            return
        
        try:
            course_capacity = int(course_capacity)
            course_unit_count = int(course_unit_count)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Capacity and Unit Count must be integers")
            return
        
        selected_prerequisites = [item.data(1) for item in self.prerequisites_list_widget.selectedItems()]
        
        success, added_course = CourseController.save(course_name, selected_prerequisites, course_capacity, course_unit_count)
        if success:
            course_id = added_course.id
            professor_term_id = self.get_professor_term_id(term_id)
            if professor_term_id:
                CourseController.assign_professor(professor_term_id, course_id)
                QMessageBox.information(self, "Success", f"Course added and assigned successfully: {added_course}")
            else:
                QMessageBox.critical(self, "Error", "Failed to assign professor to the course")
        else:
            QMessageBox.critical(self, "Error", added_course)
        
    def get_professor_term_id(self, term_id):
        success, professor_terms = TermController.find_professors_by_term_id(term_id)
        if success:
            for professor_term in professor_terms:
                if isinstance(professor_term, ProfessorTerm):
                    if professor_term.professor_id == self.professor.id:
                        return professor_term.id
                else:
                    QMessageBox.critical(self, "Error", "Invalid professor term data")
                    break
        return None