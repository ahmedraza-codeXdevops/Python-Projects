import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- Database ----------------

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
course TEXT,
marks INTEGER
)
""")

conn.commit()

# ---------------- Functions ----------------

def show_data():
    tree.delete(*tree.get_children())

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def add_student():

    if name_var.get() == "":
        messagebox.showerror("Error", "Enter Name")
        return

    cursor.execute(
        "INSERT INTO students(name,age,course,marks) VALUES(?,?,?,?)",
        (
            name_var.get(),
            age_var.get(),
            course_var.get(),
            marks_var.get()
        )
    )

    conn.commit()

    clear()

    show_data()


def delete_student():

    selected = tree.focus()

    if selected == "":
        return

    values = tree.item(selected)["values"]

    cursor.execute("DELETE FROM students WHERE id=?", (values[0],))

    conn.commit()

    show_data()


def select_item(event):

    selected = tree.focus()

    values = tree.item(selected)["values"]

    if values:

        id_var.set(values[0])
        name_var.set(values[1])
        age_var.set(values[2])
        course_var.set(values[3])
        marks_var.set(values[4])


def update_student():

    cursor.execute("""
    UPDATE students
    SET
    name=?,
    age=?,
    course=?,
    marks=?
    WHERE id=?
    """,

    (
        name_var.get(),
        age_var.get(),
        course_var.get(),
        marks_var.get(),
        id_var.get()
    ))

    conn.commit()

    show_data()

    clear()


def search_student():

    tree.delete(*tree.get_children())

    cursor.execute("""
    SELECT * FROM students
    WHERE name LIKE ?
    """,

    ('%' + search_var.get() + '%',))

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def clear():

    id_var.set("")
    name_var.set("")
    age_var.set("")
    course_var.set("")
    marks_var.set("")


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Student Management System")

root.geometry("900x550")

id_var = tk.StringVar()
name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()
marks_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(root, text="Name").place(x=20, y=20)
tk.Entry(root, textvariable=name_var).place(x=120, y=20)

tk.Label(root, text="Age").place(x=20, y=60)
tk.Entry(root, textvariable=age_var).place(x=120, y=60)

tk.Label(root, text="Course").place(x=20, y=100)
tk.Entry(root, textvariable=course_var).place(x=120, y=100)

tk.Label(root, text="Marks").place(x=20, y=140)
tk.Entry(root, textvariable=marks_var).place(x=120, y=140)

tk.Button(root, text="Add", width=12, command=add_student).place(x=20, y=190)

tk.Button(root, text="Update", width=12, command=update_student).place(x=140, y=190)

tk.Button(root, text="Delete", width=12, command=delete_student).place(x=260, y=190)

tk.Button(root, text="Clear", width=12, command=clear).place(x=380, y=190)

tk.Label(root, text="Search").place(x=20, y=250)

tk.Entry(root, textvariable=search_var).place(x=120, y=250)

tk.Button(root, text="Search", command=search_student).place(x=280, y=245)

tk.Button(root, text="Show All", command=show_data).place(x=360, y=245)

columns = ("ID", "Name", "Age", "Course", "Marks")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140)

tree.place(x=20, y=300)

tree.bind("<ButtonRelease-1>", select_item)

show_data()

root.mainloop()

conn.close()