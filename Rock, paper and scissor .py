import random

choices = ["rock", "paper", "scissors"]

print("🎮 Rock, Paper, Scissors")

while True:
    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("💻 Computer wins!")

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
