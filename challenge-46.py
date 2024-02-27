'''
Task


Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format:

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints:
1. 0 < total number of students in college < 100

Output Format:

Output total number of students who have subscriptions to the English or the French newspaper but not both.

'''


if __name__ == "__main__":
    # Number of students subscribed to English newspaper
    n = int(input())
    
    # Set of roll numbers of students subscribed to English newspaper
    english_subs = set(map(int, input().split()))
    
    # Number of students subscribed to French newspaper
    b = int(input())
    
    # Set of roll numbers of students subscribed to French newspaper
    french_subs = set(map(int, input().split()))
    
    # Find the students who have subscribed to either English or French newspaper but not both
    either_or_subs = english_subs.symmetric_difference(french_subs)
    
    # Output the total number of students who have subscriptions to either English or French newspaper but not both
    print(len(either_or_subs))
