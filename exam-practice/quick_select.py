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


def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k:
            return arr[pi]
        elif pi < k:
            return quickselect(arr, pi + 1, high, k)
        else:
            return quickselect(arr, low, pi - 1, k)
    return None


def find_kth_order_statistic(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds")
        
    return quickselect(arr, 0, len(arr) - 1, k - 1)


# Example usage
arr = [4, 7, 9, 1, 2, 4, 6, 7]
k = 5
print(find_kth_order_statistic(arr, k))
