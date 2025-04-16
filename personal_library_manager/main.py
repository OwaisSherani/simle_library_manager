import json

class BookCollection: # class is a blue print to make an object
    """A class to manage a collection of books, allowing user to store and organize their reading materials"""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage"""
        self.book_list = [] #self to manage the data in class
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory
        If the file doesn't exist or is corrupted, start with an empty collection"""
        try:
            with open (self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for premenant storage"""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering infromation from the user"""
        book_title = input("Enter Book title: ")
        book_author = input("Enter author: ")
        publicatin_year = input("Enter Publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title" : book_title,
            "author" : book_author,
            "year" : publicatin_year,
            "genre" : book_genre,
            "read" : is_book_read,

        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from collection using its title"""
        book_title = input("Enter the title of book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
            print("Book not found\n")


    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]
        if found_books:
            print("Matching Book")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                    print("Leave blank to keep existing value.")
                    book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                    book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                    book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                    book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                    book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"  )

                    self.save_to_file()
                    print("Book updated successfully!\n")
                    return
        print("Book not found!\n")

    def start_application(self):
        while True:
            print("Welcome to your Book Collection Manager")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Find a book")
            print("4. Update a book")


            user_choice = input("Please Choose an option (1-4): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()

            else:
                print("Invalid choice. Please Try again!")

if __name__ == "__main__":

    book_manager = BookCollection()
    book_manager.start_application()

   
