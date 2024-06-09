from controller.exceptions.my_exceptions import NoPersonFoundError
from model.da import Da
from datetime import datetime
from model.entity import *

class CourseDA(Da):
    def save(self, course):
        self.connect()

        self.cursor.execute("INSERT INTO COURSE_TBL ()")