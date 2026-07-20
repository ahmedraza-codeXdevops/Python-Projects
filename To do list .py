import tkinter as tk

def add_task_to_list():
    add_new_task = task_entry.get()
    if add_new_task:
        task_listbox.insert(tk.END, add_new_task)
        task_entry.delete(0, tk.END)


def remove_task_from_list():
    selected_task = task_listbox.curselection()
    if selected_task:
        
        for index in reversed(selected_task):
            task_listbox.delete(index)

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        for index in selected_task:
            task = task_listbox.get(index)

            if "❌" in task:
                new = task.replace("❌", "✅", 1)
            else:
                new = task.replace("✅", "❌", 1)
            task_listbox.delete(index)
            task_listbox.insert(index, new)



window = tk.Tk()
window.title("To Do List")
window.geometry("400x400")

task_entry = tk.Entry (window, width=30)
task_entry.pack (pady=10)

add_task_button = tk.Button (window, text="Add Task",  width=30, command=add_task_to_list)
add_task_button.pack()

task_listbox = tk.Listbox (window, width=40, height=10)
task_listbox.pack (pady=10)

delete_task_button = tk.Button(window, text="Delete Task", command=remove_task_from_list)
delete_task_button.pack()

mark_completed_button = tk.Button(window, text="Toggle Completed", command=mark_completed)
mark_completed_button.pack(pady=5)

window.mainloop()
