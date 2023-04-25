from db.models import Student, Instrument
import inquirer

def function5a(session, search_option):
    print(" ")
    print("Delete individual student from database.")
    while search_option:
        print(" ")
        last_name = input("Enter student last name: ")
        if last_name == "Q":
            break
        else:
            delete_student_record(session, last_name)

def delete_student_record(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    while students:
        options = []
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
        confirm = input(f"Confirm delete student record? n/Y: ")
        if confirm == "Y":
            print(" ")
            confirm_confirm = input("WARNING: Selecting Y will delete this student from the database. Press n/Y to confirm: ")
            if confirm_confirm == "Y":
                session.query(Student).filter(Student.id == selection).delete()
                session.commit()
                print(" ")
                print("Student record successfully deleted!")
            elif confirm_confirm == "Q":
                break
            else:
                print(" ")
                print("Student record NOT deleted.")
        elif confirm == "Q":
            break
        else:
            print(" ")
            print("Student record NOT deleted.")
    else:
        print(" ")
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function5b(session, search_option):
    print(" ")
    print("Delete individual instrument from database.")
    while search_option:
        print(" ")
        instrument_id = input("Enter instrument ID: ")
        if instrument_id == "Q":
            break
        else:
            delete_instrument_record(session, instrument_id)

def delete_instrument_record(session, id):
    instrument = session.query(Instrument).filter(Instrument.id == id).first()
    while instrument:
        print(" ")
        confirm = input(f"Confirm delete the following instrument: Id: {id} Instrument: {instrument.type}? n/Y: ")
        if confirm == "Y":
            print(" ")
            confirm_confirm = input("WARNING: Selecting Y will delete this entry from the database. Press n/Y to confirm: ")
            if confirm_confirm == "Y":
                session.delete(instrument)
                session.commit()
                print(" ")
                print("Instrument record successfully deleted.")
            elif confirm_confirm == "Q":
                break
            else:
                print(" ")
                print("Instrument record NOT deleted.")
        elif confirm == "Q":
            break
        else:
            print(" ")
            print("Instrument record NOT deleted.")

def function5c(session, search_option):
    print(" ")
    print("Delete students by grade level.")
    while search_option:
        print(" ")
        grade = input("Enter grade level to delete: ")
        if grade == "Q":
            break
        else:
            delete_students_by_grade(session, grade)

def delete_students_by_grade(session, grade):
    print(" ")
    students = session.query(Student).filter(Student.grade_level == grade).all()
    while students:
        confirm = input(f"Confirm delete all students with grade {grade}? n/Y: ")
        if confirm == "Y":
            print(" ")
            confirm_confirm = input(f"WARNING: Selecting Y will delete ALL student records with grade level {grade}. Press n/Y to confirm: ")
            if confirm_confirm == "Y":
                for student in students:
                    session.delete(student)
                    session.commit()
                print(" ")
                print(f"Successfully deleted all student records with grade level {grade}.")
            elif confirm_confirm == "Q":
                break
            else:
                print(" ")
                print("Student records NOT deleted.") 
        elif confirm == "Q":
            break
        else:
            print(" ")
            print("Student records NOT deleted.")
    else:
        print(f"No student records found with grade level {grade}.")
