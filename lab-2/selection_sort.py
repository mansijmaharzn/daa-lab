def selection_sort(a):
    n = len(a)
    total_steps = 0
    swapped_steps = 0
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        
        if min != i:
            a[i], a[min] = a[min], a[i]
            swapped_steps += 1
            print(f"Swapped: {a}")
        
        print(f"Pass {i}: {a}")

        total_steps += 1


    print(f"a. Number of steps taken: {total_steps}")
    print(f"b. Number of swaps taken: {swapped_steps}")


selection_sort([2, 1, 12, 19, 8, 16])