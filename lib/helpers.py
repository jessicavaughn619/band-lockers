import pandas
import inquirer
from db.models import Locker, Student, Instrument

# Locker methods
    
def add_locker(session, locker):
    session.add(locker)
    session.commit()

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
            student_combo = (session.query(Locker).filter(Locker.student_id == students.id).all())
            if student_combo:
                for combo in student_combo:
                    print(f'Last Name: {last_name} Locker: {combo.number} Combination: {combo.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have a locker assigned.")
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
            student_combo = session.query(Locker).filter(Locker.student_id == selection).first()
            if student_combo:
                print(f'Last Name: {last_name} Locker: {student_combo.number} Combination: {student_combo.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have a locker assigned.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

# Assign locker method needs work - need to identify specific locker to update

def assign_locker(session, id, student_id):
    session.query(Locker).filter(Locker.id == id).update({
        Locker.student_id: student_id
        })

# Instrument methods

def add_instrument(session, instrument):
    session.add(instrument)
    session.commit()

def count_instruments(session, instrument):
    instrument_count = session.query(Instrument).filter(Instrument.type.like(instrument)).count()
    if instrument_count > 0:
        print(f"There are {instrument_count} {instrument}(s) currently assigned to students.")
    if instrument_count == 0:
        print("None of this instrument type are currently assigned to students.")

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

# Student methods
#  
def add_student(session, student):
    session.add(student)
    session.commit()

# def delete_seniors(session):
#     seniors = session.query(Student).filter(Student.grade_level == 12)
#     session.delete(seniors)
#     session.commit()

# def increase_grade_level(session):
#     session.query(Student).update({Student.grade_level: Student.grade_level + 1})
#     print("Increased all student grade levels by one year.")

def print_students_by_grade(session, grade):
    students = (session.query(Student).filter(Student.grade_level == grade)).all()
    student_data = ([(student.first_name, student.last_name) for student in students])
    print(pandas.DataFrame(student_data, columns=["First Name", "Last Name"]))

def count_students_by_grade(session, grade):
    grade_count = (session.query(Student).filter(Student.grade_level == grade).count())
    print(f"There are {grade_count} student(s) in grade {grade}.")

def find_by_last_name(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        student_data = ([(student.last_name, student.first_name, student.grade_level) for student in students])
        print(pandas.DataFrame(student_data, columns=["Last Name", "First Name", "Grade"]))
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")