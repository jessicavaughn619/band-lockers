from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Locker, Instrument, Student)

if __name__ == "__main__":
    engine = create_engine("sqlite:///instrument_lockers.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Locker).delete()
    session.query(Instrument).delete()
    session.query(Student).delete()

    locker2 = Locker(
        number = 1,
        combination = "00-00-00",
        student_id = 2
    )
    session.add(locker2)
    session.commit()

    olivia = Student(
        first_name = "Olivia",
        last_name = "Vaughn",
        grade_level = 9
    )
    session.add(olivia)
    session.commit()

    flute = Instrument(
        type = "Flute",
        student_id = 2
    )
    session.add(flute)
    session.commit()


    session.close()
    session.commit()