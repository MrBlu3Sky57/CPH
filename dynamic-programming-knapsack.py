N = 12
WEIGHTS = [1, 3, 3, 5]

possible = [False] * (N + 1)
possible[0] = True

for w in WEIGHTS:
    for x in reversed(range(0, N + 1)):
        if possible[x] == True:
            possible[x + w] = True 
print(possible)