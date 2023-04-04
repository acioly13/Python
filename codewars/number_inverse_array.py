# Recebe um numero e retorna um array com o inverso

def digitalize(n):
    return [int(digit) for digit in reversed(str(n))]


print(digitalize(123))
