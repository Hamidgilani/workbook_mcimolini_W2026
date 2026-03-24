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

    # Finds a student by ID. Returns None if the student is not found.
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id: # if the ID matches we return the Student
                return student
        
        return None
    
    # Same as above for Assignment
    def get_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                return assignment
            
        return None
    
    # Loops through all students and all of their submissions and provides an average grade in the course
    def get_course_average(self):
        total = 0 # stores our total
        num_submissions = 0 # total submissions

        # nested for loop (a loop in a loop)
        for student in self.students: # first loop, loops through students
            for submission in student.submissions: # second loop, loops through our submissions
                total += submission.grade # same as total = total + submission.grade
                num_submissions += 1 # same as num_submissions = num_submission + 1
        
        return total / num_submissions