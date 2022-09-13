# Implementação Insertion Sort

def insertion_sort(vetor):
    len_v = len(vetor)
    for i in range(1, len_v):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave


vetor = [4,3,2,1]
insertion_sort(vetor)
print(vetor)