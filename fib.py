
'''
def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n-1)+fib(n-2)


print(fib(n=int(input("Digite o Termo: "))))



def fib(n):
    if(n == 0):
        return 0
    else:
        if(n == 1):
            return 1
        else:
            P = 0
            U = 1
            for i in range(2, n):
                A = P + U
                P = U
                U = A
            return A


print(fib(n=int(input("Digite o Termo: "))))
'''
