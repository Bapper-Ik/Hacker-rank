'''
Task


Consider the following:
A string, S, of length N where S=c0c1...cn-1.
An integer, K, where K is a factor of N.
We can split S into N/K substrings where each subtring, ti, consists of a contiguous block of K characters in S. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index J in ti occurs at a previous index <J in ti, then do not include the character in string ui.
Given S andK , print N/K lines where each line  denotes string ui.

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze

Prints:
Print each subsequence on a new line. There will be N/K of them. No return value is expected.

def merge_the_tools(string, k):
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

Input Format:
The first line contains a single string,S .
The second line contains an integer, K, the length of each substring.

constraints:
1. 1 <= N <= 10^4
2. 1 <= K <= N


'''


def merge_the_tools(string, k):
    # your code goes here
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    
    # Process each substring
    for substring in substrings:
        # Create a set to store unique characters
        unique_chars = set()
        # Build the new string with duplicate characters removed
        new_string = ''
        for char in substring:
            if char not in unique_chars:
                new_string += char
                unique_chars.add(char)
        # Print the new string
        print(new_string)



string, k = input(), int(input())
merge_the_tools(string, k)