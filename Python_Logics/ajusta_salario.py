salario_atual = float(input("Digite Salario Atual: "))
if salario_atual < 500:
    novo_salario = salario_atual * 1.15
elif 500 <= salario_atual <= 1000:
    novo_salario = salario_atual * 1.10
else:
    novo_salario = salario_atual * 1.05
print(f'Novo Salario: {novo_salario:.2f}')
