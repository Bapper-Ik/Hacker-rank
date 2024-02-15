'''
Task
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

'''

n = int(input("Enter the number of students: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter student name and marks separated by space: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("Enter the name of the student: ")

marks = student_marks[query_name]

average = sum(marks) / len(marks)

print("{:.2f}".format(average))
