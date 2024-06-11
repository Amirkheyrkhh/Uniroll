from sqlalchemy.orm import relationship

from model.entity.enrollment import enrollment_table
from model.entity.user import User


class Professor(User):
    __mapper_args__ = {
        'polymorphic_identity':'professor',
    }
    courses = relationship('Course', backref= 'professor')