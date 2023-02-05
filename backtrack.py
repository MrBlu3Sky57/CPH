n = int(input())
count = 0
column = [False] * (n*n)
diag1 = [False] * (n*n)
diag2 = [False] * (n*n)

def search(y):
    if y == n:
        count = count + 1
        return
    
    for x in range(n):
        if column[x] or diag1[x] or diag2[x]: continue
        column[x] = True
        diag1[x + y] = True
        diag2[x - y + n - 1] = True
        search(y+1)
        column[x] = False
        diag1[x + y] = False
        diag2[x - y + n - 1] = False


search(0)

print(count)

