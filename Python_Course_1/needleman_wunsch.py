# Algoritmo de Needleman-Wunsch
import sys


def needleman_wunsch(s1, s2, match, mismatch, gap):
    cols, lin = len(s1) + 1, len(s2) + 1
    # Cria a matriz
    matrix = [[0 for x in range(cols)] for y in range(lin)]
    # Direções para construir o alinhamento
    traceback = {}
    # Inicializa a primeira linha e coluna
    matrix[0][0] = 0
    for i in range(1, cols):
        matrix[0][i] = matrix[0][i - 1] + gap
        traceback[(0, i)] = (0, i - 1)
    for j in range(1, lin):
        matrix[j][0] = matrix[j - 1][0] + gap
        traceback[(j, 0)] = (j - 1, 0)

    # Retorna o valor máximo
    def max_valor(i, j):
        v1 = matrix[i - 1][j - 1] + (match if s1[j - 1] == s2[i - 1] else mismatch)  # Diagonal esquerda
        v2 = matrix[i - 1][j] + gap  # Cima
        v3 = matrix[i][j - 1] + gap  # Esquerda

        max_v = max(v1, v2, v3)

        if max_v == v1:
            traceback[(i, j)] = (i - 1, j - 1)
        elif max_v == v2:
            traceback[(i, j)] = (i - 1, j)
        else:
            traceback[(i, j)] = (i, j - 1)
        return max_v

    # Preenche a matriz
    for i in range(1, lin):
        for j in range(1, cols):
            matrix[i][j] = max_valor(i, j)

    s1_result, s2_result = '', ''  # Resultado dos alinhamentos
    i, j = lin - 1, cols - 1  # Inicia do ultimo valor

    while True:
        i_next, j_next = traceback[(i, j)]
        if i - 1 == i_next and j - 1 == j_next:  # Diagonal
            s1_result += s1[j_next]
            s2_result += s2[i_next]
        elif i - 1 == i_next and j == j_next:  # Cima
            s1_result += '-'
            s2_result += s2[i_next]
        elif i == i_next and j - 1 == j_next:  # Esquerda
            s1_result += s1[j_next]
            s2_result += '-'

        i, j = i_next, j_next
        if not i and not j:
            break

    s1_result, s2_result = s1_result[::-1], s2_result[::-1]
    print(f'{s1_result}\n{s2_result}\n')


if __name__ == "__main__":
    # Obtém a quantidade de argumentos passados
    len_args = len(sys.argv)
    if len_args == 6:
        s1, s2 = sys.argv[1], sys.argv[2]
        match, mismatch, gap = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
        needleman_wunsch(s1, s2, match, mismatch, gap)
    else:
        print('\nExecute: \n\tpython needleman_wunsch.py <s1> <s2> <match> <mismatch> <gap>')
        print('\nExemplo: \n\tpython needleman_wunsch.py GATTACA GATACA 1 -1 -1\n')
