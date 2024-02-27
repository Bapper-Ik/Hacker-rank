'''
Task
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1. 1 <= N <= 10^5
2. The sum of the lengths of all the words do not exceed 10^6
3. All the words are composed of lowercase English letters only.

Input Format:

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

'''


def word_count(words):
    word_dict = {}
    # Iterate through the words
    for word in words:
        # Update the count of occurrences for each word
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

if __name__ == "__main__":
    n = int(input())  # Number of words
    words = [input().strip() for _ in range(n)]  # Input words
    
    # Count occurrences of each word
    word_counts = word_count(words)
    
    # Output the number of distinct words
    print(len(word_counts))
    # Output the number of occurrences for each distinct word
    print(*word_counts.values())

