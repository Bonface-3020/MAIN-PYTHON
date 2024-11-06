class Library:
    def __init__(self, name, book_list):
        self.bookList = book_list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-book database has been updated. You can take the book now.")
        else:
            print("Sorry, the book is already lent to someone else.", self.lendDict[book])

    def addBook(self, book):
        self.bookList.append(book)
        print("The book has been added.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print("The book has been returned.")
        else:
            print("The book was not lent out.")

if __name__ == '__main__':
    # Initialize the library with a list of books
    library = Library("Let's Upskill", ['Python', 'C++', 'Guido van Rossum', 'Algorithms', 'New School Chemistry', 'CSC 102', 'Social Skills'])

    while True:
        print(f"\nWelcome to {library.name}! Please enter a choice to continue:")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        print("5. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            library.displayBooks()
        elif user_choice == 2:
            book_name = input("Enter the name of the book you want to lend: ")
            user_name = input("Enter your name: ")
            library.lendBook(user_name, book_name)
        elif user_choice == 3:
            new_book = input("Enter the name of the book you want to add: ")
            library.addBook(new_book)
        elif user_choice == 4:
            book_name = input("Enter the name of the book you want to return: ")
            library.returnBook(book_name)
        elif user_choice == 5:
            print("Thank you for using the library. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        user_choice2 = input("Press 'q' to quit, or 'c' to continue: ").lower()
        if user_choice2 == "q":
            print("Thank you for using the library. Goodbye!")
            break
        elif user_choice2 == "c":
            continue
        else:
            print("Invalid input, returning to main menu.")
