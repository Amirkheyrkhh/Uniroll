from controller.user_controller import UserController
from model.da.dataaccess import DataAccess
from model.entity.user import Gender
from view.login_view import LoginWindow

def main():
    window = LoginWindow()
    window.mainloop()

if __name__ == "__main__":
    # da = DataAccess()
    # da.create_tables()
    main()

# UserController.save("gholam", "shahi", Gender.Male, "0123456788", "sample", "sample", "09123456786", "gholam", "123456", "admin")