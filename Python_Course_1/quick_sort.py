def particiona(v, inicio, final):
    # O pívo sera o element do inicio
    pivo = inicio
    for i in range(inicio + 1, final +1):
        if v[i] <= v[inicio]:
            pivo += 1
            v[i], v[pivo] = v[pivo], v[i]
    v[inicio], v[pivo] = v[pivo], v[inicio]
    return pivo


def quick_sort(v, inicio, final):
    """
       Se o fim for maior que o início, entao calculase a posição do pivo utilizando a função particiona
    """
    if final > inicio:
        # Separa os dados em duas partições
        pivo = particiona(v, inicio, final)
        """Tendo o pivo, chama a função duas vezes para cada partição, uma para a partição da esquerda e outra para a 
        partição da direita """

        quick_sort(v, inicio, pivo - 1)
        quick_sort(v, pivo + 1, final)


v = [4, 3, 2, 1]
quick_sort(v, 0, len(v) - 1)
print(v)