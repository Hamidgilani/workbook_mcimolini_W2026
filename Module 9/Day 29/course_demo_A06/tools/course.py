class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self):
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments."
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        
        return None
    
    def get_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                return assignment
            
        return None
    
    def get_course_average(self):
        total = 0 # total grade points
        num_submissions = 0 # total submissions

        # we'll use a nest for loop for this
        for student in self.students: # outer loop through Students
            for submission in student.submissions: # inner loop through Submissions
                total += submission.grade
                num_submissions += 1
        
        return total / num_submissions