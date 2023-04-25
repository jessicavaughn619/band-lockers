from db.models import Locker, Student, Instrument
import inquirer
import pandas
import re

def function2a(session, search_option):
    print(" ")
    print("Print a list of students by grade level including a final count of students.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option == "a":
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

def print_students_by_grade(session, grade):
    students = (session.query(Student).filter(Student.grade_level == grade)).all()
    student_data = ([(student.first_name, student.last_name) for student in students])
    print(pandas.DataFrame(student_data, columns=["First Name", "Last Name"]))

def count_students_by_grade(session, grade):
    grade_count = (session.query(Student).filter(Student.grade_level == grade).count())
    print(f"There are {grade_count} student(s) in grade {grade}.")

def function2b(session, search_option):
    print(" ")
    print("Count the number of instruments in inventory.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option == "b":
        print(" ")
        instrument = input("Enter instrument type: ")
        instrument_types = ["Flute", "Oboe", "Clarinet", "Alto Saxophone", "Tenor Saxophone", "Bari Saxophone", "French Horn", "Bassoon", "Bass Clarinet", "Trumpet", "Trombone", "Euphonium", "Tuba"]
        if instrument in instrument_types:
            print(" ")
            count_instruments(session, instrument=instrument)
        elif instrument == "Q":
            break
        else:
            print(f"You entered: {instrument}, which is invalid. Please select from the following list of instruments: {instrument_types}")

def count_instruments(session, instrument):
    instrument_count = session.query(Instrument).filter(Instrument.type.like(instrument)).count()
    if instrument_count > 0:
        print(f"There are {instrument_count} {instrument}(s) currently assigned to students.")
    if instrument_count == 0:
        print("None of this instrument type are currently assigned to students.")