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



def get_marks():
    while True:
        try:
            marks = float(input("Enter new student marks: ") )
            if 0<=marks<=100:
                break
            else:
                print("Invalid input: Enter a number from 0 to 100.\n")
        
        except ValueError:
            print("Invalid input: Enter a valid number.\n")
    return marks



def get_student_details():
    name = (input("Enter new student name: ")).title()
    usn = (input("Enter new student usn: ")).upper()
    marks = get_marks()

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
    input("Press Enter to continue...")



def view(students):
    if len(students) == 0:
            print("No students exist.\n")
            return
    
    for index,existing_student in enumerate(students, start=1):
        print(f"Student {index}:")
        show_student_details(existing_student)
    input("Press Enter to continue...")



def find_student_by_usn(usn):
    for existing_student in students:
        if usn == existing_student["usn"]:
            return existing_student
    return None



def search(usn):
    existing_student = find_student_by_usn(usn)
    if existing_student is None:
        print(f"No student with USN: {usn} was found.")
        return
    print("Student found: \n")
    show_student_details(existing_student)
    input("Press Enter to continue...")



def delete(usn):
    existing_student = find_student_by_usn(usn)
    if existing_student is None:
        print(f"No student with USN: {usn} was found.")
        return
    students.remove(existing_student)
    save_students() 
    print("Student successfully deleted!\n")
    input("Press Enter to continue...")



def update_marks(usn):
    existing_student = find_student_by_usn(usn)
    if existing_student:
        existing_student['marks'] = get_marks()
        save_students()
        print("Student marks updated successfully!\n")
    else:
        print(f"No student with USN: {usn} was found.\n")
    input("Press Enter to continue...")



def statistics():
    total = len(students)

    if total == 0:
        print("No students exist.\n")
        return
    
    sum_marks = 0
    highest = students[0]["marks"]
    lowest = students[0]["marks"]

    for existing_student in students:
        sum_marks += existing_student["marks"]

        if highest < existing_student["marks"]:
            highest = existing_student["marks"]

        if lowest > existing_student["marks"]:
            lowest = existing_student["marks"]
    average = sum_marks/total

    print("====Statistics====")
    print(f"Total Students: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}\n")
    input("Press Enter to continue...")



def sort_menu():
    print("====Sort Students====\n")
    print("1. Sort by Name")
    print("2. Sort by USN")
    print("3. Sort by Marks (Ascending)")
    print("4. Sort by Marks (Descending)")

    try:
        sort_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input: Enter a number.")
        return
    if sort_choice == 1:
        sort_students("name")
    elif sort_choice == 2:
        sort_students("usn")
    elif sort_choice == 3:
        sort_students("marks")
    elif sort_choice == 4:
        sort_students("marks", reverse=True)
    else:
        print("Invalid Input: Enter a number from 1 to 4.")



def sort_students(criteria, reverse = False):
    sorted_students = sorted(students, key=lambda student: student[criteria], reverse=reverse)
    view(sorted_students)
    input("Press Enter to continue...")



def display_menu():
    print("====Student Grade Manager====")
    print("Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student Marks")
    print("6. Show Statistics")
    print("7. Sort Students")
    print("8. Exit ")



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
            view(students)

        elif choice == 3:
            usn = input("Enter the USN to search: ").upper()
            search(usn)

        elif choice == 4:
            usn = input("Enter the USN of student to be deleted: ").upper()
            delete(usn)

        elif choice == 5:
            usn = input("Enter the USN of student to update marks: ").upper()
            update_marks(usn)

        elif choice == 6:
            statistics()

        elif choice == 7:
            sort_menu()

        elif choice == 8:
            print("Bye")
            break

        else:
            print("Invalid choice: Enter integer numbers from 1 to 6.\n")



if __name__ == "__main__":
    main()

