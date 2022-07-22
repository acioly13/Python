def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


"""
fat(3)
    3 * fat(2)
    fat(2)
        2 * fat(1)
        fat(1)
            1 * fat(0)
            fat(0)
                1
"""

# Fibonacci enesimo termo
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Fibonacci até enesimo termo
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Calcular potencia
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente-1)