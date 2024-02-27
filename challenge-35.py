'''
Task

There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i] .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains N, the number of cubes.
The second line contains N space separated integers, denoting the sideLengths of each cube in that order.

Constraints
1. 1 <= T <= 5
2. 1 <= N <= 10^5
3. 1 <= sideLength < 2^31



Output Format

For each test case, output a single line containing either Yes or No.
'''

def check_stack_possibility(N, side_lengths):
    left = 0  # Pointer for the leftmost cube
    right = N - 1  # Pointer for the rightmost cube
    prev_cube = float('inf')  # Keep track of the side length of the previous cube
    
    while left <= right:
        if side_lengths[left] >= side_lengths[right]:
            current_cube = side_lengths[left]
            left += 1
        else:
            current_cube = side_lengths[right]
            right -= 1
        
        # If the current cube side length is greater than the previous cube, it's not possible to stack them
        if current_cube > prev_cube:
            return "No"
        prev_cube = current_cube
    
    return "Yes"

if __name__ == "__main__":
    T = int(input())  # Number of test cases
    
    for _ in range(T):
        N = int(input())  # Number of cubes
        side_lengths = list(map(int, input().split()))  # Side lengths of cubes
        
        # Check if it's possible to stack the cubes and print the result
        print(check_stack_possibility(N, side_lengths))
