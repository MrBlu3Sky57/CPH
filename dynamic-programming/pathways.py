import numpy as np

N = 5
value = [[3, 7, 9, 2, 7], [9, 8, 3, 5, 5], [1, 7, 9, 8, 5], [3, 8, 6, 4, 10], [6, 3, 9, 7, 8]]
sum = np.zeros((N + 1, N + 1), dtype=int)

for x in range(1, N + 1):
    for y in range(1, N + 1):
        sum[y][x] = max(sum[y-1][x], sum[y][x-1]) + value[y - 1][x - 1]

print(sum[N][N])