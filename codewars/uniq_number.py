# Procura em uma lista de números inteiros, o número que não se repete

def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n


print(find_uniq([1, 1, 1, 2, 1, 1, 2, 3]))
