# Converter metros para centímetros e milímetros
# Entradas
z = 1
while z != 0:

    print("------Escolha a operação------")
    print("1) - Converter metros para centímetros")
    print("2) - Converter metros para milímetros")
    print("0) - Sair")
    z = int(input("\nDigite a opção desejada: "))

    if z == 1:
        print("\n"*200)
        print("------Metros para Centimetros------")
        metros = float(input("Digite o valor em metros: "))
        print("O valor em centímetros é: ", metros * 100, "cm")
    elif z == 2:
        print("\n"*200)
        print("------Metros para Milímetros------")
        metros = float(input("Digite o valor em metros: "))
        print("O valor em milímetros é: ", metros * 1000, "mm")
    elif z == 0:
        print("\n"*200)
        print("Saindo...")

