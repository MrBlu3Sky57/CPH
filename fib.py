term1 = 1
term2 = 1

def fib(n, term1, term2):
    if n == 0:
        print(end=" ")

    else:
        print(term1, end=" ")
        fib(n-1, term2, term1 + term2)
        
fib(4, 1, 1)