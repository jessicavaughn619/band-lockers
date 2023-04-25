#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Instrument, Locker, Student
from helpers import (assign_locker, assign_instrument, update_student_info, 
                     increase_grade_levels, delete_student_record, delete_instrument_record, 
                     delete_students_by_grade)
from subfunctions.function1 import (function1a, function1b, function1c)
from subfunctions.function2 import (function2a, function2b)
from subfunctions.function3 import (function3a, function3b)

class Cli:
    def __init__(self):
        self.students = [student for student in session.query(Student)]
        self.lockers = [locker for locker in session.query(Locker)]
        self.instruments = [instrument for instrument in session.query(Instrument)]
        self.session = session
        self.main_menu()

    def main_menu(self):
        print(" ")
        user_name = input("Enter Your Name: ")
        while user_name:
            print(" ")
            print(f"~~ Welcome to Bando, {user_name}! ~~")
            print(" ")
            print("Please select from the following options:")
            print(" ")
            print("Press S to search the database.")
            print("Press P to print records.")
            print("Press C to create new data entries.")
            print("Press U to update database entries.")
            print("Press D to delete database entries.")
            print(" ")
            print("Press Q to quit.")
            print(" ")
            user_choice = input("What would you like to do next? ")
            if user_choice == "S":
                Cli.function1(self, user_choice)
            elif user_choice == "P":
                Cli.function2(self, user_choice)
            elif user_choice == "C":
                Cli.function3(self, user_choice)
            elif user_choice == "U":
                Cli.function4(self, user_choice)
            elif user_choice == "D":
                Cli.function5(self, user_choice)
            elif user_choice == "Q":
                break
            else:
                print("Invalid option entered. Please select from the list of options or press Q to exit.")
                
    def function1(self, user_choice):
        while user_choice == "S":
            print(" ")
            print("SEARCH QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Search for locker combinations by locker number or student last name.")
            print("b: Search for instrument assignments by student last name.")
            print("c: Search for individual students by student last name.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function1a(session, search_option)
            elif search_option == "b":
                function1b(session, search_option)
            elif search_option == "c":
                function1c(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")
    
    def function2(self, user_choice):
        while user_choice == "P":
            print(" ")
            print("PRINT QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Print a list of students by grade level including a final count of students.")
            print("b: Count the number of instruments in inventory.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function2a(session, search_option)
            elif search_option == "b":
                function2b(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

    def function3(self, user_choice):
        while user_choice == "C":
            print(" ")
            print("CREATE NEW DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Add new student to database.")
            print("b: Add new instrument to database.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function3a(session, search_option)
            elif search_option == "b":
                function3b(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")
    
    def function4(self, user_choice):
        while user_choice == "U":
            print(" ")
            print("UPDATE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Assign or reassign locker to student.")
            print("b: Assign or reassign instrument to student.")
            print("c: Update student information.")
            print("d: Increase student grade levels.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function4a(self, session, search_option)
            elif search_option == "b":
                Cli.function4b(self, session, search_option)
            elif search_option == "c":
                Cli.function4c(self, session, search_option)
            elif search_option == "d":
                Cli.function4d(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function4a(self, session, search_option):
        print(" ")
        print("Assign or reassign locker to student.")
        while search_option == "a":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                assign_locker(session, last_name)
    
    def function4b(self, session, search_option):
        print(" ")
        print("Assign or reassign instrument to student.")
        while search_option == "b":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                assign_instrument(session, last_name)

    def function4c(self, session, search_option):
        print(" ")
        print("Update student information.")
        while search_option == "c":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                update_student_info(session, last_name)
    
    def function4d(self, session, search_option):
        print(" ")
        print("Increase all student grade levels by one year.")
        while search_option == "d":
            print(" ")
            confirm = input("Confirm update ALL student grade levels to increase by one year? n/Y: ")
            if confirm == "Y":
                print(" ")
                confirm_confirm = input("WARNING: Selecting Y will update ALL student grade levels to increase by one year. Press n/Y to confirm: ")
                if confirm_confirm == "Y":
                    increase_grade_levels(session)
                    print(" ")
                    print("Successfully increased all student grade levels by one year.")
                    break
                else: 
                    print("Student records NOT updated.")
                    break
            else:
                print("Student records NOT updated.")
                break

    def function5(self, user_choice):
        while user_choice == "D":
            print(" ")
            print("DELETE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Delete individual student from database.")
            print("b: Delete individual instrument from database.")
            print("c: Delete students by grade level.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function5a(self, session, search_option)
            elif search_option == "b":
                Cli.function5b(self, session, search_option)
            elif search_option == "c":
                Cli.function5c(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function5a(self, session, search_option):
        print(" ")
        print("Delete individual student from database.")
        while search_option == "a":
            print(" ")
            last_name = input("Enter student last name: ")
            delete_student_record(session, last_name)

    def function5b(self, session, search_option):
        print(" ")
        print("Delete individual instrument from database.")
        while search_option == "b":
            print(" ")
            instrument_id = input("Enter instrument ID: ")
            delete_instrument_record(session, instrument_id)

    def function5c(self, session, search_option):
        print(" ")
        print("Delete students by grade level.")
        while search_option == "c":
            print(" ")
            grade = input("Enter grade level to delete: ")
            delete_students_by_grade(session, grade)

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    Cli()
