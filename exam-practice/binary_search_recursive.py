def binary_search(arr, l, r, key):
    flag = -1
    if l <= r:
        m = (l + r) // 2

        if key == arr[m]:
            flag = m
        
        elif key <= arr[m]:
            return binary_search(arr, l, m - 1, key)
        
        else:
            return binary_search(arr, m + 1, r, key)

    return flag


arr = [2, 3, 4, 5, 9, 11]
target = 9
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")