import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()

    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def complete_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        task = task_list.get(index)

        if not task.startswith("✓ "):
            task_list.delete(index)
            task_list.insert(index, "✓ " + task)
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def clear_tasks():
    if task_list.size() > 0:
        confirm = messagebox.askyesno(
            "Clear All",
            "Are you sure you want to delete all tasks?"
        )

        if confirm:
            task_list.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f4f6f8")

title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8",
    fg="#222"
)
title.pack(pady=25)

task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=35
)
task_entry.pack(pady=10, ipady=8)

add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12, "bold"),
    width=15,
    command=add_task
)
add_button.pack(pady=10)

task_list = tk.Listbox(
    root,
    font=("Arial", 14),
    width=38,
    height=14,
    selectmode=tk.SINGLE
)
task_list.pack(pady=15)

button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=10)

complete_button = tk.Button(
    button_frame,
    text="Complete",
    font=("Arial", 11, "bold"),
    width=10,
    command=complete_task
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    font=("Arial", 11, "bold"),
    width=10,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    font=("Arial", 11, "bold"),
    width=10,
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()