'''
Task

assuming You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

note:
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:

The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Constraints:
1. 0 < N <= 100

Output Format:

Print the item_name and net_price in order of its first occurrence.
'''


def print_items_with_net_price(N, items):
    item_dict = {}
    for item in items:
        item_name, price = item.rsplit(' ', 1)
        if item_name not in item_dict:
            item_dict[item_name] = int(price)
        else:
            item_dict[item_name] += int(price)
    
    # Print each item_name and net_price in order of its first occurrence
    for item_name, net_price in item_dict.items():
        print(item_name, net_price)

if __name__ == "__main__":
    N = int(input())  # Number of items
    items = [input() for _ in range(N)]  # List of items and their prices
    
    # Print each item_name and net_price in order of its first occurrence
    print_items_with_net_price(N, items)
