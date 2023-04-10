from sqlalchemy import PrimaryKeyConstraint, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
    
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Locker(Base):
    __tablename__ = "lockers"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    number = Column(Integer())
    combination = Column(String())

    student_id = Column(Integer(), ForeignKey("students.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Number: {self.number} ' \
        + f'Combination: {self.combination}'
    
class Instrument(Base):
    __tablename__ = "instruments"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    type = Column(String())

    student_id = Column(Integer(), ForeignKey("students.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Type: {self.type}'
    
class Student(Base):
    __tablename__ = "students"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    first_name = Column(String())
    last_name = Column(String())
    grade_level = Column(Integer())

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'First Name: {self.first_name} ' \
        + f'Last Name: {self.last_name} ' \
        + f'Grade Level: {self.grade_level}'