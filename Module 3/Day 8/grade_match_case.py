letter_grade = input("Enter your letter grade (A, B, C, or D): ").upper()
# or letter_grade = letter_grade.upper()
# This will change all of our input to upper-case for ease of comparison

# Convert our letter grade to a GPA
match letter_grade:
    case "A":
        gpa = 4.0
    case "B":
        gpa = 3.3
    case "C":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _: # default case
        print("Could not determine numeric grade")
        gpa = 0.0

print(f"Your GPA is {gpa}")