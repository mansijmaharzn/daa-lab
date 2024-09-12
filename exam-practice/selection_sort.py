def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]


arr = [4, 6, 9, 1, 2, 4, 6, 7,]
selection_sort(arr)
print(arr)