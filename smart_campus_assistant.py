import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from datetime import datetime


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CampusDatabase:

    def __init__(self):
        self.connection = sqlite3.connect("campus.db")
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.insert_data()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                date TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                date TEXT,
                venue TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS internships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                skills TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS faculty (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                department TEXT,
                subject TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS timetable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                day TEXT,
                subject TEXT,
                time TEXT,
                room TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scholarships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                eligibility TEXT,
                deadline TEXT
            )
        """)

        self.connection.commit()

    def insert_data(self):

        self.cursor.execute("SELECT COUNT(*) FROM notices")

        if self.cursor.fetchone()[0] == 0:

            notices = [
                (
                    "Python Workshop",
                    "Python programming workshop for students.",
                    "28-08-2026"
                ),
                (
                    "Project Submission",
                    "Submit your major project synopsis.",
                    "30-08-2026"
                ),
                (
                    "Placement Training",
                    "Placement aptitude training session.",
                    "02-09-2026"
                )
            ]

            self.cursor.executemany("""
                INSERT INTO notices
                (title, description, date)
                VALUES (?, ?, ?)
            """, notices)

        self.cursor.execute("SELECT COUNT(*) FROM events")

        if self.cursor.fetchone()[0] == 0:

            events = [
                (
                    "Hackathon 2026",
                    "05-09-2026",
                    "Computer Lab"
                ),
                (
                    "Tech Fest",
                    "12-09-2026",
                    "College Auditorium"
                ),
                (
                    "Career Guidance Seminar",
                    "18-09-2026",
                    "Seminar Hall"
                )
            ]

            self.cursor.executemany("""
                INSERT INTO events
                (name, date, venue)
                VALUES (?, ?, ?)
            """, events)

        self.cursor.execute("SELECT COUNT(*) FROM internships")

        if self.cursor.fetchone()[0] == 0:

            internships = [
                (
                    "Python Developer Intern",
                    "Tech Solutions",
                    "Python, SQL, Git"
                ),
                (
                    "Data Analyst Intern",
                    "DataWorks",
                    "Python, Excel, Power BI"
                ),
                (
                    "AI/ML Intern",
                    "AI Labs",
                    "Python, Machine Learning"
                )
            ]

            self.cursor.executemany("""
                INSERT INTO internships
                (title, company, skills)
                VALUES (?, ?, ?)
            """, internships)

        self.cursor.execute("SELECT COUNT(*) FROM faculty")

        if self.cursor.fetchone()[0] == 0:

            faculty = [
                (
                    "Dr. Sharma",
                    "Computer Science",
                    "Python"
                ),
                (
                    "Prof. Khan",
                    "Computer Science",
                    "Database Management"
                ),
                (
                    "Prof. Patel",
                    "IT",
                    "Web Development"
                )
            ]

            self.cursor.executemany("""
                INSERT INTO faculty
                (name, department, subject)
                VALUES (?, ?, ?)
            """, faculty)

        self.cursor.execute("SELECT COUNT(*) FROM timetable")

        if self.cursor.fetchone()[0] == 0:

            timetable = [
                ("Monday", "Python", "09:00 AM", "Lab 1"),
                ("Monday", "DBMS", "11:00 AM", "Room 204"),
                ("Tuesday", "Web Development", "09:00 AM", "Lab 2"),
                ("Tuesday", "DSA", "11:00 AM", "Room 205"),
                ("Wednesday", "Python", "10:00 AM", "Lab 1"),
                ("Thursday", "DBMS", "09:00 AM", "Room 204"),
                ("Friday", "Project", "11:00 AM", "Project Lab")
            ]

            self.cursor.executemany("""
                INSERT INTO timetable
                (day, subject, time, room)
                VALUES (?, ?, ?, ?)
            """, timetable)

        self.cursor.execute("SELECT COUNT(*) FROM scholarships")

        if self.cursor.fetchone()[0] == 0:

            scholarships = [
                (
                    "Merit Scholarship",
                    "Students with strong academic performance",
                    "30-09-2026"
                ),
                (
                    "Technology Scholarship",
                    "Students pursuing technology-related courses",
                    "15-10-2026"
                ),
                (
                    "Need Based Scholarship",
                    "Eligible students with financial need",
                    "31-10-2026"
                )
            ]

            self.cursor.executemany("""
                INSERT INTO scholarships
                (name, eligibility, deadline)
                VALUES (?, ?, ?)
            """, scholarships)

        self.connection.commit()

    def get_notices(self):

        self.cursor.execute("""
            SELECT title, description, date
            FROM notices
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def get_events(self):

        self.cursor.execute("""
            SELECT name, date, venue
            FROM events
            ORDER BY id
        """)

        return self.cursor.fetchall()

    def get_internships(self):

        self.cursor.execute("""
            SELECT title, company, skills
            FROM internships
        """)

        return self.cursor.fetchall()

    def get_faculty(self):

        self.cursor.execute("""
            SELECT name, department, subject
            FROM faculty
        """)

        return self.cursor.fetchall()

    def get_timetable(self, day=None):

        if day:

            self.cursor.execute("""
                SELECT day, subject, time, room
                FROM timetable
                WHERE day = ?
            """, (day,))

        else:

            self.cursor.execute("""
                SELECT day, subject, time, room
                FROM timetable
            """)

        return self.cursor.fetchall()

    def get_scholarships(self):

        self.cursor.execute("""
            SELECT name, eligibility, deadline
            FROM scholarships
        """)

        return self.cursor.fetchall()


