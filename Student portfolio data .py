import csv
import os

FILE_NAME = "students.csv"


# Create file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course", "Marks"])


# Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course, marks])

    print("\nStudent Added Successfully!\n")


# View Students
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n------------------------------")
        for row in reader:
            print("{:<8} {:<15} {:<8} {:<15} {}".format(*row))
        print("------------------------------\n")


# Search Student
def search_student():
    sid = input("Enter Student ID: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == sid:
                print("\nStudent Found")
                print(row)
                found = True
                break

    if not found:
        print("Student Not Found")


# Update Student
def update_student():
    sid = input("Enter Student ID to Update: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == sid:
                found = True
                row["Name"] = input("New Name: ")
                row["Age"] = input("New Age: ")
                row["Course"] = input("New Course: ")
                row["Marks"] = input("New Marks: ")

            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Age", "Course", "Marks"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

        print("Student Updated Successfully")

    else:
        print("Student Not Found")


# Delete Student
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] != sid:
                rows.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Age", "Course", "Marks"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

        print("Student Deleted Successfully")

    else:
        print("Student Not Found")


# Average Marks
def average_marks():
    total = 0
    count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += int(row["Marks"])
            count += 1

    if count:
        print("Average Marks:", total / count)
    else:
        print("No Student Records")


# Top Scorer
def top_scorer():
    top = None

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if top is None or int(row["Marks"]) > int(top["Marks"]):
                top = row

    if top:
        print("\nTop Scorer")
        print(top)
    else:
        print("No Student Records")


# Menu
def menu():
    create_file()

    while True:
        print("""
========= Student Management System =========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Average Marks
7. Top Scorer
8. Exit

============================================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            average_marks()

        elif choice == "7":
            top_scorer()

        elif choice == "8":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


menu()