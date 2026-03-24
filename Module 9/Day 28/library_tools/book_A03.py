class Book: # class names are PascalCase (every starting letter capitalized)
    # This is our constructor. self is required, the rest are optional parameters
    def __init__(self, title:str, author:str, pages): # self can be named somethign else, but self is the industry standard
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ dunder method. Tells python how to print our instances
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # If I want to compare two instance of Book I need to define __eq__, __gt__, and __lt__
    # ToDo as homework of future demo
    def __eq__(self, other): # other will be the other instance of book we want to compare to
        # This works very similarly to how == works by default.
        # we could remove some of these comparisons if we want.
        #if not isinstance(other, Book): # checks to make sure that other is of type Book
        #    return NotImplemented
        
        #return self.title == other.title and self.author == other.author and self.pages == other.pages

        # lets change how this works and make it work for stings as well
        if isinstance(other, Book): # checks to make sure that other is of type Book     
            return self.title == other.title and self.author == other.author
        
        # possibly not the best comparison
        elif isinstance(other, str):
            return self.title == other

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        
        # sort first by author then by title
        if self.author == other.author: # if the authors are the same
            return self.title > other.title # compare the titles
        
        return self.author > other.author # if they're not, compare the authors
    
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        
        if self.author == other.author:
            return self.title < other.title

        return self.author < other.author