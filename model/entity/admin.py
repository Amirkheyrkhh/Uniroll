from sqlalchemy import Column, Integer, ForeignKey
from model.entity.user import User

class Admin(User):
    __tablename__ = 'admin_tbl'
    id = Column(Integer, ForeignKey('user_tbl.id'), primary_key=True)

    def __init__(self, name, family, gender, national_code, birthday, address, phone_number, username, password):
        super().__init__(name, family, gender, national_code, birthday, address, phone_number, username, password)