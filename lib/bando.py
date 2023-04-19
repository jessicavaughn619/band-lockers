#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import click

from db.models import Instrument, Locker, Student

# from helpers.greet import greet
# from helpers.count import count

class Cli:
    def __init__(self, user_input):
        self.students = [student for student in session.query(Student)]
        self.lockers = [locker for locker in session.query(Locker)]
        self.instruments = [instrument for instrument in session.query(Instrument)]
        self.name = user_input
        self.session = session
        self.start()

    def start(self):
        print(" ")
        print(f"~~ Welcome to Bando, {self.name}! ~~")
        print(" ")
        print("Here are some options to get started:")
        print(" ")
        print("Press S to search for information in the inventory.")
        print("Press A to add new data to the inventory.")
        print(" ") 
    
    def function2(self, session):
        if user_choice == "S":
            locker = input("Enter locker number or student last name: ")
            if type(locker) == int:
                Locker.print_combo_by_locker_number(session, locker_number=locker)
            if type(locker) == str:
                Locker.print_combo_by_last_name(session, last_name=locker)
        if user_choice == "A":
            print("You pressed A!")


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    user_input = input("Enter Your Name: ")
    Cli(user_input)
    user_choice = input("What would you like to do next? ")
    Cli.function2(user_choice, session)