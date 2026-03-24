class Library:
    def __init__(self,name):
        self.name = name 
        # We can add properties that aren't in the init
        self.books = []
        self.value = len(self.books) * 1000


    def __str__(self):
        return f"{self.name}"
    
    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        print("Current books in our library: ")

        if len(self.books) == 0:
            print("No books in our library :(")

        for book in self.books:
            print(f"- {book}")
                