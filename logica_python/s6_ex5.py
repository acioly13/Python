# Entradas
excesso = 0
multa = 0
peso_peixe = float(input("Digite o peso do peixe: "))
if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
print(f"Peso: {peso_peixe}")
print(f"Excesso: {excesso}")
print(f"Multa: {multa}")
