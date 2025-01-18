import os
class Boooks:
    def __init__(self):
        self.book_list = []
        self.book_borrow_status = {}
        self.load_book_list()
        self.load_book_status()
        
    def load_book_list(self):
        if os.path.exists("books.txt"):
            with open("books.txt", "r") as file:
                self.book_list = file.read().splitlines()
        
    def save_book_list(self):
        with open("books.txt", "w") as file:
            file.write("\n".join(self.book_list))
    
    def save_book_status(self):
        with open("book_status.txt", "w") as file:
            for book, status in self.book_borrow_status.items():
                file.write(f"{book},{status}\n")
    
    def load_book_status(self):
        if os.path.exists("book_status.txt"):
            with open("book_status.txt", "r") as file:
                for line in file:
                    book, status = line.strip().split(",")
                    self.book_borrow_status[book] = status
        
    def add_book(self, book):
        self.book_list.append(book)
        self.save_book_list()
        print(f"Book '{book}' added successfully!")
        self.book_borrow_status[book] = "Available"
        self.save_book_status()
    
    def view_books(self):
        if not self.book_list:
            print("No books available!")
        else:
            print("\n--- Available Books ---")
            for book in self.book_list:
                print(f"- {book}")
            print("\n--- Book Borrow Status ---")
            for book, status in self.book_borrow_status.items():
                print(f"- {book}: {status}")

    def borrow_book(self, book):
        if book in self.book_list and self.book_borrow_status[book] == "Available":
            self.book_borrow_status[book] = "Borrowed"
            self.save_book_status()
            print(f"Book '{book}' borrowed successfully!")
        else:
            print(f"Book '{book}' is not available or already borrowed!")
        
    def return_book(self, book):
        if book in self.book_list and self.book_borrow_status[book] == "Borrowed":
            self.book_borrow_status[book] = "Available"
            self.save_book_status()
            print(f"Book '{book}' returned successfully!")
        else:
            print(f"Book '{book}' is not borrowed or does not exist!")