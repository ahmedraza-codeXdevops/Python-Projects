contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print("-" * 20)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("\nContact Found")
        print(f"Name : {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")