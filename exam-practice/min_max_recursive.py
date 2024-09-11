def min_max(arr, low, high):
    if low == high:
        _min = _max = arr[low]
        return _min, _max
    
    elif low == (high - 1):
        if arr[low] > arr[high]:
            _min = arr[high]
            _max = arr[low]
        else:
            _max = arr[high]
            _min = arr[low]
        
        return _min, _max
    
    else:
        mid = (low + high) // 2
        min1, max1 = min_max(arr, low, mid)
        min2, max2 = min_max(arr, mid + 1, high)

        return min(min1, min2), max(max1, max2)


# Example usage
arr = [12, 11, 45, 8, 21, 500, 2]
min_val, max_val = min_max(arr, 0, len(arr) - 1)
print("Minimum:", min_val)
print("Maximum:", max_val)