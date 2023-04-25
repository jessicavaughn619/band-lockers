from db.models import Student, Instrument

def function3a(session, search_option):
    print(" ")
    print("Add new student to database.")
    while search_option:
        print(" ")
        first_name = input("Enter student first name: ")
        if first_name == "Q":
            break
        else:
            last_name = input("Enter student last name: ")
            grade_level = input("Enter student grade level: ")
            print(" ")
            print(f"First Name: {first_name} | Last Name: {last_name} | Grade Level: {grade_level}")
            print(" ")
            confirm = input("Confirm add above student to database? n/Y: ")
            if confirm == "n":
                print(" ")
                print("Student NOT added to database.")
            elif confirm == "Y":
                add_student(session, Student(first_name=first_name, last_name=last_name, grade_level=grade_level))
                print(" ")
                print("New student successfully added to database!")
            elif confirm == "Q":
                break
            else:
                print (" ")
                print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

def add_student(session, student):
    session.add(student)
    session.commit()

def function3b(session, search_option):
    print(" ")
    print("Add new instrument to database.")
    while search_option:
        print(" ")
        type = input("Enter instrument type: ")
        if type == "Q":
            break
        else:
            print(" ")
            print(f"Type: {type}")
            print(" ")
            confirm = input("Confirm add above instrument to database? n/Y: ")
            if confirm == "n":
                print(" ")
                print("Instrument NOT added to database.")
            elif confirm == "Y":
                add_instrument(session, Instrument(type=type))
                print(" ")
                print("New instrument successfully added to database!")
            elif confirm == "Q":
                break
            else:
                print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

def add_instrument(session, instrument):
    session.add(instrument)
    session.commit()