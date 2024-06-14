from controller.user_controller import UserController, UserType
from model.entity.user import Gender
from view.login_view import LoginView
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Define global CSS styles
    css = """
    QWidget {
        background-color: #f0f0f0;
    }
    QLineEdit {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    """

    # Apply the global CSS styles
    app.setStyleSheet(css)

    window = LoginView()
    window.show()
    sys.exit(app.exec_())
#
# from controller.user_controller import UserController, UserType
# from model.entity.user import Gender


# UserController.save("amir", "rajabi", Gender.Male, "0123456766", "sample", "sample", "09123456755", "amir", "123456", UserType.Student)
# UserController.save("iman", "mazaheri", Gender.Male, "0123456760", "sample", "sample", "09123456750", "iman", "123456", UserType.Professor)
# UserController.save("morteza", "omidi", Gender.Male, "0123055766", "sample", "sample", "09123456754", "morteza", "123456", UserType.Admin)
