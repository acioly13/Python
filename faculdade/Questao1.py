# João Pedro Fernandes Acioly - 201921070 - Maricá - 4 Periodo
# Entrada de dados
cidades = {}
lista = []
z = 0
while z != 10:
    cidade = input('Digite a cidade: ')
    celsius = float(input('Digite a temperatura media no mes de Julho: '))
    print(' ')
    lista.append(celsius)
    cidades.update({cidade: celsius})
    z += 1

# Processamento de dados
maior = max(lista)
cidade_maior = list(cidades.keys())[list(cidades.values()).index(maior)]

menor = min(lista)
cidade_menor = list(cidades.keys())[list(cidades.values()).index(menor)]

media_temperatura = sum(lista)/len(lista)
print('\n' * 150)
for cidade, celsius in cidades.items():
    print(f'Cidade: {cidade} | {celsius}°C | {(celsius * 1.8) + 32 }°F')

# Saida de dados
print(' ')
print(f'Cidade com maior media de temperatura: {cidade_maior}')
print(f'Cidade com menor media de temperatura: {cidade_menor}')
print(f'Media das Temperaturas: {media_temperatura}°C')

# Salvando em arquivo .txt
with open('temperaturas.txt', 'w') as arquivo:
    for cidade, celsius in cidades.items():
        print(f'Cidade: {cidade} | {celsius}°C | {(celsius * 1.8) + 32 }°F', file=arquivo)

    print(' ', file=arquivo)
    print(f'Cidade com maior media de temperatura: {cidade_maior}', file=arquivo)
    print(f'Cidade com menor media de temperatura: {cidade_menor}', file=arquivo)
    print(f'Media das Temperaturas: {media_temperatura}°C', file=arquivo)
