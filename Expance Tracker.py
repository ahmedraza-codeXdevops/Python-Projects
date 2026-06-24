expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
        print("Expense Added Successfully!")

    elif choice == "2":
        print("\nExpenses:")
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(f"{expense['item']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Spending: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid Choice!")