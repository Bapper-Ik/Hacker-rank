'''
Task

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.
'''


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    # Update maxdepth if the current level is greater
    maxdepth = max(maxdepth, level + 1)
    
    # Recursively process child nodes
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)