class SmartCampusAssistant:

    def __init__(self, root):

        self.root = root

        self.root.title("Smart Campus Assistant")

        self.root.geometry("1250x750")

        self.root.minsize(1000, 650)

        self.database = CampusDatabase()

        self.create_sidebar()

        self.create_chat_area()

        self.create_status_bar()

        self.show_welcome()

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.root,
            width=230,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        logo = ctk.CTkLabel(
            self.sidebar,
            text="🎓 Campus\nAssistant",
            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )
        )

        logo.pack(
            pady=(30, 30)
        )

        buttons = [
            ("🏠 Dashboard", self.show_welcome),
            ("📢 Notices", self.show_notices),
            ("📅 Events", self.show_events),
            ("💼 Internships", self.show_internships),
            ("👨‍🏫 Faculty", self.show_faculty),
            ("🗓 Timetable", self.show_timetable),
            ("💰 Scholarships", self.show_scholarships)
        ]

        for text, command in buttons:

            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=42,
                anchor="w",
                command=command
            )

            button.pack(
                fill="x",
                padx=15,
                pady=5
            )

        ctk.CTkButton(
            self.sidebar,
            text="🌙 Theme",
            height=40,
            command=self.change_theme
        ).pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=20
        )

    def create_chat_area(self):

        self.main = ctk.CTkFrame(
            self.root,
            corner_radius=0
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.header = ctk.CTkFrame(
            self.main,
            height=75
        )

        self.header.pack(
            fill="x"
        )

        self.header.pack_propagate(False)

        ctk.CTkLabel(
            self.header,
            text="Smart Campus Assistant",
            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )
        ).pack(
            side="left",
            padx=25
        )

        self.chat_box = ctk.CTkTextbox(
            self.main,
            wrap="word",
            font=ctk.CTkFont(size=15)
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.input_frame = ctk.CTkFrame(
            self.main
        )

        self.input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.user_input = ctk.CTkEntry(
            self.input_frame,
            height=45,
            placeholder_text="Ask something about your campus..."
        )

        self.user_input.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=10
        )

        self.user_input.bind(
            "<Return>",
            lambda event: self.send_message()
        )

        ctk.CTkButton(
            self.input_frame,
            text="Send ➤",
            width=100,
            height=45,
            command=self.send_message
        ).pack(
            side="right",
            padx=10,
            pady=10
        )

    def create_status_bar(self):

        self.status = ctk.CTkLabel(
            self.root,
            text="● System Online",
            anchor="w"
        )

        self.status.place(
            x=250,
            y=720
        )

    def show_welcome(self):

        self.clear_chat()

        self.add_bot_message(
            """
👋 Welcome to Smart Campus Assistant!

I can help you with:

📢 College notices
📅 Events
💼 Internships
👨‍🏫 Faculty information
🗓️ Timetable
💰 Scholarships

You can also ask me questions such as:

• "Show internships"
• "What events are coming?"
• "Show today's timetable"
• "Show scholarships"
• "Who teaches Python?"
"""
        )

    def send_message(self):

        message = self.user_input.get().strip()

        if not message:
            return

        self.add_user_message(message)

        self.user_input.delete(
            0,
            "end"
        )

        response = self.process_message(
            message.lower()
        )

        self.add_bot_message(response)

    def process_message(self, message):

        if "internship" in message:

            return self.format_internships()

        if "notice" in message:

            return self.format_notices()

        if "event" in message or "hackathon" in message:

            return self.format_events()

        if "scholarship" in message:

            return self.format_scholarships()

        if "faculty" in message or "teacher" in message:

            return self.format_faculty()

        if "python" in message and (
            "teacher" in message or
            "faculty" in message
        ):

            faculty = self.database.get_faculty()

            result = ""

            for person in faculty:

                if person[2].lower() == "python":

                    result += (
                        f"👨‍🏫 {person[0]}\n"
                        f"Department: {person[1]}\n"
                        f"Subject: {person[2]}\n\n"
                    )

            return result or "No Python faculty found."

        if "timetable" in message or "schedule" in message:

            day = None

            days = [
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday"
            ]

            for d in days:

                if d in message:

                    day = d.capitalize()

            return self.format_timetable(day)

        if (
            "hello" in message
            or "hi" in message
            or "hey" in message
        ):

            return (
                "👋 Hello! How can I help you today?\n\n"
                "Try asking about internships, "
                "events, notices, timetable or scholarships."
            )

        if "help" in message:

            return (
                "🤖 I can help with:\n\n"
                "📢 Notices\n"
                "📅 Events\n"
                "💼 Internships\n"
                "👨‍🏫 Faculty\n"
                "🗓️ Timetable\n"
                "💰 Scholarships"
            )

        return (
            "🤔 I couldn't understand that.\n\n"
            "Try:\n"
            "• Show internships\n"
            "• Show events\n"
            "• Show notices\n"
            "• Show scholarships\n"
            "• Show timetable\n"
            "• Show faculty"
        )

    def format_notices(self):

        data = self.database.get_notices()

        result = "📢 CAMPUS NOTICES\n\n"

        for title, description, date in data:

            result += (
                f"🔔 {title}\n"
                f"{description}\n"
                f"📅 Date: {date}\n"
                f"{'-' * 40}\n"
            )

        return result

    def format_events(self):

        data = self.database.get_events()

        result = "📅 UPCOMING EVENTS\n\n"

        for name, date, venue in data:

            result += (
                f"🎯 {name}\n"
                f"📅 Date: {date}\n"
                f"📍 Venue: {venue}\n"
                f"{'-' * 40}\n"
            )

        return result

    def format_internships(self):

        data = self.database.get_internships()

        result = "💼 INTERNSHIP OPPORTUNITIES\n\n"

        for title, company, skills in data:

            result += (
                f"💼 {title}\n"
                f"🏢 Company: {company}\n"
                f"🛠 Skills: {skills}\n"
                f"{'-' * 40}\n"
            )

        return result

    def format_faculty(self):

        data = self.database.get_faculty()

        result = "👨‍🏫 FACULTY DIRECTORY\n\n"

        for name, department, subject in data:

            result += (
                f"👨‍🏫 {name}\n"
                f"Department: {department}\n"
                f"Subject: {subject}\n"
                f"{'-' * 40}\n"
            )

        return result

    def format_timetable(self, day=None):

        data = self.database.get_timetable(day)

        result = "🗓️ TIMETABLE\n\n"

        if not data:

            return "No timetable found."

        for day_name, subject, time, room in data:

            result += (
                f"📅 {day_name}\n"
                f"📚 {subject}\n"
                f"⏰ {time}\n"
                f"📍 {room}\n"
                f"{'-' * 40}\n"
            )

        return result

    def format_scholarships(self):

        data = self.database.get_scholarships()

        result = "💰 SCHOLARSHIPS\n\n"

        for name, eligibility, deadline in data:

            result += (
                f"🎓 {name}\n"
                f"Eligibility: {eligibility}\n"
                f"Deadline: {deadline}\n"
                f"{'-' * 40}\n"
            )

        return result

    def add_user_message(self, message):

        self.chat_box.insert(
            "end",
            f"\n👤 You\n{message}\n"
        )

        self.chat_box.see("end")

    def add_bot_message(self, message):

        self.chat_box.insert(
            "end",
            f"\n🤖 Campus Assistant\n{message}\n"
        )

        self.chat_box.see("end")

    def clear_chat(self):

        self.chat_box.delete(
            "1.0",
            "end"
        )

    def show_notices(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_notices()
        )

    def show_events(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_events()
        )

    def show_internships(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_internships()
        )

    def show_faculty(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_faculty()
        )

    def show_timetable(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_timetable()
        )

    def show_scholarships(self):

        self.clear_chat()

        self.add_bot_message(
            self.format_scholarships()
        )

    def change_theme(self):

        current = ctk.get_appearance_mode()

        if current == "Dark":

            ctk.set_appearance_mode("light")

        else:

            ctk.set_appearance_mode("dark")


if __name__ == "__main__":

    root = ctk.CTk()

    app = SmartCampusAssistant(root)

    root.mainloop()