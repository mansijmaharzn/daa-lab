# 0/1 Knapsack problem by Greedy approach
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack_greedy(items, capacity):
    # Calculate value to weight ratio for each item
    for item in items:
        item.ratio = item.value / item.weight
    
    # Sort items by ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0
    total_weight = 0
    chosen_items = []
    
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
            chosen_items.append(item)
    
    return total_value, total_weight, chosen_items

# Example usage:
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

capacity = 50
total_value, total_weight, chosen_items = knapsack_greedy(items, capacity)

print(f"Total value in knapsack = {total_value}")
print(f"Total weight in knapsack = {total_weight}")
print("Items chosen:")
for item in chosen_items:
    print(f"Value: {item.value}, Weight: {item.weight}, Ratio: {item.ratio}")
