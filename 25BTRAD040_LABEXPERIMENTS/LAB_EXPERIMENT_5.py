# LAB EXPERIMENT – 5
# NAME: HARSHITH
# USN: 25BTRAD040
# BRANCH: CSE – AIDE A

import random


# Lab Exercise 14: Bank Account System Using OOP
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: Rs.", self.balance)


def bank_account_system():
    account = BankAccount("Arya", 5000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using the bank system.")
            break
        else:
            print("Invalid choice.")


# Lab Exercise 15: Library Management System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


def library_management_system():
    library = Library()
    library.add_book(Book("Python Basics", "John"))
    library.add_book(Book("Java Programming", "James"))

    while True:
        print("\n1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter book title: ")
            library.issue_book(title)
        elif choice == "3":
            title = input("Enter book title: ")
            library.return_book(title)
        elif choice == "4":
            print("Exiting library system.")
            break
        else:
            print("Invalid choice.")


# Lab Exercise 16: Dice Simulator Using random Module
def dice_simulator():
    while True:
        print("\n1. Roll One Die")
        print("2. Roll Two Dice")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            result = random.randint(1, 6)
            print("Dice result:", result)
        elif choice == "2":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print("First die:", die1)
            print("Second die:", die2)
            print("Total:", die1 + die2)
        elif choice == "3":
            print("Dice simulation ended.")
            break
        else:
            print("Invalid choice.")


# Main menu
def main():
    while True:
        print("\n===== LAB EXPERIMENT 5 =====")
        print("1. Bank Account System")
        print("2. Library Management System")
        print("3. Dice Simulator")
        print("4. Exit")
        choice = input("Select an exercise: ")

        if choice == "1":
            bank_account_system()
        elif choice == "2":
            library_management_system()
        elif choice == "3":
            dice_simulator()
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
