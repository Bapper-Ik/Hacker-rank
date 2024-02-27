'''
Task

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i is an element of A, you add 1 to your happiness. If i is an element of B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints:
1. 1 <= n <= 10^5
2. 1 <= m <= 10^5
3. 1 <= any integer in the input <= 10^9


Input Format:
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format:
Output a single integer, your total happiness.

'''


if __name__ == "__main__":
    # Input sizes and arrays
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    # Calculate happiness
    happiness = 0
    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    # Output final happiness
    print(happiness)
