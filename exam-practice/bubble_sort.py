def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [4, 6, 9, 1, 2, 4, 6, 7,]
bubble_sort(arr)
print(arr)