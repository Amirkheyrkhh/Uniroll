from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from model.entity.base import Base

# Association table for the many-to-many relationship
prerequisite_table = Table('prerequisite_tbl', Base.metadata,
                           Column('course_id', Integer, ForeignKey('course_tbl.id')),
                           Column('prerequisite_id', Integer, ForeignKey('course_tbl.id'))
                           )

class Course(Base):
    __tablename__ = 'course_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    professor_id = Column(Integer, ForeignKey('user_tbl.id'))
    capacity = Column(Integer, nullable=False)
    unit_count = Column(Integer, nullable=True)
    prerequisites = relationship("Course",
                                 secondary=prerequisite_table,
                                 primaryjoin=id == prerequisite_table.c.course_id,
                                 secondaryjoin=id == prerequisite_table.c.prerequisite_id,
                                 backref="next_courses",
                                 cascade="save-update, merge")

    def __init__(self, name, prerequisites, professor_id, capacity, unit_count):
        super().__init__()
        self.course_id = None
        self.name = name
        self.prerequisites = prerequisites
        self.professor_id = professor_id
        self.capacity = capacity
        self.unit_count = unit_count