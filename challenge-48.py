'''
Task

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input Format:
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.


Constraints:
1. 1 < K < 1000

Output Format:
Output the Captain's room number.
'''


if __name__ == "__main__":
    # Size of each group
    k = int(input())
    
    # Unordered elements of the room number list
    room_numbers = list(map(int, input().split()))
    
    # Find the sum of all unique room numbers
    unique_room_sum = sum(set(room_numbers))
    
    # Find the sum of all room numbers
    total_room_sum = sum(room_numbers)
    
    # Calculate the Captain's room number
    captain_room_number = (unique_room_sum * k - total_room_sum) // (k - 1)
    
    # Print the Captain's room number
    print(captain_room_number)


