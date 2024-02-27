'''
Task

n this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Input Format:

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints:
1. 1 <= n <= 10000
2. 1 <= m <= 100
3. 1 <= length of each word in the input <= 100

Output Format:

Output  lines.
The ith line should contain the -indexed positions of the occurrences of the ith word separated by spaces.

'''


def find_word_indices(n, m, group_a, group_b):
    word_indices = {}
    # Populate the word_indices dictionary with indices of words in group A
    for i, word in enumerate(group_a):
        if word in word_indices:
            word_indices[word].append(i + 1)
        else:
            word_indices[word] = [i + 1]
    
    # For each word in group B, print its indices in group A or -1 if not found
    for word in group_b:
        if word in word_indices:
            print(*word_indices[word])
        else:
            print(-1)

if __name__ == "__main__":
    n, m = map(int, input().split())  # Number of words in group A and group B
    group_a = [input().strip() for _ in range(n)]  # Words in group A
    group_b = [input().strip() for _ in range(m)]  # Words in group B
    
    # Find and print the indices of words in group B in group A
    find_word_indices(n, m, group_a, group_b)


