import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

userscore = 0
computerscore = 0

def play_game(user_choice):
    global userscore, computerscore

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        userscore += 1
    else:
        result = "Computer Wins!"
        computerscore += 1

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {userscore} | Computer Score: {computerscore}"
    )


def reset_game():
    global userscore, computerscore

    userscore = 0
    computerscore = 0

    user_choice_label.config(text="Your Choice: -")
    computer_choice_label.config(text="Computer Choice: -")
    result_label.config(text="")
    score_label.config(text="Your Score: 0 | Computer Score: 0")


def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x400")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Rock-Paper-Scissors Game",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

instructions = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12)
)
instructions.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

rock_button = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    command=lambda: play_game("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(
    root,
    text="Your Choice: -",
    font=("Arial", 12)
)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(
    root,
    text="Computer Choice: -",
    font=("Arial", 12)
)
computer_choice_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

score_label = tk.Label(
    root,
    text="Your Score: 0 | Computer Score: 0",
    font=("Arial", 12)
)
score_label.pack(pady=10)

control_frame = tk.Frame(root)
control_frame.pack(pady=15)

reset_button = tk.Button(
    control_frame,
    text="Reset Game",
    width=15,
    command=reset_game
)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    control_frame,
    text="Exit Game",
    width=15,
    command=exit_game
)
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()
