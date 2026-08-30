print("🏰 Welcome to the Adventure Game!")

name = input("What is your name? ")
print(f"Hello, {name}!")

choice = input("You see a cave and a forest. Where do you go? ").lower()

if choice == "cave":
    print("You enter the dark cave.")
    action = input("You see a dragon! Run or fight? ").lower()

    if action == "fight":
        print("🐉 You defeat the dragon and find treasure!")
        print("🏆 YOU WIN!")
    else:
        print("You escape safely!")

elif choice == "forest":
    print("You walk into the forest.")
    action = input("You find a mysterious chest. Open it? (yes/no): ").lower()

    if action == "yes":
        print("💰 The chest is full of gold!")
        print("🏆 YOU WIN!")
    else:
        print("You continue walking and find your way home.")

else:
    print("You got lost! Game over.")
  
