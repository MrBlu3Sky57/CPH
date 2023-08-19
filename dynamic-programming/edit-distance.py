X = "movie"
Y = "love"

M = len(X)
N = len(Y)

K = max(M, N)

X = "{:<{K}}".format(X, K=K)
Y = "{:<{K}}".format(Y, K=K)

distance = [[0] * (K + 1) for x in range(K + 1)]


def cost(a, b):
    if X[a - 1] == Y[b - 1]:
        return 0
    else:
        return 1

# def distance(a, b):
#     if a < 0 or b < 0:
#         return float("inf")
#     elif a == 0 and b == 0:
#         return 0
#     else:
#         return min(
#             distance(a - 1, b) + 1, 
#             distance(a, b - 1) + 1,
#             distance(a - 1, b - 1) + cost(a, b)
#         )
# print(distance(M, N))

for a in range(1, K + 1):
    for b in range(1, K + 1):
        distance[a][b] = min(
            distance[a - 1][b] + 1, 
            distance[a][b - 1] + 1,
            distance[a - 1][b - 1] + cost(a, b)
        )
print(distance[M][N])