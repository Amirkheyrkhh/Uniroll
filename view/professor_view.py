from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QWidget, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from controller.course_controller import CourseController
from controller.user_controller import UserController

class ProfessorView(QMainWindow):
    def __init__(self, professor):
        super().__init__()
        self.professor = professor
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"Welcome professor {self.professor.name} {self.professor.family}")
        self.setGeometry(100, 100, 800, 600)
    
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
    
        # Create a table showing the courses belonging to the professor
        self.courses_table = QTableWidget()
        self.courses_table.setColumnCount(4)
        self.courses_table.setHorizontalHeaderLabels(["Course Name", "Capacity", "Unit Count", "Prerequisites"])
        self.courses_table.cellClicked.connect(self.on_course_selected)
        self.layout.addWidget(self.courses_table)
    
        self.load_courses()
    
        # Create a form to add/edit a course
        self.name_entry = QLineEdit(self)
        self.name_entry.setPlaceholderText("Name")
        self.name_entry.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.name_entry)
    
        self.capacity_entry = QLineEdit(self)
        self.capacity_entry.setPlaceholderText("Capacity")
        self.capacity_entry.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.capacity_entry)
    
        self.unit_count_entry = QLineEdit(self)
        self.unit_count_entry.setPlaceholderText("Unit Count")
        self.unit_count_entry.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.unit_count_entry)
    
        self.prerequisites_list = QListWidget(self)
        self.prerequisites_list.setSelectionMode(QListWidget.MultiSelection)
        self.layout.addWidget(self.prerequisites_list)
        self.load_prerequisites_list()
    
        self.add_course_button = QPushButton("Add Course", self)
        self.add_course_button.clicked.connect(self.add_course)
        self.layout.addWidget(self.add_course_button)
    
        self.save_course_button = QPushButton("Save Course", self)
        self.save_course_button.clicked.connect(self.save_course)
        self.layout.addWidget(self.save_course_button)
    
        # self.edit_course_button = QPushButton("Edit Course", self)
        # self.edit_course_button.clicked.connect(self.edit_course)
        # self.layout.addWidget(self.edit_course_button)
    
        self.remove_course_button = QPushButton("Remove Course", self)
        self.remove_course_button.clicked.connect(self.remove_course)
        self.layout.addWidget(self.remove_course_button)
        
    def refreshUI(self):
        self.professor = UserController.find_by_user_id(self.professor.id)[1]
        self.load_prerequisites_list()
        
        self.name_entry.clear()
        self.capacity_entry.clear()
        self.unit_count_entry.clear()
        
    def load_prerequisites_list(self):
        self.prerequisites_list.clear()
        for course in self.professor.courses:
            item = QListWidgetItem(course.name)
            item.setData(Qt.UserRole, course.id)
            item.setCheckState(Qt.Unchecked)
            self.prerequisites_list.addItem(item)
    
    def load_courses(self):
        self.courses_table.setRowCount(len(self.professor.courses))
        for row, course in enumerate(self.professor.courses):
            self.courses_table.setItem(row, 0, QTableWidgetItem(course.name))
            self.courses_table.setItem(row, 1, QTableWidgetItem(str(course.capacity)))
            self.courses_table.setItem(row, 2, QTableWidgetItem(str(course.unit_count)))
            
            # Extract the names of the prerequisite courses
            prerequisite_names = [prereq.name for prereq in course.prerequisites]
            self.courses_table.setItem(row, 3, QTableWidgetItem(", ".join(prerequisite_names)))
    
    def on_course_selected(self, row, column):
        course = self.professor.courses[row]
        self.name_entry.setText(course.name)
        self.capacity_entry.setText(str(course.capacity))
        self.unit_count_entry.setText(str(course.unit_count))
    
        self.prerequisites_list.clear()
        for course in self.professor.courses:
            item = QListWidgetItem(course.name)
            item.setData(Qt.UserRole, course.id)
            if course in self.professor.courses[row].prerequisites:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.prerequisites_list.addItem(item)
    
    def add_course(self):
        name = self.name_entry.text()
        capacity = self.capacity_entry.text()
        unit_count = self.unit_count_entry.text()
    
        # Get selected prerequisites
        prerequisites = []
        for index in range(self.prerequisites_list.count()):
            item = self.prerequisites_list.item(index)
            if item.checkState() == Qt.Checked:
                course_id = item.data(Qt.UserRole)
                course = next((course for course in self.professor.courses if course.id == course_id), None)
                if course:
                    prerequisites.append(course)
    
        if not name or not capacity or not unit_count:
            QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return
    
        try:
            capacity = int(capacity)
            unit_count = int(unit_count)
        except ValueError:
            QMessageBox.critical(self, "Error", "Capacity and Unit Count must be integers.")
            return
    
        result, course = CourseController.save(name, prerequisites, self.professor.id, capacity, unit_count)
        if result:
            self.courses_table.insertRow(self.courses_table.rowCount())
            self.courses_table.setItem(self.courses_table.rowCount() - 1, 0, QTableWidgetItem(name))
            self.courses_table.setItem(self.courses_table.rowCount() - 1, 1, QTableWidgetItem(str(capacity)))
            self.courses_table.setItem(self.courses_table.rowCount() - 1, 2, QTableWidgetItem(str(unit_count)))
            self.courses_table.setItem(self.courses_table.rowCount() - 1, 3, QTableWidgetItem(", ".join([course.name for course in prerequisites])))
            self.refreshUI()
        else:
            QMessageBox.critical(self, "Error", "Could not add the course!")
    
    def save_course(self):
        selected_row = self.courses_table.currentRow()
        if selected_row < 0:
            QMessageBox.critical(self, "Error", "No course selected.")
            return
    
        course_id = self.professor.courses[selected_row].id
        name = self.name_entry.text()
        capacity = self.capacity_entry.text()
        unit_count = self.unit_count_entry.text()
    
        # Get selected prerequisites
        prerequisites = []
        for index in range(self.prerequisites_list.count()):
            item = self.prerequisites_list.item(index)
            if item.checkState() == Qt.Checked:
                pre_req_id = item.data(Qt.UserRole)
                prerequisites.extend(filter(lambda course: course.id == pre_req_id, self.professor.courses))
    
        if not name or not capacity or not unit_count:
            QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return
    
        try:
            capacity = int(capacity)
            unit_count = int(unit_count)
        except ValueError:
            QMessageBox.critical(self, "Error", "Capacity and Unit Count must be integers.")
            return
    
        result, course = CourseController.edit(course_id, name, prerequisites, self.professor.id, capacity, unit_count)
        if result:
            self.courses_table.setItem(selected_row, 0, QTableWidgetItem(name))
            self.courses_table.setItem(selected_row, 1, QTableWidgetItem(str(capacity)))
            self.courses_table.setItem(selected_row, 2, QTableWidgetItem(str(unit_count)))
            self.courses_table.setItem(selected_row, 3, QTableWidgetItem(", ".join([course.name for course in prerequisites])))
            self.refreshUI()
        else:
            QMessageBox.critical(self, "Error", "Could not save the course!")
     
    def remove_course(self):
        selected_row = self.courses_table.currentRow()
        if selected_row < 0:
            QMessageBox.critical(self, "Error", "No course selected.")
            return

        course_id = self.professor.courses[selected_row].id
        result = CourseController.remove(course_id)
        if result:
            # self.courses_table.removeRow(selected_row)
            # del self.professor.courses[selected_row]
            
            # Reload the professor's courses from the database
            self.refreshUI()
            self.load_courses()
        else:
            QMessageBox.critical(self, "Error", "Could not remove the course!")