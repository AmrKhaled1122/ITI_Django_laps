from db import get_connection
from user_service import UserService
from book_service import BookService
from borrow_service import BorrowService

conn = get_connection()
user_service = UserService(conn)
book_service = BookService(conn)
borrow_service = BorrowService(conn)

print("Welcome to Mini Library")
print("1. Login")
print("2. Register")
choice = input("Choose option: ")

username = input("Username: ")
password = input("Password: ")

if choice == '2':
    role = input("Role (admin/user): ").strip().lower()
    if role not in ['admin', 'user']:
        print("Invalid role. Defaulting to 'user'.")
        role = 'user'
    user_service.register_user(username, password, role)
    print("Registration complete. Please login again.")
    exit()

user = user_service.authenticate(username, password)
if not user:
    print("Login failed.")
    exit()

print(f"Login successful as {user['role'].upper()}")

if user['role'] == 'admin':
    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_service.add_book(title, author)

        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            book_service.remove_book(book_id)

        elif choice == '3':
            books = book_service.get_all_books()
            print("\nAll Books:")
            for b in books:
                print(f"ID: {b[0]} | Title: {b[1]} | Author: {b[2]}")

        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

elif user['role'] == 'user':
    while True:
        print("\n1. Borrow Book")
        print("2. Return Book")
        print("3. View My Borrowed Books")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            book_id = input("Enter book ID to borrow: ")
            borrow_service.borrow_book(user['id'], book_id)

        elif choice == '2':
            book_id = input("Enter book ID to return: ")
            borrow_service.return_book(user['id'], book_id)

        elif choice == '3':
            borrowed_books = borrow_service.get_user_borrowed_books(user['id'])
            print("\nYour Borrowed Books:")
            if borrowed_books:
                for b in borrowed_books:
                    print(f"ID: {b[0]} | Title: {b[1]} | Author: {b[2]}")
            else:
                print("You haven't borrowed any books.")

        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
