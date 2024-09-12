def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]

        while j >= 0 and key <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key


arr = [4, 6, 9, 1, 2, 4, 6, 7,]
insertion_sort(arr)
print(arr)