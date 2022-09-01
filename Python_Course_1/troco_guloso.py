moedas = [100, 50, 5, 1]
solucao = []
soma = 0
troco = 100.1  # valor a ser trocado
i = 0
while i < len(moedas) and soma != troco:
    if soma + moedas[i] <= troco:
        solucao.append(moedas[i])
        soma += moedas[i]
    else:
        i += 1

print(solucao)

