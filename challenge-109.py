'''
Task


CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. (1,2,3,4,5,6,7,8,9,A,B,C,D,E and F).
■ A-F letters can be lower case. (a,b,c,d,e, and f are also valid digits).

Examples:

Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}

Input Format:
The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Constraints:
0 < N < 50

Output Format:
Output the color codes with '#' symbols on separate lines

Explanation:
#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Note: There are no comments ( // or /* */) in CSS Code.

'''


import re

def extract_hex_color_codes(css_lines):
    hex_color_codes = []
    for line in css_lines:
        properties = re.findall(r'\b\w+\s*:\s*(.*?)\s*;', line)
        for prop in properties:
            matches = re.findall(r'#[0-9a-fA-F]{3,6}\b', prop)
            hex_color_codes.extend(matches)
    return hex_color_codes

if __name__ == "__main__":
    N = int(input().strip())
    css_lines = [input().strip() for _ in range(N)]
    color_codes = extract_hex_color_codes(css_lines)
    for code in color_codes:
        print(code)


