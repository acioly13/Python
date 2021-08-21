vetor = []
codigo = int(input('Digite o codigo: '))
if codigo > 0:
    for i in range(5):
        valor = int(input('Digite um numero: '))
        vetor.append(valor)
    if codigo == 1:
        print(f'\nVetor: {vetor}')
    elif codigo == 2:
        vetor.reverse()
        print(f'\nVetor: {vetor}')
