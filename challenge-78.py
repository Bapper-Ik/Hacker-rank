'''
Task

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Input Format:
The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

Constraints:
1. 0 < N <= 100
2. 0 < X <= 100

Output Format:
Print the averages of all students on separate lines.

The averages must be correct up to 1 decimal place.
'''



# Read input
N, X = map(int, input().split())

# Initialize a list to store the sum of scores for each student
student_scores_sum = [0] * N

# Read scores for each subject and accumulate the scores for each student
for _ in range(X):
    scores = list(map(float, input().split()))
    for i in range(N):
        student_scores_sum[i] += scores[i]

# Compute the average score for each student and print
for i in range(N):
    average_score = student_scores_sum[i] / X
    print("{:.1f}".format(average_score))
