N = 5
COINS = {1, 3, 4}

ready = [False] * (N + 1)
value = [0] * (N + 1)
first = [0] * (N + 1)
best = float("inf")


# Recursive solution
def recursive_solve(x):
    global best, ready, value

    if x < 0:
        return float("inf")
    if x == 0:
        return 0
    if ready[x] == True:
        return value[x]
    for y in COINS:
       best = min(best, recursive_solve(x - y) + 1)
    ready[x] = True
    value[x] = best
    return best


# Iterative solution - also constructs solution
def iterative_solution(x):
    global value, first
    for y in range(1, x + 1):
        value[y] = float("inf")
        for c in COINS:
            if y - c > -1 and value[y] > value[y - c] + 1:
                value[y] = value[y - c] + 1
                first[y] = c
    return value[y]


# Iterative process that counts number of solutions
def iterative_count(x):
    count = [0] * (N + 1)
    count[0] = 1
    for y in range(1, x + 1):
        for c in COINS:
            if y - c > - 1:
                count[y] += count[y - c]
    return count[-1]


print(recursive_solve(N))
print(iterative_solution(N))
print(iterative_count(N))

# n = N
# output = []
# while n > 0:
#     output.append(first[n])
#     n -= first[n]
# print(output)

