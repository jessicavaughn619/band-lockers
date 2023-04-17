from sqlalchemy import PrimaryKeyConstraint, Column, Integer, String, MetaData, ForeignKey, select
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
    
    def print_combo_by_locker_number(session, locker_number):
        combo = select(Locker).filter_by(number=locker_number)
        print([record for record in combo])

#     def print_combo_by_last_name(session, last_name):
#         student = session.query(Student).filter(last_name==last_name)
#         locker = session.query(Locker).filter_by(student_id=student)

# # Student.id returning Locker.id = student.id, needs to return Locker.student_id = student.id
#         combo = [session.get(Locker, student.id) for student in student]
#         if combo:
#             print([record for record in combo])
#         if not combo:
#             print("This student does not have a locker assigned.")

    
class Instrument(Base):
    __tablename__ = "instruments"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    type = Column(String())

    student_id = Column(Integer(), ForeignKey("students.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Type: {self.type}'
    
# Need to add lowercase method

    @classmethod
    def count_instruments(session, instrument):
        print(session.query(Instrument).filter_by(type=instrument).count())

    # def student_instruments(session, last_name):
    #     student = session.query(Student).filter_by(last_name=last_name)
    #     instrument = [session.get(Instrument, student.id).filter_by(student_id=student.id) for student in student]
    #     print(instrument)
    
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
    
    @classmethod
    def count_students_by_grade(session, grade):
        print(session.query(Student).filter_by(grade_level=grade).count())