import sqlite3

DATABASE = "student.db"


def connect():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks INTEGER
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, age, course, marks):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course, marks) VALUES (?, ?, ?, ?)",
        (name, age, course, marks)
    )

    conn.commit()
    conn.close()


def fetch_students():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_student(student_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()


def update_student(student_id, name, age, course, marks):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?,
            age=?,
            course=?,
            marks=?
        WHERE id=?
    """, (name, age, course, marks, student_id))

    conn.commit()
    conn.close()


def search_student(keyword):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE name LIKE ?
           OR course LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()

    conn.close()

    return rows


connect()