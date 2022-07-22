from random import *
# receber vetor com 5 numeros e mostrar a ordem inversa
vetor = []
for i in range(5):
    vetor.append(randint(1, 99))
print(f"Vetor: {vetor}")
print(f"Ordem inversa: {vetor[::-1]}")