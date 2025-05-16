def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
        print(fib[i])

    return fib[n-1]

print(fibo(10))