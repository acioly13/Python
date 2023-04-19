# Retornar o número digital de um número inteiro

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
