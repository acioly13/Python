# Busca Binaária

def binary_search(lista, chave, inicio, fim):
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2
    if lista[meio] == chave:
        return True
    elif lista[meio] > chave:
        return binary_search(lista, chave, inicio, meio - 1)
    return binary_search(lista, chave, meio + 1, fim)


# Teste
lista = [11, 5, 10, 20, 15, 4]
chave = 30
lista.sort()
if binary_search(lista, chave, 0, len(lista) - 1):
    print('A chave', chave, 'está na lista')
else:
    print('A chave', chave, 'não está na lista')
