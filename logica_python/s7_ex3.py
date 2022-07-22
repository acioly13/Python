# Algoritmo que indique escreva numeros e mostre se é impar
count = 0
for i in range(100, 201):
    if i % 2 != 0:
        print(f'{i} é impar')
        count += 1
print(f'Foram impares {count} numeros')