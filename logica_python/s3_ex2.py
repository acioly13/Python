# Calcular o estoque medio de uma peça
# Entrada
quantidade_minima = int(input('Digite a quantidade mínima da peça: '))
quantidade_maxima = int(input('Digite a quantidade máxima da peça: '))
# Processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
# Saída
print(f'Estoque medio: {estoque_medio}')
