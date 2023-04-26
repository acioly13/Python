import random

num = random.randint(1, 100)

while True:

    resposta = int(input("Digite um número: "))
    if resposta < num:
        print("O número é maior")
    elif resposta > num:
        print("O número é menor")
    else:
        print("Você acertou")
        break
