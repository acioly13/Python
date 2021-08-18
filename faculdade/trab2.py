from random import random, randint
import time

matrizA = []
matrizB = []
matrizC = []
n = 3

for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(1, 3))
print("Matriz A")
for l in range(0, n):
    for c in range(0, n):
        print(f'[{matrizA[l][c]:^5}]', end="")
    print()
print(" ")
print("Matriz B")
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(1, 3))
for l in range(0, n):
    for c in range(0, n):
        print(f'[{matrizB[l][c]:^5}]', end="")
    print()
print(" ")
print("Matriz AxB")

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
for l in range(0, n):
    for c in range(0, n):
        print(f'[{matrizC[l][c]:^5}]', end="")
    print()
print(" ")
