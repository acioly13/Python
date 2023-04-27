# Recebe um inteiro e retorna a quantidade de 1's em sua representação binária


def count_bits(n):
    return bin(n).count('1')


# Testes
print(count_bits(0))  # 0
print(count_bits(4))  # 1
print(count_bits(7))  # 3
print(count_bits(9))  # 2
