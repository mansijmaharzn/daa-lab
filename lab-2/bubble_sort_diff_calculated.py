"""
In this program:
a. Count number of steps taken
b. Count number of swaps

c. Modify it so that, if there are no swaps in one pass, the program stops.
Compare number of steps with older design
"""
def bubble_sort(a):
    print("\nNormal Bubble Sort")
    n = len(a)
    total_steps = 0
    swap_steps = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                swap_steps += 1
                a[j], a[j+1] = a[j+1], a[j]
                print(f"Swapped: {a}")
            total_steps += 1
    
    return total_steps, swap_steps


def bubble_sort_modified(a):
    print("\nModified Bubble Sort")
    n = len(a)
    total_steps = 0
    swap_steps = 0
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j+1]:
                swapped = True
                swap_steps += 1
                a[j], a[j+1] = a[j+1], a[j]
                print(f"Swapped: {a}")
            total_steps += 1
        
        if not swapped:
            break
    
    return total_steps, swap_steps


total_steps, swap_steps = bubble_sort([2, 1, 12, 19, 8, 16])
modified_total_steps, modified_swap_steps = bubble_sort_modified([2, 1, 12, 19, 8, 16])

print(f"a. Number of steps taken by normal bubble sort: {total_steps}")
print(f"b. Number of swaps taken by normal bubble sort: {swap_steps}")

print(f"c.\nNumber of steps taken by modified bubble sort: {modified_total_steps}")
print(f"Number of swaps taken by modified bubble sort: {modified_swap_steps}")

print(f"Difference in total steps: {total_steps - modified_total_steps}")
print(f"Difference in total swaps: {swap_steps - modified_swap_steps}")