# [3, 6, 9, 1, 2, 5, 7]
# l                  r
# pi
#     i              j


def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1
    j = r

    while i <= j:
        # find greater than pivot from i
        while i <= r and pivot >= arr[i]:
            i += 1

        # find lower than pivot from j
        while j >= l and pivot < arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[l], arr[j] = arr[j], arr[l]

    return j


def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)



arr = [3, 6, 9, 1, 2, 5, 7, 0, 50]
quick_sort(arr, 0, len(arr)-1)
print(arr)