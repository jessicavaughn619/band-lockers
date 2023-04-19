#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import re
from db.models import Instrument, Locker, Student

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
        print("Press S to search the database (lookup locker combos, instrument assignments, and individual students).")
        print("Press P to print student rosters by grade level.")
        print("Press A to add new data to the inventory.")
        print(" ")
    
    def function2a(self, session):
        while search_option == "a":
            print(" ")
            combo_search = input("Enter locker number or student last name: ")
            print(" ")
            int_pattern = r'\d'
            regex = re.compile(int_pattern)
            match = regex.search(combo_search)
            if match:
                Locker.print_combo_by_locker_number(session, locker_number=combo_search)
            elif combo_search == "Q":
                break
            elif not match:
                Locker.print_combo_by_last_name(session, last_name=combo_search)
    
    def function2b(self, session):
        while search_option == "b":
            print(" ")

    def function2c(self, session):
        while search_option == "c":
            print(" ")
        
    def function5(self, session):
        while user_choice == "P":
            grade = input("Enter grade level: ")
            if grade == "9" or grade == "10" or grade == "11" or grade == "12":
                Student.print_students_by_grade(session, grade=grade)
                print(" ")
                Student.count_students_by_grade(session, grade=grade)
                print(" ")
            elif grade == "Q":
                break
            else:
                print(f"You entered: {grade}, which is invalid. Please enter 9, 10, 11, or 12 to print students by grade level.")

    def function6(self, session):
        if user_choice == "A":
            print("You pressed A!")


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    user_input = input("Enter Your Name: ")
    Cli(user_input)
    user_choice = input("What would you like to do next? ")
    if user_choice == "S":
        print(" ")
        print("SEARCH QUERIES:")
        print(" ")
        print("Select from the following options:")
        print("a: Look up locker combinations by locker number or student last name.")
        print("b: Look up instrument assignments by student last name.")
        print("c: Look up individual students by student last name.")
        print("Press Q to exit.")
        print(" ")
        search_option = input("Selection: ")
        if search_option == "a":
            print(" ")
            print("Search for locker combinations by locker number or student last name.")
            Cli.function2a(search_option, session)
        elif search_option == "b":
            print(" ")
            print("Search for instrument assignments by student last name.")
            Cli.function2b(search_option, session)
        elif search_option == "c":
            print(" ")
            print("Search for individual students by student last name.")
            Cli.function2c(search_option, session)
    elif user_choice == "P":
        print(" ")
        print("This script prints a list of students by grade level and includes a final count of students.")
        print("Press Q to exit.")
        print(" ")
        Cli.function5(user_choice, session)
    elif user_choice == "A":
        Cli.function6(user_choice, session)
    elif user_choice == "I":
        pass
