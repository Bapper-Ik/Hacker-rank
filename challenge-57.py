'''
Task

 ABC is a right triangle, 90 deg at B.
Therefore,  angle ABC=90 deg.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta deg, as shown in the figure) in degrees.

Input Format:
The first line contains the length of side AB.
The second line contains the length of side .

Constraints:
1. 0 < AB <= 100
2. 0 < BC <= 100
3. length AB and BC are natural numbers

Lengths  and  are natural numbers.
Output Format:

Output angle MBC in degrees.

Note: Round the angle to the nearest integer.
'''


import math

def find_angle_mbc(ab, bc):
    # Calculate the angle MBC in radians using atan2
    angle_rad = math.atan2(ab, bc)
    
    # Convert the angle from radians to degrees and round to the nearest integer
    angle_deg = round(math.degrees(angle_rad))
    
    return angle_deg

if __name__ == "__main__":
    ab = float(input())  # Length of side AB
    bc = float(input())  # Length of side BC
    
    angle_mbc = find_angle_mbc(ab, bc)
    print(f"{angle_mbc}\u00b0")   
    # Print the angle with the degree symbol

