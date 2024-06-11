import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
from controller.user_controller import UserController
from view.components.placeholder_entry import PlaceholderEntry
from view.professor_view import ProfessorView


class LoginWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")

        self.title("Login")
        self.geometry("300x200")

        self.configure(bg='white')

        self.username_entry = PlaceholderEntry(self, placeholder="Username", font=("Helvetica", 12))
        self.username_entry.pack(pady=10)

        self.password_entry = PlaceholderEntry(self, placeholder="Password", show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=10)

        self.login_button = ttk.Button(self, text="Login", command=self.login, style="RoundedButton.TButton")
        self.login_button.pack(pady=10)


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            result, user = UserController.find_by_username_and_password(username, password)
            if result:
                if user.type == 'professor':
                    self.destroy()
                    window = ProfessorView(user)
                    window.show()
            else:
                messagebox.showerror("Error", "Login failed. Please check your username and password.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# if __name__ == "__main__":
#     window = LoginWindow()
#     window.mainloop()