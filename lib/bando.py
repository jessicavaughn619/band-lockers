#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.models import Instrument, Locker, Student

# from helpers.greet import greet
# from helpers.count import count

class Cli:
    def __init__(self, user_input):
        self.students = [student for student in session.query(Student)]
        self.lockers = [locker for locker in session.query(Locker)]
        self.instruments = [instrument for instrument in session.query(Instrument)]
        self.name = user_input
        self.start()

    def start(self):
        print(' ')
        print(f'Welcome to Bando {self.name}!')
        print(' ')

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    user_input = input("Enter Your Name:")
    Cli(user_input)