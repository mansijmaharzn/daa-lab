class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value to weight ratio


def knapsack_fractional(items, capacity):
    # Sort items by ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0
    total_weight = 0
    chosen_items = []
    
    for item in items:
        if total_weight + item.weight <= capacity:
            # Take the whole item
            total_weight += item.weight
            total_value += item.value
            chosen_items.append((item, 1))  # 1 indicates taking the full item
        else:
            # Take the fraction of the item
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item.weight
            total_weight += remaining_capacity
            total_value += item.value * fraction
            chosen_items.append((item, fraction))
            break  # Knapsack is full
    
    return total_value, total_weight, chosen_items


# Example usage:
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50
total_value, total_weight, chosen_items = knapsack_fractional(items, capacity)

print(f"Total value in knapsack = {total_value}")
print(f"Total weight in knapsack = {total_weight}")
print("Items chosen:")
for item, fraction in chosen_items:
    print(f"Value: {item.value}, Weight: {item.weight}, Ratio: {item.ratio}, Fraction taken: {fraction:.4f}")
