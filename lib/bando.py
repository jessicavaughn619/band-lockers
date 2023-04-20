#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import re
from db.models import Instrument, Locker, Student
from helpers import (print_combo_by_locker_number, print_combo_by_last_name, print_student_instruments, find_by_last_name, print_students_by_grade, count_students_by_grade, add_instrument, add_student)

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
            print("a: Search for locker combinations by locker number or student last name.")
            print("b: Search for instrument assignments by student last name.")
            print("c: Search for individual students by student last name.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function1a(self, session, search_option)
            elif search_option == "b":
                Cli.function1b(self, session, search_option)
            elif search_option == "c":
                Cli.function1c(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function1a(self, session, search_option):
        print(" ")
        print("Search for locker combinations by locker number or student last name.")
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
                print_combo_by_locker_number(session, locker_number=combo_search)
            elif not match:
                print_combo_by_last_name(session, last_name=combo_search)
    
    def function1b(self, session, search_option):
        print(" ")
        print("Search for instrument assignments by student last name.")
        while search_option == "b":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                print_student_instruments(session, last_name=record)

    def function1c(self, session, search_option):
        print(" ")
        print("Search for individual students by student last name.")
        while search_option == "c":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                find_by_last_name(session, last_name=record)
        
    def function2(self, user_choice):
        print(" ")
        print("Print a list of students by grade level including a final count of students.")
        print(" ")
        print("Press Q to exit to main menu.")
        while user_choice == "P":
            print(" ")
            grade = input("Enter grade level: ")
            if grade == "9" or grade == "10" or grade == "11" or grade == "12":
                print_students_by_grade(session, grade=grade)
                print(" ")
                count_students_by_grade(session, grade=grade)
            elif grade == "Q":
                break
            else:
                print(f"You entered: {grade}, which is invalid. Please enter 9, 10, 11, or 12 to print students by grade level.")

    def function3(self, user_choice):
        while user_choice == "C":
            print(" ")
            print("CREATE NEW DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print("a: Add new student to database.")
            print("b: Add new instrument to database.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function3a(self, session, search_option)
            elif search_option == "b":
                Cli.function3b(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

    def function3a(self, session, search_option):
        print(" ")
        print("Add new student to database.")
        while search_option == "a":
            print(" ")
            first_name = input("Enter student first name: ")
            if first_name == "Q":
                break
            else:
                last_name = input("Enter student last name: ")
                grade_level = input("Enter student grade level: ")
                print(" ")
                print("Add the following new student to the database?")
                print(f"First Name: {first_name} Last Name: {last_name} Grade Level: {grade_level}")
                print(" ")
                confirm = input("n/Y: ")
                if confirm == "n":
                    print("Student NOT added to database.")
                elif confirm == "Y":
                    add_student(session, Student(first_name=first_name, last_name=last_name, grade_level=grade_level))
                    print("New student successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

    def function3b(self, session, search_option):
        print(" ")
        print("Add new instrument to database.")
        while search_option == "b":
            print(" ")
            type = input("Enter instrument type: ")
            if type == "Q":
                break
            else:
                print(" ")
                print("Add the following new instrument to the database?")
                print(f"Type: {type}")
                print(" ")
                confirm = input("n/Y: ")
                if confirm == "n":
                    print("Instrument NOT added to database.")
                elif confirm == "Y":
                    add_instrument(session, Instrument(type=type))
                    print("New instrument successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")
    
    def function4(self, user_choice):
        while user_choice == "U":
            print(" ")
            print("UPDATE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print("a: Assign or reassign locker to student.")
            print("b: Assign or reassign instrument to student.")
            print("c: Update student information.")
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
                print(" ")
                print("Is this the correct student record?")
                print(" ")
                find_by_last_name(session, last_name)
                print(" ")
                confirm_record = input("n/Y: ")
                if confirm_record == "n":
                    print("Locker assignment NOT updated.")
                elif confirm_record == "Y":
                    student_id = input("Enter student ID from record: ")
                    print(" ")
                    updated_locker = input("Enter new locker number: ")
                    print(" ")
                    print("Confirm assign the following locker number?")
                    print(" ")
                    print(f"Locker Number: {updated_locker}")
                    confirm = input("n/Y: ")
                    if confirm == "n":
                        print("Locker assignment NOT updated.")
                    elif confirm == "Y":
                        # assign_locker(session, locker=updated_locker, student_id=student_id)
                        print("Locker assignment successfully completed!")
                    elif confirm == "Q":
                        break
                    else:
                        print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")
    
    def function4b(self, session, search_option):
        print(" ")
        print("Assign or reassign instrument to student.")
        while search_option == "b":
            pass

    def function4c(self, session, search_option):
        print(" ")
        print("Update student information.")
        while search_option == "c":
            pass
    
    def function5(self, user_choice):
        while user_choice == "D":
            print(" ")
            print("DELETE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print("a: Delete student from database.")
            print("b: Delete instrument from database.")
            print("c: Update all grade levels and remove graduating seniors.")
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
        print("Delete student from database.")
        while search_option == "a":
            pass

    def function5b(self, session, search_option):
        print(" ")
        print("Delete instrument from database.")
        while search_option == "b":
            pass

    def function5c(self, session, search_option):
        print(" ")
        print("Update all grade levels and remove graduating seniors.")
        while search_option == "c":
            pass

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    Cli()
