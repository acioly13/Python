# João Pedro Fernandes Acioly - 201921070 - Maricá - 4 Periodo
# Entrada de dados
n1 = int(input('Digite quantas caixas PEQUENAS você comprou: '))
n2 = int(input('Digite quantas caixas MEDIAS você comprou: '))
n3 = int(input('Digite quantas caixas GRANDES você comprou: '))

# Processamento de dados
pequena = n1 * 20
media = n2 * 30
grande = n3 * 45
total = pequena + media + grande

# Saida de dados
print(f'Total Arrecadado: {total} reais')
