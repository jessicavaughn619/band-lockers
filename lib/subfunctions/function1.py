from db.models import Locker, Student, Instrument
import inquirer
import pandas
import re

def function1a(session, search_option):
    print(" ")
    print("Search for locker combinations by locker number or student last name.")
    while search_option:
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

def print_combo_by_locker_number(session, locker_number):
    combo = session.query(Locker).filter(Locker.number == locker_number).first()
    if combo:
        print(f'Locker: {combo.number} Combination: {combo.combination}')
    else:
        print("There is no matching locker number in the database.")

def print_combo_by_last_name(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        if len(students) == 1:
            student_combos = (session.query(Locker).join(Student).where(Student.id == Locker.student_id).filter(Student.last_name == last_name).all())
            if student_combos:
                print("The selected student has the following locker(s) assigned: ")
                print(" ")
                for combo in student_combos:
                    print(f'Locker: {combo.number} Combination: {combo.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have any lockers assigned.")
        else:
            options = []
            print("There are multiple students with the last name: {last_name}")
            print(" ")
            for student in students:
                option = (f'{last_name}, {student.first_name}', student.id)
                options.append(option)
            questions = [
                inquirer.List('students',
                              message="Please select the correct student: ",
                              choices=options,
                              ),
                              ]
            answers = inquirer.prompt(questions)
            selection = answers['students']

            student_combos = (session.query(Locker).join(Student).where(Student.id == Locker.student_id).filter(Locker.student_id == selection).all())
            if student_combos:
                print("The selected student has the following locker(s) assigned: ")
                print(" ")
                for combo in student_combos:
                    print(f'Locker: {combo.number} Combination: {combo.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have any lockers assigned.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function1b(session, search_option):
    print(" ")
    print("Search for instrument assignments by student last name.")
    while search_option:
        print(" ")
        record = input("Enter student last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            print_student_instruments(session, last_name=record)

def print_student_instruments(session, last_name):
    students = session.query(Student).filter(Student.last_name == last_name).all()
    if students:
        if len(students) == 1:
            instrument = (session.query(Instrument).filter(Instrument.student_id == student.id).all())
            if instrument:
                print(f"This student has the following instrument(s) assigned: ")
                print(" ")
                instrument_data = ([instrument.type for instrument in instrument])
                print(pandas.DataFrame(instrument_data, columns=["Instrument"]))
            else:
                print(f"Last Name: {last_name} | There are no instruments assigned to a student matching the last name entered.")
        else:
            options = []
            print("There are multiple students with the last name: {last_name}")
            print(" ")
            for student in students:
                option = (f'{last_name}, {student.first_name}', student.id)
                options.append(option)
            questions = [
                inquirer.List('students',
                                message="Please select the correct student: ",
                                choices=options,
                                ),
                                ]
            answers = inquirer.prompt(questions)
            selection = answers['students']
            student_instruments = session.query(Instrument).filter(Instrument.student_id == selection).all()
            if student_instruments:
                print(f"This student has the following instrument(s) assigned: ")
                print(" ")
                instruments = [instrument.type for instrument in student_instruments]
                print(pandas.DataFrame(instruments, columns=["Instrument"]))
            else:
                print(f"Last Name: {last_name} | There are no instruments assigned to a student matching the last name entered.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function1c(session, search_option):
    print(" ")
    print("Search for individual students by student last name.")
    while search_option:
        print(" ")
        record = input("Enter student last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            find_by_last_name(session, last_name=record)

def find_by_last_name(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        student_data = ([(student.last_name, student.first_name, student.grade_level) for student in students])
        print(pandas.DataFrame(student_data, columns=["Last Name", "First Name", "Grade"]))
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")