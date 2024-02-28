'''
Task

You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
Note: Do not print data if data == '\n'.

Input Format

The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.

Constraints
0 < N < 100

Output Format

Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.

Format the answers as explained in the problem statement.

'''



from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.single_line_comment = False
        self.multi_line_comment = False
        self.data = False

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

n = int(input())
html = ""
for i in range(n):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
