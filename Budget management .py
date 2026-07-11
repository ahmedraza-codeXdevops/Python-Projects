budget = 100000

while True:
    print("\nCurrent Budget:", budget)

    amount = int(input("Enter project cost (0 to Exit): "))

    if amount == 0:
        break

    if amount <= budget:
        budget -= amount
        print("Project Approved")
    else:
        print("Budget Insufficient")