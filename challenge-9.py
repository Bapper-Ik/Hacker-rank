'''
Task
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up.
'''

n = int(input("Enter the number of scores: "))

scores = list(map(int, input("Enter the scores separated by space: ").split()))

sorted_scores = sorted(set(scores), reverse=True)

if len(sorted_scores) > 1:
    runner_up_score = sorted_scores[1]
    print(runner_up_score)
else:
    print("There is no runner-up score as there are not enough unique scores.")
