import random


def linear_search(arr, target):
    i = 0
    for element in arr:
        if element == target:
            return i
        i += 1
    
    return -1


arr = [3, 5, 2, 4, 9]
target = 4
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Modified version of linear search
def linear_search_modified(lst, item):
    steps = 0
    for index in range(len(lst)):
        steps += 1
        if lst[index] == item:
            return index, steps
    
    return -1, steps


random_list = [random.randint(0, 1000) for _ in range(1000)]
search_values = [random.randint(0, 1000) for _ in range(1000)]

total_steps = 0
for value in search_values:
    _, steps = linear_search_modified(random_list, value)
    total_steps += steps

average_steps = total_steps / len(search_values)
print(f"Average number of steps taken: {average_steps}")