books = ["Python", "SQL", "Data Science"]

while True:
    print("\n1.View Books")
    print("2.Issue Book")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(books)

    elif choice == "2":
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")

    elif choice == "3":
        break