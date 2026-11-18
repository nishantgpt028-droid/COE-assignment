#Library Management System
import json
from datetime import date

#For Loading and Saving Data from JSON Files
def load_data(file_name):
    try:
        file = open(file_name, "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return []


def save_data(file_name, data):
    file = open(file_name, "w")
    json.dump(data, file, indent=4)
    file.close()


books = load_data("books.json")
students = load_data("students.json")
issued_books = load_data("issued_books.json")


# 1.Add book
def add_book():
    bid = input("Enter book ID: ")

    for b in books:
        if b["book_id"].lower() == bid.lower():
            print("Book ID already exists!")
            return

    name = input("Enter book name: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")
    copies = int(input("Enter number of copies: "))

    if copies <= 0:
        print("Enter a valid number of copies!")
        return

    b = {
        "book_id": bid,
        "book_name": name,
        "author": author,
        "category": category,
        "available_copies": copies
    }

    books.append(b)
    save_data("books.json", books)
    print("Book added successfully!")


# 2.Show all books
def display_books():
    if len(books) == 0:
        print("No books available!")
    else:
        for b in books:
            print("\nBook ID:", b["book_id"])
            print("Book Name:", b["book_name"])
            print("Author:", b["author"])
            print("Category:", b["category"])
            print("Available Copies:", b["available_copies"])


# 3.Search book
def search_book():
    s = input("Enter book ID, name or author: ").lower()
    found = 0

    for b in books:
        if (s == b["book_id"].lower() or
            s in b["book_name"].lower() or
            s in b["author"].lower()):

            print("\nBook Found")
            print("Book ID:", b["book_id"])
            print("Book Name:", b["book_name"])
            print("Author:", b["author"])
            print("Category:", b["category"])
            print("Available Copies:", b["available_copies"])
            found = 1

    if found == 0:
        print("Book not found!")


# 4.Register student
def register_student():
    sid = input("Enter student ID: ")

    for s in students:
        if s["student_id"].lower() == sid.lower():
            print("Student already registered!")
            return

    name = input("Enter student name: ")
    dept = input("Enter department: ")
    contact = input("Enter contact number: ")

    s = {
        "student_id": sid,
        "name": name,
        "department": dept,
        "contact": contact
    }

    students.append(s)
    save_data("students.json", students)
    print("Student registered successfully!")


# 5.Issue book
def issue_book():
    sid = input("Enter student ID: ")
    bid = input("Enter book ID: ")

    student_found = False
    book_found = False

    for s in students:
        if s["student_id"].lower() == sid.lower():
            student_found = True
            break

    for b in books:
        if b["book_id"].lower() == bid.lower():
            book_found = True
            selected = b
            break

    if student_found == False:
        print("Student not registered!")
        return

    if book_found == False:
        print("Book not found!")
        return

    if selected["available_copies"] == 0:
        print("No copies available!")
        return

    selected["available_copies"] -= 1

    record = {
        "student_id": sid,
        "book_id": selected["book_id"],
        "issue_date": str(date.today())
    }

    issued_books.append(record)

    save_data("books.json", books)
    save_data("issued_books.json", issued_books)

    print("Book issued successfully!")


# 6.Return book
def return_book():
    sid = input("Enter student ID: ")
    bid = input("Enter book ID: ")

    for r in issued_books:
        if (r["student_id"].lower() == sid.lower() and
            r["book_id"].lower() == bid.lower()):

            for b in books:
                if b["book_id"].lower() == bid.lower():
                    b["available_copies"] += 1
                    break

            issued_books.remove(r)

            save_data("books.json", books)
            save_data("issued_books.json", issued_books)

            print("Book returned successfully!")
            return

    print("Issue record not found!")


# 7.Show issued books
def display_issued_books():
    if len(issued_books) == 0:
        print("No books are currently issued!")
    else:
        for r in issued_books:
            print("\nStudent ID:", r["student_id"])
            print("Book ID:", r["book_id"])
            print("Issue Date:", r["issue_date"])


# 8.Delete book
def delete_book():
    book_id = input("Enter book ID to delete: ")

    for r in issued_books:
        if r["book_id"].lower() == book_id.lower():
            print("Book is currently issued. Cannot delete!")
            return

    for b in books:
        if b["book_id"].lower() == book_id.lower():
            books.remove(b)
            save_data("books.json", books)
            print("Book deleted successfully!")
            return

    print("Book not found!")


# Main program
def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Search for a Book")
        print("4. Register a Student")
        print("5. Issue a Book")
        print("6. Return a Book")
        print("7. Display Issued Books")
        print("8. Delete a Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            register_student()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            display_issued_books()
        elif choice == "8":
            delete_book()
        elif choice == "9":
            print("Program closed!")
            break
        else:
            print("Invalid choice!")


main()
