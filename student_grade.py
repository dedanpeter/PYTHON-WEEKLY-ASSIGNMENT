# student_grade.py
# Task 2: Student Grade Function

# A function that gives a grade from a mark
def calculate_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

# Ask the user for the mark
mark = float(input("Enter the student's mark: "))

# Call the function
grade = calculate_grade(mark)

# Show the answer
print("Grade:", grade)
