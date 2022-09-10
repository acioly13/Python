# Gerando subconjuntos com Backtracking

def gerar_subconjuntos(S, vet, K, N):
    if K == N:
        print('{', end=' ')
        for i in range(N):
            if vet[i]:
                print('%d' % S[i], end=' ')
        print('}')
    else:
        vet[K] = True
        gerar_subconjuntos(S, vet, K + 1, N)
        vet[K] = False
        gerar_subconjuntos(S, vet, K + 1, N)


S = [1, 2]
tamS = len(S)
vet = [False for i in range(tamS)]
gerar_subconjuntos(S, vet, 0, tamS)
