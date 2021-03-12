from random import random, randint
import time

'''
Nome: João Pedro Fernandes Acioly 
Data: 30/06/2020 
Disciplina: Estrutura de Dados 
Curso: Engenharia de Software 
Professor: Andre 
'''

inicio = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10
print('-'*16, 'Teste 01', '-'*16)
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim = time.time()
print(" ")
print(f'N: {n}')
print(f'Tempo de execução: {fim - inicio}')
print("")

inicio2 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 100
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim2 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim2 - inicio2}')
print(" ")


inicio3 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 1000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim3 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim3 - inicio3}')
print(" ")
'''
inicio4 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim4 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim4 - inicio4}')
print(" ")
'''


inicio5 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10
print('-'*16, 'Teste 02', '-'*16)
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim5 = time.time()
print(" ")
print(f'N: {n}')
print(f'Tempo de execução: {fim5 - inicio5}')
print("")

inicio6 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 100
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim6 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim6 - inicio6}')
print(" ")


inicio7 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 1000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim7 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim7 - inicio7}')
print(" ")
'''
inicio8 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim8 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim8 - inicio8}')
print(" ")
'''

inicio9 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10
print('-'*16, 'Teste 03', '-'*16)
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim9 = time.time()
print(" ")
print(f'N: {n}')
print(f'Tempo de execução: {fim9 - inicio9}')
print("")

inicio10 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 100
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))
for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))
for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]
fim10 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim10 - inicio10}')
print(" ")


inicio11 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 1000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim11 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim11 - inicio11}')
print(" ")
'''
inicio12 = time.time()
matrizA = []
matrizB = []
matrizC = []
n = 10000
for i in range(n):
    matrizA.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizA[l][c] = int(randint(0, 999))

for i in range(n):
    matrizB.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizB[l][c] = int(randint(0, 999))

for i in range(n):
    matrizC.append([0]*n)
for l in range(0, n):
    for c in range(0, n):
        matrizC[l][c] = matrizA[l][c]*matrizB[l][c]

fim12 = time.time()
print(f'N: {n}')
print(f'Tempo de execução:{fim12 - inicio12}')
print(" ")
'''
