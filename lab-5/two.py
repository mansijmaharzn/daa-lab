a = [
    [3, 8, 4],
    [2, 9, 6],
    [8, 4, 9],
]

min_nums = []


for i in range(3):
    min = a[i][0]
    for j in range(3):
        if a[i][j] < min:
            min = a[i][j]
    min_nums.append(min)


print(f"Result: {min_nums}")