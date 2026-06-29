from datetime import datetime

message = input("Enter log message: ")

with open("server.log", "a") as file:
    file.write(f"{datetime.now()} : {message}\n")

print("Log saved.")