class Submission:
    def __init__(self, student, assignment, grade):
        self.student = student
        self.assignment = assignment
        self.grade = grade
    
    def __str__(self):
        # we can access the methods and properties of other classes from other classes
        return f"{self.student.name} received {self.grade} on {self.assignment}"