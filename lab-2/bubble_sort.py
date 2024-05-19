"""
In this program:
a. Count number of steps taken
b. Count number of swaps

c. Modify it so that, if there are no swaps in one pass, the program stops.
Compare number of steps with older design
"""
def bubble_sort(a):
    print("Normal Bubble Sort")
    n = len(a)
    total_steps = 0
    swap_steps = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                swap_steps += 1
                a[j], a[j+1] = a[j+1], a[j]
                print(a)
            total_steps += 1
    
    print(f"a. Number of steps taken: {total_steps}")
    print(f"b. Number of swaps taken: {swap_steps}")


def bubble_sort_modified(a):
    print("c. Modified Bubble Sort")
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
                print(a)
            total_steps += 1
        
        if not swapped:
            break
    
    print(f"a. Number of steps taken: {total_steps}")
    print(f"b. Number of swaps taken: {swap_steps}")


bubble_sort([2, 1, 12, 19, 8, 16])
bubble_sort_modified([2, 1, 12, 19, 8, 16])