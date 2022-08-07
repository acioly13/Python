def potencia2(num):
    return num ** 2


potencia_2 = lambda num: num ** 2


def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


fatorial_2 = lambda num: num * fatorial(num - 1) if num > 0 else 1

lista = [1, 2, 3]
m = map(lambda x: x ** 2, lista)
for i in m:
    print(i)
