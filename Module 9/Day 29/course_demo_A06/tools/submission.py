class Submission:
    def __init__(self, student, assignment, grade): # our class methods can take other classes as input
        self.student = student
        self.assignmnet = assignment
        self.grade = grade

    def __str__(self):
        return f"{self.student.name} received {self.grade} on {self.assignmnet}"