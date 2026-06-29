import os

try:
    with open("/proc/meminfo") as file:
        print(file.read())
except FileNotFoundError:
    print("This works on Linux only.")