# João Pedro Fernandes Acioly - 201921070 - Maricá - 4 Periodo
# Entrada de dados
lotes = {}
lista = []
z = 0
while z != 20:
    lote = input('Digite o lote: ')
    tamanho = float(input('Digite a area em metros quadrados: '))
    print(' ')
    lista.append(tamanho)
    lotes.update({lote: tamanho})
    z += 1

# Processamento de dados
maior = max(lista)
lote_maior = list(lotes.keys())[list(lotes.values()).index(maior)]

menor = min(lista)
lote_menor = list(lotes.keys())[list(lotes.values()).index(menor)]

medias_lotes = sum(lista) / len(lista)

# Saida de dados
print('\n' * 150)
for lote, tamanho in lotes.items():
    print(f'Lote: {lote} | {tamanho} m²')


print(' ')
print(f'Maior Lote: {lote_maior}')
print(f'Menor Lote: {lote_menor}')
print(f'Media dos Lotes: {medias_lotes} m²')

# Salvando em arquivo .txt
with open('lotes.txt', 'w') as arquivo:
    for lote, tamanho in lotes.items():
        print(f'Lote: {lote} | {tamanho} m²', file=arquivo)

    print(' ', file=arquivo)
    print(f'Maior Lote: {lote_maior}', file=arquivo)
    print(f'Menor Lote: {lote_menor}', file=arquivo)
    print(f'Media dos Lotes: {medias_lotes} m²', file=arquivo)
