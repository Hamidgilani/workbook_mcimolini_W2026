class Assignment():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"Assignment ID: {self.id}, Assignment Name: {self.name}"
    
    # how the class will be represented while debugging or using breakpoints
    def __repr__(self):
        return str(self)