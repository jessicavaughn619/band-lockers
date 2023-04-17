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
    
    def print_combo_by_locker_number(session, locker_number):
        combo = session.query(Locker).filter(Locker.number == locker_number).first()
        if combo:
            print(combo)
        else:
            print("There is no matching locker number in the database.")

    def print_combo_by_last_name(session, last_name):
        student = (session.query(Student).filter(Student.last_name == last_name).first())
        if student:
            print(session.query(Locker).filter(Locker.student_id == student.id).first())
        else:
            print("There is no locker assigned to a student matching the last name entered.")

    
class Instrument(Base):
    __tablename__ = "instruments"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    type = Column(String())

    student_id = Column(Integer(), ForeignKey("students.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Type: {self.type}'

    def count_instruments(session, instrument):
        instrument_count = session.query(Instrument).filter(Instrument.type.like(instrument)).count()
        if instrument_count > 0:
            print(f"There are {instrument_count} {instrument}(s) currently assigned to students.")
        if instrument_count == 0:
            print("None of this instrument type are currently assigned to students.")

    def print_student_instruments(session, last_name):
        student = session.query(Student).filter(Student.last_name == last_name).first()
        instruments = (session.query(Instrument).filter(Instrument.student_id == student.id).all())
        if instruments:
            print(instruments)
        else:
            print("There are no instruments assigned to a student matching the last name entered.")
    
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
    
    # def delete_seniors(session):
    #     seniors = session.query(Student).filter(Student.grade_level == 12)
    #     session.delete(seniors)
    #     session.commit()
    
    # def increase_grade_level(session):
    #     session.query(Student).update({Student.grade_level: Student.grade_level + 1})
    #     print("Increased all student grade levels by one year.")
    
    def count_students_by_grade(session, grade):
        grade_count = (session.query(Student).filter(Student.grade_level == grade).count())
        print(f"There are {grade_count} student(s) in grade {grade}.")

    def find_by_last_name(session, last_name):
        print(session.query(Student).filter(Student.last_name == last_name).all())