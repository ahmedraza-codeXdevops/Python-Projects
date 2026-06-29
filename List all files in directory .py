import os

path = input("Enter folder path: ")

for file in os.listdir(path):
    print(file)