from random import randint
# receber codigo, se codigo = 0 terminar programa, 1 mostrar vetor,2 mostrar vetor ordem inversa
vetor = []
codigo = int(input("Digite o código: "))
if codigo > 0:
    for i in range(1, 11):
        vetor.append(randint(0, 100))
    if codigo == 1:
        print(f"Vetor: {vetor}")
    elif codigo == 2:
        print(f"Vetor ordem inversa: {vetor[::-1]}")
