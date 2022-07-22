# Entradas
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
excesso = 0

# Processamento
if horas_trabalhadas > 50:
    excesso = horas_trabalhadas - 50
    horas_trabalhadas = horas_trabalhadas - excesso
extra = excesso * 20
salario = horas_trabalhadas * 10
salario_total = extra + salario
# Saida
print(f"Salario Total: {salario_total}")
print(f"Extra: {extra}")

