"""
0/1 Knapsack by backtracking.
"""

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def knapsack_backtracking(index, current_weight, current_value, current_items):
    global max_value, best_items

    if current_weight > capacity:
        return

    if current_value > max_value:
        max_value = current_value
        best_items = current_items[:]

    if index == len(items):
        return

    item = items[index]

    # Include the item
    current_items.append(item)
    knapsack_backtracking(index + 1, current_weight + item.weight, current_value + item.value, current_items)
    current_items.pop()

    # Exclude the item
    knapsack_backtracking(index + 1, current_weight, current_value, current_items)


# Example usage:
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

capacity = 50
max_value = 0
best_items = []

knapsack_backtracking(0, 0, 0, [])

total_weight = sum(item.weight for item in best_items)
print(f"Total value in knapsack = {max_value}")
print(f"Total weight in knapsack = {total_weight}")
print("Items chosen:")
for item in best_items:
    print(f"Value: {item.value}, Weight: {item.weight}")