from sqlalchemy import Column, Integer, ForeignKey, Table, DateTime, Enum
from sqlalchemy.orm import relationship
from model.entity.base import Base
from enum import Enum as PyEnum
from datetime import datetime

class Term(Base):
    __tablename__ = 'term_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    def __init__(self, start_date, end_date=None):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date

    @property
    def ended(self):
        return self.end_date is not None

    @ended.setter
    def ended(self, value):
        if value:
            self.end_date = datetime.now()

    @property
    def educational_year(self):
        return self.start_date.year

    @property
    def educational_half_year(self):
        return 1 if self.start_date.month < 7 else 2
    
    @property
    def educational_full_year(self):
        return f"{self.educational_year}-{self.educational_year + 1}" if self.start_date.month < 7 else f"{self.educational_year - 1}-{self.educational_year}"