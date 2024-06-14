from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from controller.user_controller import UserController
from view.professor_view import ProfessorView
from view.student_view import StudentView

class LoginView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.username_entry = QLineEdit(self)
        self.username_entry.setPlaceholderText("Username")
        self.username_entry.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.username_entry)

        self.password_entry = QLineEdit(self)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.password_entry)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

        self.professor_view = None  # Keep a reference to the ProfessorView instance

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        try:
            result, user = UserController.login(username, password)
            if result:
                if user.type == "professor":
                    self.professor_view = ProfessorView(user)
                    self.professor_view.show()
                    self.close()
                elif user.type == "admin":
                    self.close()
                elif user.type == "student":
                    self.student_view = StudentView(user)
                    self.student_view.show()
                    self.close()
                else:
                    QMessageBox.critical(self, "Error", "Invalid user type.")
            else:
                QMessageBox.critical(self, "Error", "Login failed. Please check your username and password.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")