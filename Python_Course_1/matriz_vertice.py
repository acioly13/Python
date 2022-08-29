matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],

]
n = len(matriz)
for i in range(n):
    grau = 0
    for j in range(n):
        if matriz[i][j] == 1:
            grau += 1
    print(f'O vertice {i} tem grau {grau}')