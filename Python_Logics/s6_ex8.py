# Indicar se um numero é par ou impar, positivo ou negativo
# Entrada
num = int(input("Digite um numero: "))
# Processamento
if num > 0:
    if num % 2 == 0:
        print(f"{num} é positivo e par")
    else:
        print(f"{num} é positivo e impar")
elif num < 0:
    if num % 2 == 0:
        print(f"{num} é negativo e par")
    else:
        print(f"{num} é negativo e impar")
else:
    print("O numero é zero")
