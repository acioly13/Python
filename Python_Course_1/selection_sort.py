# Implementação do Selection Sort

def selection_sort(vetor):
    len_vetor = len(vetor)
    for i in range(len_vetor - 1):
        menor = i
        for j in range(i + 1, len_vetor):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[menor], vetor[i] = vetor[i], vetor[menor]


vetor = [4,3,2,1]
selection_sort(vetor)
print(vetor)
