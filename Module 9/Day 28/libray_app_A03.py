from library_tools.book_A03 import Book
from library_tools.library_A03 import Library

if __name__ == '__main__':
    print("Welcome to our Library App")
    print("--------------------------")

    library = Library("Library of Alexandria")
    print(library)

    book = Book("Percy Jackson and the Lightning Thief", # nothing fancy about these new lines
                "Rick Riordan",
                435)
    
    # Once we have an instance of our Class (book) aka an Object of type Book, we can do stuff with it
    print("The properties of our book are:")
    print(f"Title: {book.title}")
    print(f"Autor: {book.author}")
    
    # We can print the object itself
    print("The Book instance is:")
    print(book) # until we define a __str__ or __repr__ this will print the object type and memory address.

    library.list_books() # this will be empty

    library.add_book(book)
    library.list_books()

    library.remove_book(book.title)
    library.list_books()

    library.add_book(book)
    library.add_book(Book("Percy Jackson", "Rick Riordan", 250))
    library.add_book(Book("Z", "ABCD", 26))
    library.add_book(Book("Anthology: Percy Jackson", "Rick Riordan", 3000))

    print("Sorted Library")
    library.sort_library()
    library.list_books()