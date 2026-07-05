def display_menu():
    print("====Student Grade Manager====")
    print("Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit ")

def add():
    print("Not implemented")

def view():
    print("Not implemented")

def search():
    print("Not implemented")

def delete():
    print("Not implemented")

def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice:"))
            
        except ValueError:
            print("Pls enter only integer values.")
            continue

        if choice == 1:
            add()
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
            print("Invalid choice: Pls enter integer numbers from 1 to 5.")

if __name__ == "__main__":
    main()

