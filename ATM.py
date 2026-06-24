balance = 10000

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance += amount

    elif choice == "3":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient Balance")

    elif choice == "4":
        break