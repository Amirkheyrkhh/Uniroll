from model.entity.user import User


class Admin(User):
    __mapper_args__ = {
        'polymorphic_identity':'admin',
    }


