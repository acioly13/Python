vetor = []
vetor_par = []
for i in range(5):
    valor = int(input('Digite um numero: '))
    vetor.append(valor)
    if vetor[i] > 0 and vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
print(f'Pares: {vetor_par}')

