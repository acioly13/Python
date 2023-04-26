import statistics


def calcular_estatisticas(lista):
    # Ordenar a lista
    lista_ordenada = sorted(lista)

    # Calcular a média
    media = sum(lista_ordenada) / len(lista_ordenada)

    # Calcular a mediana
    if len(lista_ordenada) % 2 == 0:
        mediana = (lista_ordenada[len(lista_ordenada) // 2 - 1] + lista_ordenada[len(lista_ordenada) // 2]) / 2
    else:
        mediana = lista_ordenada[len(lista_ordenada) // 2]

    # Calcular a moda
    moda = statistics.mode(lista_ordenada)

    # Calcular o primeiro quartil (Q1)
    if len(lista_ordenada) % 2 == 0:
        Q1 = statistics.median(lista_ordenada[:len(lista_ordenada) // 2])
    else:
        Q1 = statistics.median(lista_ordenada[:len(lista_ordenada) // 2])

    # Retornar as estatísticas
    return media, mediana, moda, lista_ordenada, Q1


# Exemplo de uso
lista = [1, 51, 9, 21, 27, 11, 13, 15, 5, 33, 19]
media, mediana, moda, lista_ordenada, Q1 = calcular_estatisticas(lista)
print(f"Lista 1: {lista_ordenada}")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Primeiro Quartil: {Q1}")
print(f"Segundo Quartil: {mediana}")
print('\n')

lista2 = [40, 21, 19, 11, 27, 44, 11, 13, 15, 1, 22, 5, 25, 19]
media, mediana, moda, lista_ordenada, Q1 = calcular_estatisticas(lista2)
print(f"Lista 2: {lista_ordenada}")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Primeiro Quartil: {Q1}")
print(f"Segundo Quartil: {mediana}")
print('\n')

lista3 = [51, 11, 69, 41, 55, 11, 13, 15, 5, 33, 19]
media, mediana, moda, lista_ordenada, Q1 = calcular_estatisticas(lista3)
print(f"Lista 3: {lista_ordenada}")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Primeiro Quartil: {Q1}")
print(f"Segundo Quartil: {mediana}")
