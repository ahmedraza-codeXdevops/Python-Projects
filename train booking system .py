train_name = "Rajdhani Express"
available_seats = 5

print("Train:", train_name)
print("Available Seats:", available_seats)

tickets = int(input("How many tickets do you want? "))

if tickets <= available_seats:
    available_seats -= tickets
    print("Booking Successful!")
    print("Remaining Seats:", available_seats)
else:
    print("Sorry! Seats not available.")