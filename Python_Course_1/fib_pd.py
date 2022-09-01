# fibonacci com programação dinâmica
n = 50
mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1


def fib(n):
    if mem[n - 1] != -1:
        return mem[n - 1]
    mem[n - 1] = fib(n - 1) + fib(n - 2)
    return mem[n - 1]


print(fib(n))

