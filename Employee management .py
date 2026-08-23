import sqlite3

conn = sqlite3.connect("corporate_management.db")
cursor = conn.cursor()

# Create Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    department TEXT,
    designation TEXT,
    salary REAL
)
""")

# Create Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY(employee_id) REFERENCES employees(id)
)
""")

conn.commit()


def add_employee():
    print("\n--- Add Employee ---")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    try:
        cursor.execute("""
        INSERT INTO employees
        (name, email, phone, department, designation, salary)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, phone, department, designation, salary))

        conn.commit()
        print("Employee added successfully.")

    except sqlite3.IntegrityError:
        print("Email already exists.")


def view_employees():
    print("\n--- Employee List ---")

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
        return

    for emp in employees:
        print("-" * 50)
        print("ID:", emp[0])
        print("Name:", emp[1])
        print("Email:", emp[2])
        print("Phone:", emp[3])
        print("Department:", emp[4])
        print("Designation:", emp[5])
        print("Salary:", emp[6])


def search_employee():
    print("\n--- Search Employee ---")

    keyword = input("Enter employee name or department: ")

    cursor.execute("""
    SELECT * FROM employees
    WHERE name LIKE ? OR department LIKE ?
    """, ('%' + keyword + '%', '%' + keyword + '%'))

    employees = cursor.fetchall()

    if not employees:
        print("Employee not found.")
        return

    for emp in employees:
        print("-" * 40)
        print("ID:", emp[0])
        print("Name:", emp[1])
        print("Department:", emp[4])
        print("Designation:", emp[5])
        print("Salary:", emp[6])


def update_employee():
    print("\n--- Update Employee ---")

    employee_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if not employee:
        print("Employee not found.")
        return

    name = input("Enter New Name: ")
    phone = input("Enter New Phone: ")
    department = input("Enter New Department: ")
    designation = input("Enter New Designation: ")
    salary = float(input("Enter New Salary: "))

    cursor.execute("""
    UPDATE employees
    SET name = ?,
        phone = ?,
        department = ?,
        designation = ?,
        salary = ?
    WHERE id = ?
    """, (
        name,
        phone,
        department,
        designation,
        salary,
        employee_id
    ))

    conn.commit()

    print("Employee updated successfully.")


def delete_employee():
    print("\n--- Delete Employee ---")

    employee_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT name FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if not employee:
        print("Employee not found.")
        return

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    conn.commit()

    print("Employee deleted successfully.")


def mark_attendance():
    print("\n--- Mark Attendance ---")

    employee_id = int(input("Enter Employee ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")

    cursor.execute("""
    INSERT INTO attendance
    (employee_id, date, status)
    VALUES (?, ?, ?)
    """, (employee_id, date, status))

    conn.commit()

    print("Attendance recorded successfully.")


def view_attendance():
    print("\n--- Attendance Report ---")

    cursor.execute("""
    SELECT
        employees.name,
        attendance.date,
        attendance.status
    FROM attendance
    JOIN employees
    ON employees.id = attendance.employee_id
    """)

    records = cursor.fetchall()

    if not records:
        print("No attendance records found.")
        return

    for record in records:
        print(
            "Employee:",
            record[0],
            "| Date:",
            record[1],
            "| Status:",
            record[2]
        )


def department_report():
    print("\n--- Department Report ---")

    cursor.execute("""
    SELECT department, COUNT(*)
    FROM employees
    GROUP BY department
    """)

    departments = cursor.fetchall()

    for department, count in departments:
        print(department, ":", count, "employees")


def salary_report():
    print("\n--- Salary Report ---")

    cursor.execute("""
    SELECT
        COUNT(*),
        SUM(salary),
        AVG(salary),
        MAX(salary),
        MIN(salary)
    FROM employees
    """)

    result = cursor.fetchone()

    print("Total Employees:", result[0])
    print("Total Salary:", result[1])
    print("Average Salary:", result[2])
    print("Highest Salary:", result[3])
    print("Lowest Salary:", result[4])


def main():
    while True:

        print("\n")
        print("=" * 55)
        print(" CORPORATE EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Mark Attendance")
        print("7. View Attendance")
        print("8. Department Report")
        print("9. Salary Report")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            mark_attendance()

        elif choice == "7":
            view_attendance()

        elif choice == "8":
            department_report()

        elif choice == "9":
            salary_report()

        elif choice == "10":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()

conn.close()