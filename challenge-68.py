'''
Task

write a code that'll generate a HackerRank logo with "H"

Input Format:

A single line containing the thickness value for the logo.

Constraints:
1. the thickness must be an odd number
2. 0 < thickness < 50


Output Format:

Output the desired logo.
'''



def print_hackerrank_logo(thickness):
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


if __name__ == "__main__":
    thickness = int(input())
    if thickness % 2 == 0:
        print("Thickness must be an odd number.")
    else:
        print_hackerrank_logo(thickness)
