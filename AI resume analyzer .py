import customtkinter as ctk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import re
from datetime import datetime


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


SKILLS = {
    "Python",
    "Java",
    "C++",
    "C",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "PHP",
    "SQL",
    "MySQL",
    "MongoDB",
    "PostgreSQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Data Analysis",
    "Statistics",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Linux",
    "REST API",
    "FastAPI",
    "Keras",
    "OpenCV",
    "NLP",
    "Natural Language Processing",
    "DSA",
    "Data Structures",
    "Algorithms",
}


class ResumeAnalyzer:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Resume Analyzer")
        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)

        self.resume_text = ""
        self.resume_path = ""
        self.matched_skills = []
        self.missing_skills = []
        self.score = 0

        self.create_header()
        self.create_main_area()
        self.create_footer()

    def create_header(self):

        header = ctk.CTkFrame(
            self.root,
            height=80,
            corner_radius=0
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        title = ctk.CTkLabel(
            header,
            text="🤖  AI Resume Analyzer",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(side="left", padx=30, pady=20)

        subtitle = ctk.CTkLabel(
            header,
            text="Smart Resume & Job Matching System",
            font=ctk.CTkFont(size=14)
        )
        subtitle.pack(side="right", padx=30)

    def create_main_area(self):

        main = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )
        main.pack(fill="both", expand=True, padx=20, pady=20)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)

        # LEFT PANEL

        left = ctk.CTkFrame(
            main,
            corner_radius=15
        )
        left.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="nsew"
        )

        left.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(
            left,
            text="📄 Resume",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

        self.upload_button = ctk.CTkButton(
            left,
            text="Upload Resume PDF",
            height=40,
            command=self.upload_resume
        )
        self.upload_button.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.file_label = ctk.CTkLabel(
            left,
            text="No resume selected",
            text_color="gray"
        )
        self.file_label.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        ctk.CTkLabel(
            left,
            text="Resume Preview",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.resume_box = ctk.CTkTextbox(
            left,
            corner_radius=10,
            wrap="word"
        )
        self.resume_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        # RIGHT PANEL

        right = ctk.CTkFrame(
            main,
            corner_radius=15
        )
        right.grid(
            row=0,
            column=1,
            padx=(10, 0),
            sticky="nsew"
        )

        right.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(
            right,
            text="🎯 Job Description",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.job_box = ctk.CTkTextbox(
            right,
            height=180,
            corner_radius=10,
            wrap="word"
        )
        self.job_box.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.job_box.insert(
            "1.0",
            """Example:
We are looking for a Python Data Analyst.

Required skills:
Python, SQL, Pandas, NumPy, Excel,
Power BI, Statistics, Machine Learning,
Data Analysis and Git."""
        )

        self.analyze_button = ctk.CTkButton(
            right,
            text="🔍 Analyze Resume",
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.analyze_resume
        )
        self.analyze_button.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.result_box = ctk.CTkTextbox(
            right,
            corner_radius=10,
            wrap="word"
        )
        self.result_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    def create_footer(self):

        footer = ctk.CTkFrame(
            self.root,
            height=60,
            corner_radius=0
        )
        footer.pack(fill="x")
        footer.pack_propagate(False)

        self.save_button = ctk.CTkButton(
            footer,
            text="💾 Save Report",
            width=150,
            command=self.save_report
        )
        self.save_button.pack(
            side="left",
            padx=20,
            pady=10
        )

        clear_button = ctk.CTkButton(
            footer,
            text="🗑 Clear",
            width=120,
            command=self.clear_all
        )
        clear_button.pack(
            side="left",
            pady=10
        )

        self.status_label = ctk.CTkLabel(
            footer,
            text="Ready",
            text_color="gray"
        )
        self.status_label.pack(
            side="right",
            padx=20
        )

    def upload_resume(self):

        path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[
                ("PDF Files", "*.pdf")
            ]
        )

        if not path:
            return

        try:

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            if not text.strip():
                messagebox.showerror(
                    "Error",
                    "Could not extract text from this PDF."
                )
                return

            self.resume_text = text
            self.resume_path = path

            filename = path.split("/")[-1]

            self.file_label.configure(
                text=f"Selected: {filename}",
                text_color="#4CAF50"
            )

            self.resume_box.delete("1.0", "end")
            self.resume_box.insert(
                "1.0",
                text
            )

            self.status_label.configure(
                text="Resume loaded successfully"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to read PDF:\n\n{e}"
            )

    def extract_skills(self, text):

        text_lower = text.lower()

        found = []

        for skill in SKILLS:

            skill_lower = skill.lower()

            pattern = r"\b" + re.escape(skill_lower) + r"\b"

            if re.search(pattern, text_lower):
                found.append(skill)

        return sorted(found)

    def analyze_resume(self):

        if not self.resume_text:

            messagebox.showwarning(
                "Resume Required",
                "Please upload a PDF resume first."
            )

            return

        job_description = self.job_box.get(
            "1.0",
            "end"
        ).strip()

        if not job_description:

            messagebox.showwarning(
                "Job Description Required",
                "Please enter a job description."
            )

            return

        resume_skills = self.extract_skills(
            self.resume_text
        )

        job_skills = self.extract_skills(
            job_description
        )

        if not job_skills:

            messagebox.showwarning(
                "No Skills Found",
                "No recognized technical skills were found "
                "in the job description."
            )

            return

        resume_set = set(
            skill.lower()
            for skill in resume_skills
        )

        job_set = set(
            skill.lower()
            for skill in job_skills
        )

        matched_lower = resume_set.intersection(
            job_set
        )

        missing_lower = job_set.difference(
            resume_set
        )

        self.matched_skills = [
            skill for skill in job_skills
            if skill.lower() in matched_lower
        ]

        self.missing_skills = [
            skill for skill in job_skills
            if skill.lower() in missing_lower
        ]

        self.score = round(
            len(matched_lower) / len(job_set) * 100
        )

        self.display_results(
            resume_skills,
            job_skills
        )

        self.status_label.configure(
            text="Analysis completed"
        )

    def display_results(
        self,
        resume_skills,
        job_skills
    ):

        self.result_box.delete(
            "1.0",
            "end"
        )

        if self.score >= 80:
            status = "Excellent Match ⭐⭐⭐"
        elif self.score >= 60:
            status = "Good Match ⭐⭐"
        elif self.score >= 40:
            status = "Moderate Match ⭐"
        else:
            status = "Needs Improvement"

        result = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        RESUME ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 JOB MATCH SCORE

        {self.score}%

{status}


✅ MATCHED SKILLS

"""

        if self.matched_skills:

            for skill in self.matched_skills:
                result += f"✓ {skill}\n"

        else:
            result += "No matching skills found.\n"

        result += """

❌ MISSING SKILLS

"""

        if self.missing_skills:

            for skill in self.missing_skills:
                result += f"✗ {skill}\n"

        else:
            result += "No major missing skills detected.\n"

        result += """

🧠 RESUME SKILLS DETECTED

"""

        if resume_skills:

            for skill in resume_skills:
                result += f"• {skill}\n"

        else:
            result += "No recognized skills detected.\n"

        result += """

🎯 RECOMMENDATIONS

"""

        if self.missing_skills:

            result += (
                "Focus on developing these skills:\n\n"
            )

            for skill in self.missing_skills:
                result += f"→ {skill}\n"

        else:

            result += (
                "Your detected skills cover the "
                "recognized requirements of this job.\n"
            )

        result += f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analysis Date:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

        self.result_box.insert(
            "1.0",
            result
        )

    def save_report(self):

        content = self.result_box.get(
            "1.0",
            "end"
        ).strip()

        if not content:

            messagebox.showwarning(
                "No Report",
                "Analyze a resume before saving."
            )

            return

        path = filedialog.asksaveasfilename(
            title="Save Analysis Report",
            defaultextension=".txt",
            filetypes=[
                ("Text File", "*.txt")
            ]
        )

        if not path:
            return

        try:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    "AI RESUME ANALYZER REPORT\n"
                )

                file.write(
                    "=" * 50 + "\n\n"
                )

                file.write(content)

            messagebox.showinfo(
                "Success",
                "Report saved successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not save report:\n{e}"
            )

    def clear_all(self):

        self.resume_text = ""
        self.resume_path = ""
        self.matched_skills = []
        self.missing_skills = []
        self.score = 0

        self.resume_box.delete(
            "1.0",
            "end"
        )

        self.result_box.delete(
            "1.0",
            "end"
        )

        self.job_box.delete(
            "1.0",
            "end"
        )

        self.job_box.insert(
            "1.0",
            "Enter the job description here..."
        )

        self.file_label.configure(
            text="No resume selected",
            text_color="gray"
        )

        self.status_label.configure(
            text="Ready"
        )


if __name__ == "__main__":

    root = ctk.CTk()

    app = ResumeAnalyzer(root)

    root.mainloop()