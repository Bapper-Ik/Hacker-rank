'''
Task
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''


N = int(input("Enter the number of students: "))

students = []
for _ in range(N):
    name = input("Enter student's name: ")
    score = float(input("Enter student's score: "))
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_lowest_grade = None
for student in students:
    if second_lowest_grade is None:
        second_lowest_grade = student[1]
    elif student[1] > second_lowest_grade:
        second_lowest_grade = student[1]
        break

second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

second_lowest_students.sort()

for name in second_lowest_students:
    print(name)
