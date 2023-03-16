# Encontrar o índice de um elemento em uma lista

def find_index(lista, chave):
    for i, v in enumerate(lista):
        if v == chave:
            return i
    return -1


# Teste
lista = [11, 5, 10, 20, 15, 4]
chave = 30
lista.sort()
if find_index(lista, chave) != -1:
    print('A chave', chave, 'está na lista')
else:
    print('A chave', chave, 'não está na lista')

