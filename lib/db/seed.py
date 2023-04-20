from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Locker, Instrument, Student)

fake = Faker()

engine = create_engine("sqlite:///band_lockers.db")
session = Session(engine, future=True)

def delete_records():
    session.query(Locker).delete()
    session.query(Instrument).delete()
    session.query(Student).delete()
    session.commit()

def create_records():
    # students
    grade_levels = [9, 10, 11, 12]
    students = [Student(
        first_name=f'{fake.first_name()}',
        last_name=f'{fake.last_name()}',
        grade_level=random.choice(grade_levels)
    ) for i in range(80)]

    # lockers
    lockers = [Locker(
        number = fake.unique.random_int(min=1, max=150),
        combination = f'{fake.random_int(min=0, max=39)}-{fake.random_int(min=0, max=39)}-{fake.random_int(min=0, max=39)}',
        student_id = fake.random_int(min=1, max=80)
    ) for i in range(150)]

    # instruments
    instrument_types = ["Flute", "Oboe", "Clarinet", "Alto Saxophone", "Tenor Saxophone", "Bari Saxophone", "French Horn", "Bassoon", "Bass Clarinet", "Trumpet", "Trombone", "Euphonium", "Tuba"]
    instruments = [Instrument(
        type = random.choice(instrument_types),
        student_id = fake.random_int(min=1, max=80)
    ) for i in range(80)]

    session.add_all(students + lockers + instruments)
    session.commit()
    return students, lockers, instruments

if __name__ == "__main__":
    delete_records()
    create_records()


    session.close()
    session.commit()
