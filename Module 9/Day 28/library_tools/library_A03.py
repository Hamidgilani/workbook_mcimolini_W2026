class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # attributes do not need to be passed in by the constructor

    def __str__(self):
        return f"{self.name}"
    
    # allows users to add books to the library
    def add_book(self, book):
        self.books.append(book) # add the book to the end of our current collection

    # allows us to print a list of all books in the library
    def list_books(self):
        print("Current Library Inventory:")

        if len(self.books) == 0:
            print("-No books in library-")
        # outcome would be the same if this is in an else as there will be no books to iterate through
        for book in self.books:
            print(f"- {book}")

    #ToDo make a method to remove books
    def remove_book(self, title):
        self.books.remove(title) # this won't work as string != book
        # the above will work now that we've modified the __eq__ method in Book
        
        # for now, let's do it with a loop
        #for book in self.books:
        #    if book.title == title:
        #        self.books.remove(book) # this should work
                # this works, but it's rather clunky. We can make this better by modifying book
                # we can do this with dunder function in book
    
    def sort_library(self, reverse = False):
        self.books.sort(reverse=reverse) # this works out of the box, but we have no control over how
        # lets go implement our other comparisons in Book