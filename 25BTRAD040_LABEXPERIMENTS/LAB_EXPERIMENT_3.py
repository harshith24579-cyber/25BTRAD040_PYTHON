# LAB EXPERIMENT - 3
# NAME: HARSHITH
# USN: 25BTRAD040
# BRANCH: AIDE-A
# DATE: 28.10.26


# Lab Exercise 8: Contact Book Using Lists and Dictionaries
contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found!")


def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
            return

    print("Contact not found!")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")


def display_contacts():
    if not contacts:
        print("No contacts available!")
    else:
        for contact in contacts:
            print(contact)


def contact_book():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice!")


# Lab Exercise 9: Student Grading System
def student_grading_system():
    students = {}

    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("\nEnter student name: ")
        marks = float(input("Enter marks out of 100: "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            continue

        students[name] = marks

    print("\n--- STUDENT RESULTS ---")
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print("Name:", name)
        print("Marks:", marks)
        print("Grade:", grade)
        print("------------------")


# Lab Exercise 10: Frequency Counter Using Dictionaries
def frequency_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\n--- WORD FREQUENCY ---")
    for word, count in frequency.items():
        print(word, ":", count)


# Main Menu
def main():
    while True:
        print("\n===== LAB EXPERIMENT 3 =====")
        print("1. Contact Book")
        print("2. Student Grading System")
        print("3. Frequency Counter")
        print("4. Exit")

        choice = input("Select an exercise: ")

        if choice == "1":
            contact_book()
        elif choice == "2":
            student_grading_system()
        elif choice == "3":
            frequency_counter()
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
