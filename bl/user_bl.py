from exceptoins.exceptoins import UserNotFoundError
from model.da.dataaccess import DataAccess
from model.entity import User

user_da = DataAccess(User)


class UserBl:
    @staticmethod
    def save(user):
        return user_da.save(user)

    @staticmethod
    def edit(user):
        if user_da.find_by_id(user.user_id):
            return user_da.edit(user)
        else:
            raise UserNotFoundError()

    @staticmethod
    def remove(user_id):
        user = user_da.find_by_id(user_id)
        if user:
            return user_da.remove(user)
        else:
            raise UserNotFoundError()

    @staticmethod
    def find_all():
        user_list = user_da.find_all()
        if user_list:
            return user_list
        else:
            raise UserNotFoundError()

    @staticmethod
    def find_by_id(user_id):
        user = user_da.find_by_id(user_id)
        if user:
            return user
        else:
            raise UserNotFoundError()

    @staticmethod
    def find_by_family(family):
        user_list = user_da.find_by(user.family == family)
        if user_list:
            return user_list
        else:
            raise UserNotFoundError()