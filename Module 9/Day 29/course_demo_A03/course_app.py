# Import the class data using the data module.
from data.course_data import student_data, assignment_data, submission_data

# Import our classes
from tools.course import Course
from tools.student import Student
from tools.assignment import Assignment
from tools.submission import Submission

# This will add all students in our student_data file to the provided course
def add_students(course):
    for student in student_data: # not a Student class, just a dictionary entry
        student_instance = Student(student["id"], student["name"]) # turns the dictionary entry into a Student instance
        course.add_student(student_instance) # add the newly created student to our course

# Same as above but assignments
def add_assignments(course):
    for assignment in assignment_data: # not an Assignment class, just a dictionary entry
        assignment_instance = Assignment(assignment["id"], assignment["name"]) # turns the dictionary entry into an Assignment instance
        course.add_assignment(assignment_instance)

def add_submissions(course):
    for submission in submission_data: # dictionary entry
        student = course.get_student(submission["student_id"]) # finds our Student if they exist
        assignment = course.get_assignment(submission["assignment_id"]) # finds our Assignment if it exists

        submission = Submission(student, assignment, submission["grade"]) # creates our Submission

        student.add_submission(submission) # this can fail if our student doesn't exist and should be error checked

if __name__ == "__main__":
    course = Course("Dans Basketball Mastery Course") # creates and instance of our Course class

    add_students(course)
    add_assignments(course)
    add_submissions(course)

    print(course)
    print(f"Course average: {course.get_course_average()}")