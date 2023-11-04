student_grades = {
    "alice": [85,90,95],
    "bob": [88,89,92,95],
    "chali": [78,80],
    "david": [95,96,98]
}

for student, grades in student_grades.items():
    average_grade= sum(grades)/len(grades)
    print(student, average_grade)