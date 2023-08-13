N = 10
COINS = {1, 3, 4}

ready = [False] * (N + 1)
value = [0] * (N + 1)
best = float("inf")

def solve(x):
    global best, ready, value

    if x < 0:
        return float("inf")
    if x == 0:
        return 0
    if ready[x] == True:
        return value[x]
    for y in COINS:
       best = min(best, solve(x - y) + 1)
    ready[x] = True
    value[x] = best
    return best

print(solve(N))

