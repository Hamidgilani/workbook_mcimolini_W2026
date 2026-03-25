# Import the class data using the data module.
from data.course_data import student_data, assignment_data, submission_data

from tools.course import Course
from tools.student import Student
from tools.assignment import Assignment
from tools.submission import Submission

def add_students(course):
    for student in student_data: # at this point student is just a dictionary entry
        student_instance = Student(student["id"], student["name"]) # now we have a student instance/object
        course.add_student(student_instance) 

def add_assignments(course):
    for assignment in assignment_data: # still just a dictionary entry 
        assignment_instance = Assignment(assignment["id"],assignment["name"])
        course.add_assignment(assignment_instance)
def add_submissions(course):
    for submission in submission_data:
        student = course.get_student(submission["student_id"]) # gets a student or None
        assignment = course.get_assignment(submission["assignment_id"]) # gets an Assignment or None 

        submission = Submission(student,assignment,submission["grade"])
        student.add_submission(submission)



if __name__ == "__main__":
    course = Course("Dan's Basketball Course")

    add_students(course)
    add_assignments(course)
    add_submissions(course)

    print(course)

    print(f"course average: {course.get_course_average()}")



