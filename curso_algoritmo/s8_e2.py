vetor1 = []
vetor2 = []
soma = []
for i in range(5):
    valor1 = int(input('Digite um numero: '))
    vetor1.append(valor1)
    valor2 = int(input('Digite outro numero: '))
    vetor2.append(valor2)
    soma.append(vetor1[i]+vetor2[i])

print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Soma: {soma}')

