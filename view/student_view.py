from tkinter import ttk
from tkinter.ttk import Combobox

from ttkthemes.themed_tk import ThemedTk

from view.components.placeholder_entry import PlaceholderEntry
from view.components.rounded_button import RoundedButton
from controller.course_controller import CourseController

class StudentView(ThemedTk):

    def __init__(self, student):
        super().__init__()
        self.student = student

    def show(self):
        self.title(f"Welcome, {self.student.name}, {self.student.family}")
        self.geometry("800x600")
        self.configure(bg='white')

        # Create a table showing the courses belonging to the professor
        self.courses_table = ttk.Treeview(self)
        self.courses_table["columns"] = ("Course Name", "Capacity")
        self.courses_table.column("#0", width=0, stretch=False)
        self.courses_table.column("Course Name", anchor="w", width=100)
        self.courses_table.column("Capacity", anchor="w", width=100)
        self.courses_table.heading("#0", text="", anchor="w")
        self.courses_table.heading("Course Name", text="Course Name", anchor="w")
        self.courses_table.heading("Capacity", text="Capacity", anchor="w")
        self.courses_table.pack(fill='x', pady=10)

        for course in self.student.courses:
            self.courses_table.insert("", "end", values=(course.name, course.capacity))

        # Create a form to add a new course
        self.name_entry = PlaceholderEntry(self, placeholder="Name", font=("Helvetica", 12))
        self.name_entry.pack(pady=10)

        self.capacity_entry = PlaceholderEntry(self, placeholder="Capacity", font=("Helvetica", 12))
        self.capacity_entry.pack(pady=10)

        self.prerequisites_dropdown = Combobox(self)
        self.prerequisites_dropdown['values'] = [course.name for course in self.student.courses]
        self.prerequisites_dropdown.pack(pady=10)

        self.add_course_button = RoundedButton(self, text="Add Course", command=self.add_course)
        self.add_course_button.pack(pady=10)

        self.mainloop()

    def add_course(self):
        name = self.name_entry.get()
        capacity = int(self.capacity_entry.get())
        prerequisites = [course for course in self.student.courses if course.name == self.prerequisites_dropdown.get()]

        result, message = CourseController.save(name, prerequisites, self.student.id, capacity)
        if result:
            self.courses_table.insert("", "end", values=(name, capacity))
        else:
            print(message)  # Replace this with your preferred method of displaying error messages