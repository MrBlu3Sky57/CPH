arr = [6, 2, 5, 1, 7, 4, 8, 3]
N = len(arr)
length = [1] * N
global_best = 0

def solve(x):
    global global_best
    for x in range(1, N):
        local_best = 1
        for y in range(0, x):
            if arr[y] < arr[x]:
                global_best = max(global_best, length[y] + 1)
                local_best = max(local_best, length[y] + 1)
                length[x] = local_best
    return global_best
                
print(solve(N))