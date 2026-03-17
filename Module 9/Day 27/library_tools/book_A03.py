class Book: # class names are PascalCase (every starting letter capitalized)
    # This is our constructor. self is required, the rest are optional parameters
    def __init__(self, title, author, pages): # self can be named somethign else, but self is the industry standard
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ dunder method. Tells python how to print our instances
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # If I want to compare two instance of Book I need to define __eq__, __gt__, and __lt__
    # ToDo as homework of future demo

    
