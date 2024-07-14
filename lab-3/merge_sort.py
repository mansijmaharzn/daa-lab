count = 0
count_while = 0


def merge_sort(arr):
    global count
    global count_while

    count += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            count_while += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                print(arr)
            else:
                arr[k] = R[j]
                j += 1
                print(arr)
            k += 1

        while i < len(L):
            count_while += 1
            arr[k] = L[i]
            i += 1
            k += 1
            print(arr)
        
        while j < len(R):
            count_while += 1
            arr[k] = R[j]
            j += 1
            k += 1
            print(arr)


arr = [38, 27, 43, 3, 9, 82, 10, 25, 17, 30]
print("Giver Array: ", arr)

merge_sort(arr)
print("Sorted Array: ", arr)

print(f"Number of times function is called: {count}")
print(f"Number of times while loop is called: {count_while}")
print("Its significant is that it shows the number of steps.")