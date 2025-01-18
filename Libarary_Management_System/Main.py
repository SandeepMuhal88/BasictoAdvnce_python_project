import Books_Management_system as bm
import Student_Roll as sr
def main():
    while True:
        print("\n--- ********************************** Welcome to Library Management System ************************************ ---")
        print("Press the number between 1 to 4:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = int(input("Enter your choice:-"))
        if choice == 1:
            book = input("Enter the book name:-")
            bm.Boooks().add_book(book)
        elif choice == 2:
            bm.Boooks().view_books()
        elif choice == 3:
            book = input("Enter the book name:-")
            bm.Boooks().borrow_book(book)
        elif choice == 4:
            book = input("Enter the book name:-")
            bm.Boooks().return_book(book)
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
        print("\n--- ********************************** Welcome to Library Management System ************************************ ---")


if __name__ == "__main__":
    main()