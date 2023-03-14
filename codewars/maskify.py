# Mascarar todos os caracteres de uma string, exceto os últimos 4

def maskify(cc):
    return '#'*(len(cc)-4) + cc[-4:]


# Teste
print(maskify('4556364607935616'))
print(maskify('64607935616'))
print(maskify('1'))
print(maskify(''))
print(maskify('TESTETESTETESTE'))