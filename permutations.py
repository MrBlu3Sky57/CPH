n = int(input())
permutation = []
chosen = []

for x in range(n):
    chosen.append(False)

def search():
    if len(permutation) == n:
        print(permutation)
    else:
        for x in range(n):
            if(chosen[x] == True): continue
            chosen[x] = True
            permutation.append(x)
            search()
            chosen[x] = False
            permutation.remove(x)

search()