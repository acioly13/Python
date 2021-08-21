vetor = []
maior50 = False
for i in range(5):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

print(f'\nVetor: {vetor}')
for i in range(5):
    if vetor[i] > 50:
        print(f'Valor: {vetor[i]} na posição {i}')
        maior50 = True

if not maior50:
    print('Não existem valores maiores que 50')
