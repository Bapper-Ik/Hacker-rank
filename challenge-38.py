'''
Task

Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and names.

Your task is to help Dr. Wesley calculate the average marks of the students.

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format:

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, names and class, under their respective column names.

Constraints:
1. 0 < N <= 100

Output Format:
Print the average marks of the list corrected to 2 decimal places.
'''



def calculate_average_marks(N, columns, data):
    # Find the index of the column containing marks
    marks_index = columns.index('MARKS')
    
    # Extract the marks of each student and calculate the total sum
    total_marks = sum(int(student[marks_index]) for student in data)
    
    # Calculate the average marks
    average_marks = total_marks / N
    
    return average_marks

if __name__ == "__main__":
    N = int(input())  # Total number of students
    columns = input().split()  # Names of the columns
    data = [input().split() for _ in range(N)]  # Marks, IDs, names, and class of each student
    
    # Calculate and print the average marks corrected to 2 decimal places
    average_marks = calculate_average_marks(N, columns, data)
    print("{:.2f}".format(average_marks))
