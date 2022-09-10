# Implementação do Bubble Sort
import time


def bubble_sort(vetor):
    len_vetor = len(vetor)
    for i in range(len_vetor-1,0, -1):
        swapped = False
        for j in range(i):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                swapped = True
        if not swapped:
            break


vetor = [10, 40, 5, 15, 30, 70, 20]
start = time.time()
bubble_sort(vetor)
end = time.time()
print(vetor)
print("Tempo de execução: ", end - start)
