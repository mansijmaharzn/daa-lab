a = [
    [3, 8, 4],
    [2, 9, 6],
    [8, 4, 9],
]

x = 0
for i in range(3):
    for j in range(i+1):
        x += a[i][j]


print(f"Value of x: {x}")