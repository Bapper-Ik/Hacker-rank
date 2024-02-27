'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format:
A single line of input containing the space separated month, day and year, respectively, in  MM DD YY  format.

Constraints:
1. 2000 < year < 3000

Output Format:
Output the correct day in capital letters.
'''


from datetime import datetime

def find_day(month, day, year):
    # Create a datetime object for the given date
    date_object = datetime(year, month, day)
    
    # Get the day name from the datetime object
    day_name = date_object.strftime('%A').upper()
    
    return day_name

if __name__ == "__main__":
    # Input the date in MM DD YY format
    month, day, year = map(int, input().split())
    
    # Call the function to find the day
    day_of_week = find_day(month, day, year)
    
    # Output the day in capital letters
    print(day_of_week)
