# criar vetor que armazene 5 valores e depois armazene os pares positivos
vetor = []
vetor_par = []
for i in range(5):
    vetor.append(int(input("Digite um valor: ")))
    if vetor[i] > 0 and vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
print(vetor_par)