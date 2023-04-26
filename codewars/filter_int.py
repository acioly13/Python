# Recebe uma lista e retorna uma lista com apenas os inteiros

def filter_list(lista):
    return [i for i in lista if isinstance(i, int)]


print(filter_list([1, 2, 'a', 'b']))