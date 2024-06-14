from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QWidget, QListWidget, QListWidgetItem, QHBoxLayout, QHeaderView
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from controller.term_controller import TermController
from model.entity.term import Term
from datetime import datetime
from view.add_term_view import AddTermView

import pathlib
current_directory = str(pathlib.Path(__file__).parent.absolute())
plus_icon_path = current_directory + "/assets/icons/plus.png"

class AdminView(QMainWindow):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(f"Welcome admin {self.admin.name} {self.admin.family}")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.term_table = QTableWidget()
        self.term_table.setColumnCount(4)
        self.term_table.setHorizontalHeaderLabels(['Start Date', 'End Date', 'Educational Year', 'Actions'])
        self.term_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.term_table)
        
        self.load_terms()
        
        self.button_layout = QHBoxLayout()
        
        self.add_button = QPushButton()
        self.add_button.setIcon(QIcon(plus_icon_path))
        self.add_button.clicked.connect(self.add_term)
        self.button_layout.addWidget(self.add_button)
        
        self.layout.addLayout(self.button_layout)
    
    def load_terms(self):
        success, terms = TermController.find_all()
        self.terms  = terms
        if success:
            self.term_table.setRowCount(len(terms))
            for row, term in enumerate(terms):
                self.term_table.setItem(row, 0, QTableWidgetItem(term.start_date.strftime('%Y-%m-%d')))
                self.term_table.setItem(row, 1, QTableWidgetItem(term.end_date.strftime('%Y-%m-%d') if term.end_date else ''))
                self.term_table.setItem(row, 2, QTableWidgetItem(str(term.educational_full_year)))
                
                for col in range(3):
                    self.term_table.item(row, col).setFlags(self.term_table.item(row, col).flags() & ~Qt.ItemIsEditable)
                
                close_button = QPushButton("Close")
                close_button.clicked.connect(lambda _, r=row: self.close_term(r))
                self.term_table.setCellWidget(row, 3, close_button)
        else:
            QMessageBox.critical(self, "Error", "Failed to load terms")
    
    def add_term(self):
        # Open a new view to add a term
        self.add_term_view = AddTermView(self)
        self.add_term_view.term_added.connect(self.load_terms)  # Connect the signal to the slot
        self.add_term_view.show()
    
    def close_term(self, row):
        term_id = self.terms[row].id
        success, message = TermController.close_term(term_id)
        if success:
            QMessageBox.information(self, "Success", f"Term {term_id} closed successfully")
            self.load_terms()
        else:
            QMessageBox.critical(self, "Error", f"Failed to close term {term_id}: {message}")