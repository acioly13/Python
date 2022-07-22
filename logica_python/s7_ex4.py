# Algoritmo que le 10 valores e encontra maior, menor e media
maior = -999
menor = 999
media = 0
for i in range(5):
    n = int(input("Digite um valor: "))
    if n > 0:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        media += n / 5
    else:
        print("Valor invalido")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media}")

lista = []
for i in range(5):
    n = int(input("Digite um valor: "))
    lista.append(n)
print(f"Maior: {max(lista)}")
print(f"Menor: {min(lista)}")
print(f"Media: {sum(lista) / 5}")
