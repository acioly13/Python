maior_valor = -999
menor_valor = 999
soma = 0
for i in range(1, 11):
    valor = int(input('Digite um valor: '))
    while valor < 0:
        valor = int(input('Digite um valor: '))
    if valor > maior_valor:
        maior_valor = valor
    if menor_valor == -1 or valor < menor_valor:
        menor_valor = valor
    soma = soma + valor
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')
print(f'Media: {soma/10}')
