vetor = []
soma = 0
for i in range(5):
    n = int(input('Digite um numero: '))
    vetor.append(n)
    soma += vetor[i]

print(f'Vetor: {vetor}')
print(f'Soma: {soma}')
