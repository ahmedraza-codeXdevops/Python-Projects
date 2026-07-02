import random

trains = {
    1: {"name": "Rajdhani Express", "from": "Delhi", "to": "Mumbai", "fare": 1800, "seats": 20},
    2: {"name": "Shatabdi Express", "from": "Delhi", "to": "Chandigarh", "fare": 900, "seats": 15},
    3: {"name": "Duronto Express", "from": "Mumbai", "to": "Kolkata", "fare": 2200, "seats": 10},
    4: {"name": "Garib Rath", "from": "Pune", "to": "Delhi", "fare": 1200, "seats": 25}
}

print("=" * 50)
print("       RAILWAY TICKET BOOKING SYSTEM")
print("=" * 50)

print("\nAvailable Trains")
print("-" * 50)

for train_id, train in trains.items():
    print(f"{train_id}. {train['name']}")
    print(f"   Route : {train['from']} -> {train['to']}")
    print(f"   Fare  : ₹{train['fare']}")
    print(f"   Seats : {train['seats']}")
    print()

choice = int(input("Select Train Number: "))

if choice in trains:

    train = trains[choice]

    passengers = int(input("Number of Passengers: "))

    if passengers <= train["seats"]:

        name = input("Passenger Name: ")
        age = int(input("Passenger Age: "))
        gender = input("Gender: ")

        train["seats"] -= passengers

        total = passengers * train["fare"]

        pnr = random.randint(1000000000, 9999999999)

        print("\n" + "=" * 50)
        print("              BOOKING CONFIRMED")
        print("=" * 50)
        print("PNR Number      :", pnr)
        print("Passenger Name  :", name)
        print("Age             :", age)
        print("Gender          :", gender)
        print("Train           :", train["name"])
        print("From            :", train["from"])
        print("To              :", train["to"])
        print("Passengers      :", passengers)
        print("Total Fare      : ₹", total)
        print("Remaining Seats :", train["seats"])
        print("=" * 50)

    else:
        print("\nSorry! Seats Not Available.")

else:
    print("\nInvalid Train Selection.")