class Submission:
    def __init__(self,student,assignment,grade): # our class methods ca take other classes as input
        self.student = student 
        self.assignment = assignment 
        self.grade = grade 

    def __str__(self):
        return f"{self.student.name} receieved{self.grade} on {self.assignment}"