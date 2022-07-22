# algoritmo que determine o maior numero, condição de parada: 0
# Entrada
maior = -999
num = int(input('Digite um número: '))
# Processamento
while num != 0:
    if num > maior:
        maior = num
    num = int(input('Digite um número: '))
# Saída
print(f'O maior número é {maior}')
# algoritmo que determine o menor numero, condição de parada: 0
# Entrada
menor = 999
num2 = int(input('Digite um número: '))
# Processamento
while num2 != 0:
    if num2 < menor:
        menor = num2
    num2 = int(input('Digite um número: '))
# Saída
print(f'O menor número é {menor}')