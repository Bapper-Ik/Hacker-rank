'''
Task

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format:

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Constraints:
1. Input contains only valid timestamps
2. year <= 3000
.
Output Format:

Print the absolute difference (t1-t2) in seconds.
'''


from datetime import datetime

def time_difference_seconds(t1, t2):
    # Parse the timestamps into datetime objects
    t1_datetime = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_datetime = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    
    # Calculate the absolute difference in seconds
    time_difference = abs((t1_datetime - t2_datetime).total_seconds())
    
    return time_difference

if __name__ == "__main__":
    T = int(input())  # Number of testcases
    for _ in range(T):
        t1 = input().strip()  # First timestamp
        t2 = input().strip()  # Second timestamp
        
        # Call the function to calculate the time difference in seconds
        difference_seconds = time_difference_seconds(t1, t2)
        
        # Print the result
        print(int(difference_seconds))

