# Recebe uma lista de 0 e 1 e retorn o valor em binário

def array_to_binary(arr):
    return int(''.join(map(str, arr)), 2)


array = [0, 0, 1, 0]
print(array_to_binary(array))
