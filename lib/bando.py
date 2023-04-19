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
        print("Please select from the following options:")
        print(" ")
        print("Press S to search the database (lookup locker combos, instrument assignments, and individual students).")
        print("Press P to print student rosters by grade level.")
        print("Press A to add new data to the inventory.")
        print(" ")
        print("Press Q to quit.")
        print(" ")
    
    def function1a(self, session):
        while search_option == "a":
            print(" ")
            combo_search = input("Enter locker number or student last name: ")
            print(" ")
            int_pattern = r'\d'
            regex = re.compile(int_pattern)
            match = regex.search(combo_search)
            if combo_search == "Q":
                break
            elif match:
                Locker.print_combo_by_locker_number(session, locker_number=combo_search)
            elif not match:
                Locker.print_combo_by_last_name(session, last_name=combo_search)
    
    def function1b(self, session):
        while search_option == "b":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                Instrument.print_student_instruments(session, last_name=record)

    def function1c(self, session):
        while search_option == "c":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                Student.find_by_last_name(session, last_name=record)
        
    def function2(self, session):
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

    def function3(self, session):
        if user_choice == "A":
            print("You pressed A!")


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    print(" ")
    user_input = input("Enter Your Name: ")
    while user_input:
        Cli(user_input)
        user_choice = input("What would you like to do next? ")
        if user_choice == "S":
            print(" ")
            print("SEARCH QUERIES:")
            print(" ")
            print("Select from the following options:")
            print("a: Search for locker combinations by locker number or student last name.")
            print("b: Search for instrument assignments by student last name.")
            print("c: Search for individual students by student last name.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                print(" ")
                print("Search for locker combinations by locker number or student last name.")
                Cli.function1a(search_option, session)
            elif search_option == "b":
                print(" ")
                print("Search for instrument assignments by student last name.")
                Cli.function1b(search_option, session)
            elif search_option == "c":
                print(" ")
                print("Search for individual students by student last name.")
                Cli.function1c(search_option, session)
        elif user_choice == "P":
            print(" ")
            print("Print a list of students by grade level including a final count of students.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            Cli.function2(user_choice, session)
        elif user_choice == "A":
            print(" ")
            Cli.function3(user_choice, session)
        elif user_choice == "Q":
            break
        else:
            print("Invalid option entered. Please select from the list of options or press Q to exit.")
