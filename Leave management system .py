import sqlite3

conn = sqlite3.connect("leave_management.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department TEXT,
    leave_balance INTEGER DEFAULT 20
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    leave_type TEXT,
    start_date TEXT,
    end_date TEXT,
    reason TEXT,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY(employee_id) REFERENCES employees(id)
)
""")

conn.commit()


def add_employee():

    print("\n--- ADD EMPLOYEE ---")

    name = input("Name: ")
    email = input("Email: ")
    department = input("Department: ")

    try:
        cursor.execute("""
        INSERT INTO employees
        (name, email, department)
        VALUES (?, ?, ?)
        """, (name, email, department))

        conn.commit()

        print("Employee added successfully.")
        print("Employee ID:", cursor.lastrowid)

    except sqlite3.IntegrityError:
        print("Email already exists.")


def view_employees():

    print("\n--- EMPLOYEE LIST ---")

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
        print("Department:", emp[3])
        print("Leave Balance:", emp[4])


def apply_leave():

    print("\n--- APPLY LEAVE ---")

    employee_id = int(input("Employee ID: "))

    cursor.execute(
        "SELECT leave_balance FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if not employee:
        print("Employee not found.")
        return

    leave_type = input("Leave Type (Casual/Sick/Earned): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    reason = input("Reason: ")

    cursor.execute("""
    INSERT INTO leaves
    (employee_id, leave_type, start_date, end_date, reason)
    VALUES (?, ?, ?, ?, ?)
    """, (
        employee_id,
        leave_type,
        start_date,
        end_date,
        reason
    ))

    conn.commit()

    print("Leave application submitted.")
    print("Status: Pending")


def view_leaves():

    print("\n--- LEAVE REQUESTS ---")

    cursor.execute("""
    SELECT
        leaves.id,
        employees.name,
        leaves.leave_type,
        leaves.start_date,
        leaves.end_date,
        leaves.reason,
        leaves.status
    FROM leaves
    JOIN employees
    ON employees.id = leaves.employee_id
    """)

    leaves = cursor.fetchall()

    if not leaves:
        print("No leave requests.")
        return

    for leave in leaves:

        print("\n" + "-" * 60)

        print("Leave ID :", leave[0])
        print("Employee :", leave[1])
        print("Type     :", leave[2])
        print("Start    :", leave[3])
        print("End      :", leave[4])
        print("Reason   :", leave[5])
        print("Status   :", leave[6])


def approve_leave():

    print("\n--- APPROVE LEAVE ---")

    leave_id = int(input("Leave ID: "))

    cursor.execute("""
    SELECT employee_id, status
    FROM leaves
    WHERE id = ?
    """, (leave_id,))

    leave = cursor.fetchone()

    if not leave:
        print("Leave request not found.")
        return

    if leave[1] != "Pending":
        print("This leave is already processed.")
        return

    cursor.execute("""
    UPDATE leaves
    SET status = 'Approved'
    WHERE id = ?
    """, (leave_id,))

    cursor.execute("""
    UPDATE employees
    SET leave_balance = leave_balance - 1
    WHERE id = ?
    """, (leave[0],))

    conn.commit()

    print("Leave approved.")


def reject_leave():

    print("\n--- REJECT LEAVE ---")

    leave_id = int(input("Leave ID: "))

    cursor.execute("""
    UPDATE leaves
    SET status = 'Rejected'
    WHERE id = ?
    AND status = 'Pending'
    """, (leave_id,))

    conn.commit()

    if cursor.rowcount:
        print("Leave rejected.")
    else:
        print("Leave request not found or already processed.")


def search_employee():

    print("\n--- SEARCH EMPLOYEE ---")

    keyword = input("Enter name or department: ")

    cursor.execute("""
    SELECT * FROM employees
    WHERE name LIKE ?
    OR department LIKE ?
    """, (
        "%" + keyword + "%",
        "%" + keyword + "%"
    ))

    employees = cursor.fetchall()

    for emp in employees:
        print("-" * 40)
        print("ID:", emp[0])
        print("Name:", emp[1])
        print("Department:", emp[3])
        print("Leave Balance:", emp[4])


def leave_report():

    print("\n--- LEAVE REPORT ---")

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM leaves
    GROUP BY status
    """)

    report = cursor.fetchall()

    for status, count in report:
        print(status, ":", count)


def main():

    while True:

        print("\n" + "=" * 50)
        print("       LEAVE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Apply Leave")
        print("4. View Leave Requests")
        print("5. Approve Leave")
        print("6. Reject Leave")
        print("7. Search Employee")
        print("8. Leave Report")
        print("9. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            apply_leave()

        elif choice == "4":
            view_leaves()

        elif choice == "5":
            approve_leave()

        elif choice == "6":
            reject_leave()

        elif choice == "7":
            search_employee()

        elif choice == "8":
            leave_report()

        elif choice == "9":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()

conn.close()
print("Database connection closed.")