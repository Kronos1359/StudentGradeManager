

def main():
    while True:
        choice = int(input("===Student Grade Manager===\nEnter your choice:\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit "))

        if choice == 1:
            add()
            print("Not implemented")
        elif choice == 2:
            view()
            print("Not implemented")
        elif choice == 3:
            search()
            print("Not implemented")
        elif choice == 4:
            delete()
            print("Not implemented")
        elif choice == 5:
            print("Bye")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

