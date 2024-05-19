def insertion_sort(a):
    n = len(a)
    total_steps = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1

        if a[j+1] != key:
            a[j+1] = key
            print(f"Swap Step: {a}")

        total_steps += 1
        print(f"Pass {i}: {a}")
    
    print(f"Total Steps: {total_steps}")


insertion_sort([2, 1, 12, 19, 8, 16])