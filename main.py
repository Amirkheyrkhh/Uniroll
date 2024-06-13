from view.login_view import LoginView
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(app.exec_())
#
# StudentController.save("amir", "rajabi", Gender.Male, "0123456766", "sample", "sample", "09123456755", "amir", "123456", 1, None)
# UserController.save("iman", "mazaheri", Gender.Male, "0123456760", "sample", "sample", "09123456750", "iman", "123456", "professor")
# UserController.save("morteza", "omidi", Gender.Male, "0123055766", "sample", "sample", "09123456754", "morteza", "123456", "admin")
