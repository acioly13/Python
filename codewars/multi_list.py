# Recebe uma lista e retorna a multiplicação dos valores
from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


print(grow([1, 2, 3]))
print(grow([4, 1, 1, 1, 4]))