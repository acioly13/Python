# Receba altura e sexo de uma pessoa (M ou F) e imprima o seu peso ideal,
# utilizando as seguintes fórmulas: para homens: (72.7*altura) - 58, para mulheres: (62.1*altura) - 44.7
# Entradas
sexo = input("Digite seu sexo (M ou F): ")
altura = float(input("Digite sua altura (em metros): "))
# Processamento
if sexo.upper() == "M":
    peso = (72.7 * altura) - 58
    # Saída
    print(f"Peso ideal: {peso:.2f} kg")
elif sexo.upper() == "F":
    peso = (62.1 * altura) - 44.7
    # Saída
    print(f"Peso ideal: {peso:.2f} kg")
else:
    print("Sexo inválido!")
