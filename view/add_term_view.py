from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDateEdit, QMessageBox, QCheckBox
from PyQt5.QtCore import QDate, pyqtSignal
from controller.term_controller import TermController
from datetime import datetime
from PyQt5.QtCore import Qt


class AddTermView(QDialog):
    term_added = pyqtSignal()  # Signal to indicate a term was added

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Add Term")
        self.setGeometry(150, 150, 400, 250)
        
        self.layout = QVBoxLayout(self)
        
        self.start_date_label = QLabel("Start Date:")
        self.layout.addWidget(self.start_date_label)
        
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate())
        self.layout.addWidget(self.start_date_edit)
        
        self.end_date_checkbox = QCheckBox("Has End Date")
        self.end_date_checkbox.setChecked(True)
        self.end_date_checkbox.stateChanged.connect(self.toggle_end_date)
        self.layout.addWidget(self.end_date_checkbox)
        
        self.end_date_label = QLabel("End Date:")
        self.layout.addWidget(self.end_date_label)
        
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())
        self.layout.addWidget(self.end_date_edit)
        
        self.add_button = QPushButton("Add Term")
        self.add_button.clicked.connect(self.add_term)
        self.layout.addWidget(self.add_button)
    
    def toggle_end_date(self, state):
        if state == Qt.Checked:
            self.end_date_edit.setEnabled(True)
        else:
            self.end_date_edit.setEnabled(False)
    
    def add_term(self):
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate() if self.end_date_checkbox.isChecked() else None
        
        success, message = TermController.save(start_date, end_date)
        if success:
            QMessageBox.information(self, "Success", "Term added successfully")
            self.term_added.emit()  # Emit the signal
            self.accept()
        else:
            QMessageBox.critical(self, "Error", f"Failed to add term: {message}")