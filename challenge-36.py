'''
Task


'''



from collections import Counter

def top_three_characters(s):
    # Count the occurrences of each character in the string
    char_count = Counter(s)
    
    # Get the three most common characters
    top_three = char_count.most_common(3)
    
    # Sort the top three characters by occurrence count in descending order
    # If occurrence count is the same, sort characters in alphabetical order
    top_three_sorted = sorted(top_three, key=lambda x: (-x[1], x[0]))
    
    # Print the top three characters along with their occurrence count
    for char, count in top_three_sorted:
        print(char, count)

if __name__ == "__main__":
    s = input().strip()  # Input company name
    top_three_characters(s)
