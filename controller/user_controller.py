from controller.exceptions.my_exceptions import DuplicateUsernameError
from model.entity.user import *
from model.tools.decorator.decorators import exception_handling
from model.da.user_da import UserDa


class UserController:
    user_da = UserDa()

    @classmethod
    @exception_handling
    def save(cls, name, family, gender, national_code, birthday, adress, phone_number, username, password, term, courses, role):
        if not UserController.find_by_username(username)[0]:
            user = User(name, family, gender, national_code, birthday, adress, phone_number, username, password, term, courses,
                        role)
            user.role = role
            cls.user_da.save(user)
            return True, f"User saved successfully {user}"
        else:
            raise DuplicateUsernameError

    @classmethod
    @exception_handling
    def edit(cls, user_id, name, family, gender, national_code, adress, phone_number, username, password, term, courses,
             role):
        user = User(name, family, gender, national_code, adress, phone_number, username, password, term, courses, role)
        user.user_id = user_id
        user.role = role
        old_user = cls.user_da.find_by_id(user_id)
        cls.user_da.edit(user)
        return True, (f"User edited successfully From : {old_user} To : {user}")

    @classmethod
    @exception_handling
    def remove(cls, user_id):
        user = cls.user_da.find_by_id(user_id)
        cls.user_da.remove(user_id)
        return True, f"User removed successfully {user}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.user_da.find_all()

    @classmethod
    @exception_handling
    def find_by_user_id(cls, user_id):
        return True, cls.user_da.find_by_id(user_id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, cls.user_da.find_by_family(family)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, cls.user_da.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, cls.user_da.find_by_username_and_password(username, password)
