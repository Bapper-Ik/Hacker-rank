'''
Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format:

The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

Constraints:
1. 0 < total number of student in college < 1000

Output Format:

Output the total number of students who have subscriptions to both English and French newspapers.
'''

# Number of students subscribed to English newspaper
n = int(input())
    
    # Set of roll numbers of students subscribed to English newspaper
english_subs = set(map(int, input().split()))
    
    # Number of students subscribed to French newspaper
b = int(input())
    
    # Set of roll numbers of students subscribed to French newspaper
french_subs = set(map(int, input().split()))
    
    # Find the common roll numbers between the two sets
common_subs = english_subs.intersection(french_subs)
    
    # Output the total number of students who have subscriptions to both newspapers
print(len(common_subs))

