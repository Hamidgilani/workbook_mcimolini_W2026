from library_tools.book import Book
from library_tools.library import Library

if __name__ == '__main__':
    print("Welcome to our library App")
    print("---------------------------")

    library = Library("Fantasy Tavern Library")
    book = Book("Sojourn", "R.A Salvatore", 309)


    print(book)
    print(f"{book.author} is the author.")
    print(f"{book.title} is the title.")

    library.list_books()

    library.add_book(book)

    print(f"Books in {library}:")
    library.list_books()