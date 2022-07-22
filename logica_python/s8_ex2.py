from random import *
# receba 2 vetores de 5 posições e some os valores de cada vetor em outro vetor
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(5):
    vetor1.append(randint(1, 99))
    vetor2.append(randint(1, 99))
    vetor3.append(vetor1[i] + vetor2[i])
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor 3: {vetor3}")
