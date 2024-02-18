'''
Task
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

'''


def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    # Create the lines of the rangoli
    for i in range(size):
        s = "-".join(alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    # Print the rangoli in reverse order and then in the correct order
    for line in lines[::-1] + lines[1:]:
        print(line)

# Example usage
N = 5
print_rangoli(N)