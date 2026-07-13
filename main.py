students = []

def display_menu():
    print("====Student Grade Manager====")
    print("Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit ")

def get_student_details():
    name = (input("Enter student name: ")).title()
    usn = (input("Enter student usn: ")).upper()
    while True:
        try:
            marks = float(input("Enter student marks: ") )
            if 0<=marks<=100:
                break
            else:
                print("Invalid input: Enter a number from 0 to 100.\n")
        
        except ValueError:
            print("Invalid input: Enter a valid number.\n")

    student = {
        "name": name,
        "usn": usn,
        "marks": marks
    }
    return student

def add(student):
    for existing_student in students:
        if student["usn"] == existing_student["usn"]:
            print(f"Student with usn {existing_student["usn"]} already exists.")
            print("Student was not added.\n")
            return
    students.append(student)
    print("Student added successfully!\n")

def view():
    if len(students) == 0:
            print("No students exist.\n")
            return
    else:
        for index,existing_student in enumerate(students, start=1):
            print(f"Student {index}:")
            print(f"Name: {existing_student['name']}")
            print(f"USN: {existing_student['usn']}")
            print(f"Marks: {existing_student['marks']}")
            print("------------------------------\n")

def search():
    print("Not implemented")

def delete():
    print("Not implemented")

def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
            print()

        except ValueError:
            print("Invalid input: Enter only integers.\n")
            continue

        if choice == 1:
            student = get_student_details()
            add(student)
            
        elif choice == 2:
            view()

        elif choice == 3:
            search()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Bye")
            break
        else:
            print("Invalid choice: Enter integer numbers from 1 to 5.\n")

if __name__ == "__main__":
    main()

