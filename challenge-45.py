'''
Task


Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints
1. 0 < total number of students in college < 1000

Output Format

Output the total number of students who are subscribed to the English newspaper only.
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
    
    # Find the students who are subscribed to only English newspapers
    english_only_subs = english_subs - french_subs
    
    # Output the total number of students who are subscribed to only English newspapers
    print(len(english_only_subs))

