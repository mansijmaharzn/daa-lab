a = [
    [3, 8, 4],
    [2, 9, 6],
    [8, 4, 9],
]


max_nums = []


for i in range(3):
    max = a[i][0]
    for j in range(3):
        if a[i][j] > max:
            max = a[i][j]
    max_nums.append(max)


print(f"Result: {max_nums}")