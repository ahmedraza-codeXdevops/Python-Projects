import shutil

source = input("Source file: ")
destination = input("Backup file name: ")

shutil.copy(source, destination)

print("Backup completed.")