student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 65,
    "Eve": 95
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    print(f"Student '{student_name}' not found in the dictionary.")
