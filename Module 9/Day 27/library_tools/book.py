# Make sure class name and file name are the same. It is a best practice
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
            return f"{self.title} by {self.author}"
