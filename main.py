import json

students = []



def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []



def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent = 4)



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



def show_student_details(existing_student):
    print(f"Name: {existing_student['name']}")
    print(f"USN: {existing_student['usn']}")
    print(f"Marks: {existing_student['marks']}")
    print("------------------------------\n")



def add(student):
    for existing_student in students:
        if student["usn"] == existing_student["usn"]:
            print(f"Student with usn {existing_student['usn']} already exists.")
            print("Student was not added.\n")
            return
    students.append(student)
    save_students()
    print("Student added successfully!\n")



def view():
    if len(students) == 0:
            print("No students exist.\n")
            return
    
    for index,existing_student in enumerate(students, start=1):
        print(f"Student {index}:")
        show_student_details(existing_student)



def search(usn):
    for existing_student in students:
        if usn == existing_student["usn"]:
            print("Student found: \n")
            show_student_details(existing_student)
            return
    print(f"No student with USN: {usn} was found.")



def delete(usn):
    for existing_student in students:
        if usn == existing_student['usn']:
            students.remove(existing_student)
            save_students()
            print("Student successfully deleted!\n")
            return
    print(f"No student with USN: {usn} was found.")



def main():

    global students
    students = load_students()

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
            usn = input("Enter the USN to search: ").upper()
            search(usn)

        elif choice == 4:
            usn = input("Enter the USN of student to be deleted: ").upper()
            delete(usn)

        elif choice == 5:
            print("Bye")
            break

        else:
            print("Invalid choice: Enter integer numbers from 1 to 5.\n")



if __name__ == "__main__":
    main()

