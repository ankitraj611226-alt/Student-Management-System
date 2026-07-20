"""
=========================================================
              Student Management System
---------------------------------------------------------
Author      : Ankit Raj
Language    : Python
Description : A simple command-line Student Management
              System using File Handling.

Features:
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Data stored in students.txt
=========================================================
"""

import os

FILE_NAME = "students.txt"


def add_student():
    """Add a new student record."""

    print("\n----- Add Student -----")

    name = input("Enter Student Name : ").strip()
    age = input("Enter Age          : ").strip()
    course = input("Enter Course       : ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("\n✅ Student Added Successfully!\n")


def view_students():
    """Display all student records."""

    if not os.path.exists(FILE_NAME):
        print("\n❌ No student records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("\n❌ No student records found.\n")
        return

    print("\n========== Student Records ==========")

    for index, line in enumerate(students, start=1):
        name, age, course = line.strip().split(",")

        print(f"\nStudent {index}")
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Age    : {age}")
        print(f"Course : {course}")

    print("\n=====================================\n")


def search_student():
    """Search a student by name."""

    if not os.path.exists(FILE_NAME):
        print("\n❌ No student records found.\n")
        return

    search_name = input("\nEnter Student Name to Search: ").strip()

    found = False

    with open(FILE_NAME, "r") as file:

        for line in file:
            name, age, course = line.strip().split(",")

            if name.lower() == search_name.lower():

                print("\n✅ Student Found")
                print("-" * 30)
                print(f"Name   : {name}")
                print(f"Age    : {age}")
                print(f"Course : {course}")

                found = True
                break

    if not found:
        print("\n❌ Student Not Found.\n")


def delete_student():
    """Delete a student record."""

    if not os.path.exists(FILE_NAME):
        print("\n❌ No student records found.\n")
        return

    delete_name = input("\nEnter Student Name to Delete: ").strip()

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    deleted = False

    with open(FILE_NAME, "w") as file:

        for line in students:

            name, age, course = line.strip().split(",")

            if name.lower() != delete_name.lower():
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("\n✅ Student Deleted Successfully!\n")
    else:
        print("\n❌ Student Not Found.\n")


def main():
    """Main menu."""

    while True:

        print("=" * 42)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 42)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print("=" * 42)

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("\nThank You for Using Student Management System ❤️")
            break

        else:
            print("\n❌ Invalid Choice! Please Try Again.\n")


if __name__ == "__main__":
    main()