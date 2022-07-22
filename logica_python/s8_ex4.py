# vetr que receba 5 elementos e mostre a soma deles
vetor = []
for i in range(1, 6):
    vetor.append(int(input(f"Informe valor {i}/5  para adicionar ao vetor: ")))
print(f"Vetor: {vetor}")
print(f"Soma: {sum(vetor)}")
