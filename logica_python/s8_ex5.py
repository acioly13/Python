from random import randint
# Vetor que recebera 10 valores, mostrar os valores superiores a 50 e suas posições, mostrar mensagem se n tiver valores superiores a 50
vetor = []
maior_que_50 = False
for i in range(10):
    vetor.append(randint(0, 100))
    if vetor[i] > 50:
        print(f"Valor {vetor[i]} na posição {i} maior que 50")
        maior_que_50 = True
if not maior_que_50:
    print("Não há valores superiores a 50")
print(vetor)
