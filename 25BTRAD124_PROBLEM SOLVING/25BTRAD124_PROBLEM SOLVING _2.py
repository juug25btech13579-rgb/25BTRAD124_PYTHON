# Student Grading Automation
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"
n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    grade = calculate_grade(marks)
    students[name] = grade
print("\n--- Student Grades ---")
for name, grade in students.items():
    print(name, ":", grade)
